"""Association smoke/boundary checks; these are not Harvard's check50 checks."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def module(path):
    spec = importlib.util.spec_from_file_location('candidate_' + path.stem, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('--problems',nargs='+',default=['faces','tip','bank','meal','coke','twttr','plates','nutrition'])
    parser.add_argument('--task-name',default='task01')
    args = parser.parse_args()
    results = []
    def check(name, callback):
        if name.split()[0] not in args.problems:
            return
        start = time.perf_counter()
        try:
            callback()
            result = {'name': name, 'passed': True}
        except Exception as exc:
            result = {'name': name, 'passed': False, 'error': str(exc)}
        result['seconds'] = round(time.perf_counter() - start, 4)
        results.append(result)
        print(('PASS ' if result['passed'] else 'FAIL ') + name)

    def cli(problem, stdin, required=(), forbidden=()):
        path = args.root / problem / (problem + '.py')
        p = subprocess.run([sys.executable, str(path)], input=stdin, text=True,
                           capture_output=True, encoding='utf-8', timeout=5,
                           env={**os.environ, 'PYTHONIOENCODING': 'utf-8'})
        assert p.returncode == 0, p.stderr
        for text in required:
            assert text in p.stdout, repr(p.stdout)
        for text in forbidden:
            assert text not in p.stdout, repr(p.stdout)

    for given, expected in [('Hello :)', 'Hello 🙂'), (':( :) :(', '🙁 🙂 🙁'), ('AbC!?', 'AbC!?')]:
        check('faces ' + given, lambda g=given,e=expected: cli('faces', g+'\n', [e]))
    for amount, percent, expected in [('$50.00', '15%', '$7.50'), ('$100.00', '18%', '$18.00')]:
        check('tip '+amount, lambda a=amount,p=percent,e=expected: cli('tip', a+'\n'+p+'\n', [e]))
    for given, expected in [('  HELLO there', '$0'), ('How are you?', '$20'), ('Welcome', '$100')]:
        check('bank '+given, lambda g=given,e=expected: cli('bank', g+'\n', [e]))
    for given, expected in [('7:00', 'breakfast time'), ('8:00', 'breakfast time'), ('12:30', 'lunch time'), ('19:00', 'dinner time')]:
        check('meal '+given, lambda g=given,e=expected: cli('meal', g+'\n', [e]))
    check('meal outside intervals', lambda: cli('meal', '8:01\n', forbidden=['breakfast time','lunch time','dinner time']))
    check('coke invalid coin and overpay', lambda: cli('coke', '30\n25\n10\n25\n', ['Change Owed: 10']))
    check('coke exact payment', lambda: cli('coke', '25\n25\n', ['Change Owed: 0']))
    for given, expected in [('AEIOUaeiou123!?', '123!?'), ('Twitter', 'Twttr')]:
        check('twttr '+given, lambda g=given,e=expected: cli('twttr', g+'\n', ['Output: '+e]))
    for given, expected in [('CS50', 'Valid'), ('CS05','Invalid'), ('AA12A','Invalid'), ('A1','Invalid'), ('AA.','Invalid'), ('ABCDEFG','Invalid'), ('AB','Valid')]:
        check('plates '+given, lambda g=given,e=expected: cli('plates', g+'\n', [': '+e+'\n']))
    for given, expected in [('aPPLe', '130'), ('Sweet Cherries', '100'), ('Watermelon','80')]:
        check('nutrition '+given, lambda g=given,e=expected: cli('nutrition', g+'\n', ['Calories: '+e]))
    check('nutrition unknown', lambda: cli('nutrition', 'Tomato\n', forbidden=['Calories:']))
    data = {'task': 'phase1/'+args.task_name, 'python': sys.executable, 'python_version': sys.version,
            'passed': sum(r['passed'] for r in results), 'total': len(results), 'checks': results}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"{data['passed']}/{data['total']} passed")
    return 0 if data['passed'] == data['total'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
