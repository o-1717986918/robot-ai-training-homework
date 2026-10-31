"""Remove ONLY student-authored unit-test requirements from pinned Seasons/Jar.

All upstream program/class checks and their fixture files remain unchanged.
The check50 framework still executes the resulting checks; this is an explicitly
adapted behavior subset, not a claim of passing the full original assignment.
"""
import ast
import hashlib
import json
from pathlib import Path
import shutil

OMIT = {
    "seasons": {"test_student_file_passes"},
    "jar": {"test_student_file_passes", "test_number_functions",
            "test_named_functions", "test_valid_testing"},
}


def adapt(upstream, destination):
    destination.mkdir(parents=True, exist_ok=True)
    audit = []
    for exercise, removed in OMIT.items():
        source = upstream / exercise
        target = destination / exercise
        shutil.copytree(source, target)
        filename = target / "__init__.py"
        original = filename.read_text(encoding="utf-8")
        lines = original.splitlines(keepends=True)
        tree = ast.parse(original)
        omitted_lines = set()
        found = set()
        for node in tree.body:
            if not isinstance(node, ast.FunctionDef):
                continue
            if node.name in removed:
                found.add(node.name)
                first = min([node.lineno] + [d.lineno for d in node.decorator_list])
                omitted_lines.update(range(first, node.end_lineno + 1))
            elif node.name == "exists":
                for statement in node.body:
                    if (isinstance(statement, ast.Expr)
                            and isinstance(statement.value, ast.Call)
                            and isinstance(statement.value.func, ast.Attribute)
                            and statement.value.func.attr == "exists"
                            and statement.value.args
                            and isinstance(statement.value.args[0], ast.Constant)
                            and statement.value.args[0].value == f"test_{exercise}.py"):
                        omitted_lines.update(range(statement.lineno, statement.end_lineno + 1))
        if found != removed:
            raise ValueError(f"Unexpected upstream layout for {exercise}: {found}")
        modified = "".join(line for i, line in enumerate(lines, 1) if i not in omitted_lines)
        modified = modified.replace('seasons.py and test_seasons.py exist', 'seasons.py exists')
        ast.parse(modified)
        filename.write_text(modified, encoding="utf-8")
        config=target/".cs50.yml"
        config_original=config.read_text(encoding="utf-8")
        require=f"    - !require test_{exercise}.py"
        if config_original.count(require)!=1:
            raise ValueError(f"Unexpected required-file configuration for {exercise}")
        config_modified="".join(line for line in config_original.splitlines(keepends=True)
                                if line.strip()!=require.strip())
        config.write_text(config_modified,encoding="utf-8")
        remaining = [n.name for n in ast.parse(modified).body
                     if isinstance(n, ast.FunctionDef) and n.decorator_list]
        audit.append({
            "exercise": exercise,
            "mode": "upstream behavior subset; student test-file assignment removed",
            "removed_checks": sorted(removed),
            "removed_exists_requirement": f"test_{exercise}.py",
            "retained_checks": remaining,
            "upstream_source_sha256": hashlib.sha256(original.encode()).hexdigest(),
            "adapted_source_sha256": hashlib.sha256(modified.encode()).hexdigest(),
            "removed_config_requirement": f".cs50.yml: !require test_{exercise}.py",
            "upstream_config_sha256": hashlib.sha256(config_original.encode()).hexdigest(),
            "adapted_config_sha256": hashlib.sha256(config_modified.encode()).hexdigest(),
        })
    (destination / "adaptation.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")
    return audit
