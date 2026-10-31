"""Run pinned, official check50 checks locally; never submit to a CS50 gradebook."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import tempfile
import shutil
from adapt_checks import adapt


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--student-root',type=Path,required=True)
    parser.add_argument('--checks-root',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--task',type=int,choices=(1,2,3,4))
    parser.add_argument('--exercise')
    args=parser.parse_args()
    manifest=json.loads(Path(__file__).with_name('official_manifest.json').read_text(encoding='utf-8'))
    args.output.mkdir(parents=True,exist_ok=True)
    commit=subprocess.check_output(['git','-C',str(args.checks_root),'rev-parse','HEAD'],text=True).strip()
    if commit!=manifest['commit']:
        raise SystemExit(f'Unexpected upstream check commit: {commit}')
    if sys.version_info[:2]!=(3,13):
        raise SystemExit('Course checker uses Python 3.13; run official checks in Actions/the checker environment.')
    temporary=tempfile.TemporaryDirectory(prefix='course-check50-')
    adapted=Path(temporary.name)
    audit=adapt(args.checks_root,adapted)
    shutil.copyfile(adapted/'adaptation.json',args.output/'adaptation.json')
    summaries=[]
    for item in manifest['exercises']:
        if args.task and item['task']!=args.task:
            continue
        if args.exercise and item['checks_path']!=args.exercise:
            continue
        student=(args.student_root/item['student_path']).resolve()
        checks=(args.checks_root/item['checks_path']).resolve()
        item={**item,'checks_mode':'official unmodified'}
        if item['checks_path'] in ('seasons','jar'):
            checks=adapted/item['checks_path']
            item['checks_mode']='official behavior subset; student test-file checks excluded'
        name=item['checks_path'].replace('/','_')
        command=['check50','--dev',str(checks),'--output','json']
        started=time.perf_counter()
        try:
            # Official unit-test checks rapidly rewrite same-sized wrapper modules.
            # Do not let timestamp/size-based .pyc caches reuse an earlier wrapper.
            env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'}
            p=subprocess.run(command,cwd=student,capture_output=True,text=True,encoding='utf-8',timeout=180,env=env)
            (args.output/(name+'.stdout.txt')).write_text(p.stdout,encoding='utf-8')
            (args.output/(name+'.stderr.txt')).write_text(p.stderr,encoding='utf-8')
            result=json.loads(p.stdout)
            if 'error' in result:
                raise RuntimeError(result['error'].get('value',str(result['error'])))
            passed=sum(c['passed'] is True for c in result['results'])
            total=len(result['results'])
            success=p.returncode==0 and total>0 and passed==total
            summary={**item,'passed':success,'passed_checks':passed,'total_checks':total,'exit_code':p.returncode,
                     'failures':[c for c in result['results'] if c['passed'] is not True]}
        except Exception as exc:
            summary={**item,'passed':False,'error':str(exc)}
        summary['seconds']=round(time.perf_counter()-started,3)
        summaries.append(summary)
        print(('PASS ' if summary['passed'] else 'FAIL ')+item['checks_path']+' '+str(summary.get('passed_checks'))+'/'+str(summary.get('total_checks')),flush=True)
        # Save after every exercise so an interrupted run keeps completed evidence.
        data={'upstream_commit':commit,'check50':manifest['check50'],'python':sys.version,
              'passed_exercises':sum(s['passed'] for s in summaries),'total_exercises':len(summaries),
              'exercises':summaries,'mode':'local --dev; no official gradebook submission'}
        (args.output/'summary.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    if not summaries:
        parser.error('no exercises matched')
    return int(not all(s['passed'] for s in summaries))


if __name__=='__main__':
    raise SystemExit(main())
