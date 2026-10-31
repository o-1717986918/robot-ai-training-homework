"""Select an assignment from a documented branch name or explicit CI input."""
import argparse
import os
from pathlib import Path
import re
import subprocess
import sys


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--student-root',type=Path,default=Path('.'))
    parser.add_argument('--checks-root',type=Path,required=True)
    parser.add_argument('--output',type=Path,default=Path('artifacts'))
    parser.add_argument('--task',choices=['task01','task02','task03','task04','all'])
    args=parser.parse_args()
    selected=args.task or os.environ.get('REQUESTED_TASK')
    if not selected:
        branch=os.environ.get('PR_HEAD_REF','')
        match=re.fullmatch(r'phase1-(task0[1-4])',branch)
        if not match:
            parser.error('Use a phase1-task01..04 PR branch or choose task in workflow_dispatch.')
        selected=match.group(1)
    if selected not in ('task01','task02','task03','task04','all'):
        parser.error('invalid task')
    grading=Path(__file__).resolve().parent
    args.output.mkdir(parents=True,exist_ok=True)
    failed=False
    tasks=range(1,5) if selected=='all' else [int(selected[-2:])]
    for number in tasks:
        commands=[[sys.executable,str(grading/'run_official_checks.py'),'--student-root',str(args.student_root),
                   '--checks-root',str(args.checks_root),'--output',str(args.output/f'check50-task{number:02}'),'--task',str(number)]]
        if number in (1,2,3):
            commands.append([sys.executable,str(grading/f'grade_task{number:02}.py'),'--root',str(args.student_root/f'phase1/task{number:02}'),
                             '--report',str(args.output/f'task{number:02}-local.json')])
        else:
            commands.append([sys.executable,str(grading/'grade_task04.py'),'--root',str(args.student_root/'phase1/task04'),
                             '--output',str(args.output/'task04-images')])
        for command in commands:
            print('RUN',subprocess.list2cmdline(command),flush=True)
            p=subprocess.run(command)
            failed=failed or p.returncode!=0
    return int(failed)


if __name__=='__main__':
    raise SystemExit(main())
