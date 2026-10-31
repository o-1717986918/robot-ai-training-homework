import argparse
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
from unittest.mock import patch
from pyfiglet import Figlet


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--root',type=Path,required=True)
    parser.add_argument('--report',type=Path,required=True)
    args=parser.parse_args()
    results=[]
    def check(name,callback):
        try:
            callback()
            record={'name':name,'passed':True}
        except Exception as exc:
            record={'name':name,'passed':False,'error':str(exc)}
        results.append(record)
        print(('PASS ' if record['passed'] else 'FAIL ')+name)
    def cli(problem,stdin,required=(),argv=(),exit_code=0,last_line=None):
        p=subprocess.run([sys.executable,str(args.root/problem/(problem+'.py')),*argv],input=stdin,
                         capture_output=True,text=True,encoding='utf-8',timeout=30)
        assert p.returncode==exit_code, (p.returncode,p.stderr)
        for text in required:
            assert text in p.stdout+p.stderr,repr(p.stdout+p.stderr)
        if last_line is not None:
            assert p.stdout.strip().splitlines()[-1]==last_line,repr(p.stdout)
    for given,expected in [('1/4\n','25%'),('1/100\n','E'),('99/100\n','F'),
                            ('cat/dog\n1/0\n5/4\n-1/4\n1/2\n','50%')]:
        check('fuel '+repr(given),lambda g=given,e=expected:cli('fuel',g,[e]))
    check('grocery count order EOF',lambda:cli('grocery','banana\nApple\napple\n',['2 APPLE\n1 BANANA\n']))
    for names,expected in [('Ada\n','Ada'),('Ada\nBob\n','Ada and Bob'),('Ada\nBob\nCarol\n','Ada, Bob, and Carol')]:
        check('adieu '+repr(names),lambda n=names,e=expected:cli('adieu',n,last_line='Adieu, adieu, to '+e))
    check('figlet named font',lambda:cli('figlet','CS50\n',[Figlet(font='slant').renderText('CS50')],['-f','slant']))
    for argv in [['one'],['-a','slant'],['-f','not_a_font'],['-f','slant','extra']]:
        check('figlet rejects '+repr(argv),lambda a=argv:cli('figlet','',['Invalid usage'],a,1))
    check('figlet random font executes',lambda:cli('figlet','CS50\n'))
    spec=importlib.util.spec_from_file_location('professor',args.root/'professor/professor.py')
    professor=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(professor)
    def ranges():
        for level in (1,2,3):
            lower=0 if level==1 else 10**(level-1)
            for _ in range(100):
                assert lower<=professor.generate_integer(level)<10**level
        try:
            professor.generate_integer(4)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid level was accepted')
    check('professor ranges and invalid level',ranges)
    def interaction():
        # First question succeeds on third attempt, second fails three times.
        inputs=['bad','0','1','bad','0','5','0','0','0']+['5']*8
        output=io.StringIO()
        with patch('builtins.input',side_effect=inputs),patch.object(professor.random,'randint',side_effect=[2,3]*10),contextlib.redirect_stdout(output):
            professor.main()
        assert output.getvalue().count('EEE')==5,output.getvalue()
        assert '2 + 3 = 5' in output.getvalue()
        assert 'Score: 9' in output.getvalue()
    check('professor retries, solution and score',interaction)
    data={'task':'phase1/task03','python':sys.executable,'passed':sum(r['passed'] for r in results),
          'total':len(results),'checks':results}
    args.report.parent.mkdir(parents=True,exist_ok=True)
    args.report.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f"{data['passed']}/{data['total']} passed")
    return int(data['passed']!=data['total'])


if __name__=='__main__':
    raise SystemExit(main())
