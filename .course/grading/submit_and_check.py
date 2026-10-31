"""Submit one assignment and display its GitHub Actions feedback in the terminal."""
import argparse
import html
import json
import re
import subprocess
import sys
import time
from pathlib import Path

REPOSITORY = "o-1717986918/robot-ai-training-homework"
WORKFLOW = "phase1-autograde.yml"


def command(args, *, capture=False, check=True):
    try:
        result = subprocess.run(args, text=True, encoding="utf-8", errors="replace",
                                stdout=subprocess.PIPE if capture else None,
                                stderr=subprocess.PIPE if capture else None)
    except FileNotFoundError as exc:
        raise RuntimeError(f"找不到 {args[0]}。请先按作业文档安装并重开终端。") from exc
    if check and result.returncode:
        detail = (result.stderr or result.stdout or "").strip() if capture else ""
        raise RuntimeError(f"命令执行失败：{args[0]}。{detail}")
    return result


def git(*args, capture=False, check=True):
    return command(["git", *args], capture=capture, check=check)


def gh(*args, capture=False, check=True):
    return command(["gh", *args], capture=capture, check=check)


def feedback(log, task):
    lines = []
    in_step = False
    for line in log.splitlines():
        parts = line.split("\t", 2)
        if len(parts) != 3 or parts[0] != f"Check {task}" or parts[1] != "Show per-problem feedback":
            continue
        value = re.sub(r"^\S+\s+", "", parts[2])
        if value.startswith(f"# {task} · 逐题反馈"):
            in_step = True
        if in_step:
            value = html.unescape(value.replace("<br>", "\n"))
            value = value.replace("<pre>", "").replace("</pre>", "")
            lines.append(value)
    return "\n".join(lines).strip()


def main():
    parser = argparse.ArgumentParser(description="提交第一阶段作业并在终端显示自动评测结果")
    parser.add_argument("task", choices=["task01", "task02", "task03", "task04"])
    args = parser.parse_args()
    task_path = f"phase1/{args.task}"
    try:
        root = git("rev-parse", "--show-toplevel", capture=True).stdout.strip()
        if not (Path(root) / ".course/grading/submit_and_check.py").is_file():
            raise RuntimeError("请在培训方作业仓库目录运行本命令。")
        auth = gh("auth", "status", "--hostname", "github.com", capture=True, check=False)
        if auth.returncode:
            raise RuntimeError("请先运行 gh auth login --hostname github.com --git-protocol https --web 完成登录。")
        branch = git("branch", "--show-current", capture=True).stdout.strip()
        if not branch:
            raise RuntimeError("请先切换到自己的学员分支。")
        print(f"\n准备提交 {task_path}，当前分支：{branch}", flush=True)
        git("add", "--", task_path)
        changed = git("diff", "--cached", "--quiet", "--", task_path, check=False).returncode
        if changed == 1:
            git("commit", "-m", f"complete phase1 {args.task}", "--", task_path)
        elif changed != 0:
            raise RuntimeError("无法读取暂存区，请检查 Git 状态。")
        else:
            print("本任务没有新的修改，将查看当前提交的评测结果。", flush=True)
            files = git("show", "--format=", "--name-only", "HEAD", capture=True).stdout.splitlines()
            if not any(name.startswith(task_path + "/") for name in files):
                raise RuntimeError("当前提交没有修改本任务的文件；修改作业后重新运行本命令。")
        sha = git("rev-parse", "HEAD", capture=True).stdout.strip()
        git("push", "-u", "origin", branch)
        print("\n正在等待 GitHub Actions 检测，请保持终端打开……", flush=True)
        deadline = time.monotonic() + 900
        run_id = None
        while time.monotonic() < deadline:
            runs = gh("run", "list", "--repo", REPOSITORY, "--workflow", WORKFLOW,
                      "--branch", branch, "--limit", "50", "--json",
                      "databaseId,headSha,event,status,conclusion", capture=True)
            matches = [run for run in json.loads(runs.stdout)
                       if run["headSha"] == sha and run["event"] == "push"]
            if matches:
                run = matches[0]
                run_id = run["databaseId"]
                if run["status"] == "completed":
                    break
            time.sleep(5)
        else:
            raise RuntimeError("等待超时。确认本次提交修改了该任务目录，然后重新运行本命令查看。")
        details = gh("run", "view", str(run_id), "--repo", REPOSITORY, "--log", capture=True)
        report = feedback(details.stdout, args.task)
        if not report:
            raise RuntimeError("未找到本任务的逐题反馈。请确认这次提交修改了对应任务；也可用 gh run view "
                               f"{run_id} --repo {REPOSITORY} --log 查看运行日志。")
        print("\n" + report, flush=True)
        return 0 if run["conclusion"] == "success" else 1
    except (RuntimeError, ValueError, json.JSONDecodeError) as exc:
        print(f"\n无法完成终端评测：{exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="backslashreplace")
        sys.stderr.reconfigure(errors="backslashreplace")
    raise SystemExit(main())
