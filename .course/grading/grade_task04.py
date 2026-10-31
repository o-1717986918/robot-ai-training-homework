"""Association image/OOP checks with generated, non-game input fixtures."""
import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import cv2
import numpy as np


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--root',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    source=args.root.resolve()
    out=args.output.resolve()
    assert not out.exists(), 'Use a fresh output directory so repeat-run checks have a known starting point.'
    inputs=out/'输入图片'
    (inputs/'nested').mkdir(parents=True)
    def save(path,image):
        cv2.imencode(path.suffix.lower(),image)[1].tofile(path)
    save(inputs/'彩色.png',np.full((240,320,3),210,np.uint8))
    save(inputs/'wide.JPG',np.full((200,640,3),(160,180,220),np.uint8))
    save(inputs/'nested/square.PNG',np.full((100,100,3),(50,90,130),np.uint8))
    (inputs/'broken.png').write_text('not an image',encoding='utf-8')
    (inputs/'readme.txt').write_text('ignore this file',encoding='utf-8')
    logo=np.full((20,40,4),(0,0,255,128),np.uint8)
    save(out/'logo.png',logo)
    save(out/'background.png',np.full((450,800,3),245,np.uint8))
    original_hashes={p.relative_to(inputs).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs.rglob('*') if p.is_file()}
    commands=[]
    checks=[]
    def run(filename,*argv,stdin=None,expected=0):
        command=[sys.executable,str(source/filename),*map(str,argv)]
        p=subprocess.run(command,input=stdin,text=True,capture_output=True,encoding='utf-8',timeout=45)
        commands.append({'argv':command,'stdin':stdin,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
        assert p.returncode==expected,(filename,p.returncode,p.stdout,p.stderr)
        return p.stdout
    def record(name,callback):
        try:
            callback()
            entry={'name':name,'passed':True}
        except Exception as exc:
            entry={'name':name,'passed':False,'error':str(exc)}
        checks.append(entry)
        print(('PASS ' if entry['passed'] else 'FAIL ')+name)
    def assert_equal(actual,expected):
        assert actual==expected,(actual,expected)
    def rows(path):
        with path.open(newline='',encoding='utf-8-sig') as f:
            return list(csv.DictReader(f))
    record('catalog continues after bad file',lambda:assert_equal(json.loads(run('catalog.py',inputs,out/'metadata.csv')),{'success':3,'failed':1}))
    record('catalog includes upper-case and nested paths',lambda:assert_equal({r['relative_path'] for r in rows(out/'metadata.csv')},{'彩色.png','wide.JPG','nested/square.PNG'}))
    record('catalog records dimensions',lambda:assert_equal(sorted((int(r['width']),int(r['height'])) for r in rows(out/'metadata.csv')),[(100,100),(320,240),(640,200)]))
    record('catalog missing directory fails clearly',lambda:run('catalog.py',out/'missing',out/'missing.csv',expected=2))
    (out/'empty').mkdir()
    record('catalog empty directory is valid',lambda:assert_equal(json.loads(run('catalog.py',out/'empty',out/'empty.csv')),{'success':0,'failed':0}))
    def resize_first():
        result=json.loads(run('resize_images.py',inputs,out/'resized','--max-edge',160))
        assert (result['success'],result['skipped'],result['failed'])==(3,0,1),result
    record('resize first run and bad file',resize_first)
    def resize_again():
        result=json.loads(run('resize_images.py',inputs,out/'resized','--max-edge',160))
        assert (result['success'],result['skipped'],result['failed'])==(0,3,1),result
    record('resize repeat run skips existing',resize_again)
    def dimensions():
        for rel,w,h in [('彩色.png',160,120),('wide.JPG',160,50),('nested/square.PNG',100,100)]:
            image=cv2.imdecode(np.fromfile(out/'resized'/rel,dtype=np.uint8),cv2.IMREAD_COLOR)
            assert image.shape[:2]==(h,w),image.shape
    record('resize preserves aspect ratio and small image size',dimensions)
    record('resize rejects original directory',lambda:run('resize_images.py',inputs,inputs,expected=2))
    record('resize rejects nested output directory',lambda:run('resize_images.py',inputs,inputs/'output',expected=2))
    manifest=out/'groups.csv'
    manifest_rows=[
        {'image_id':'one','relative_path':'彩色.png','group':'train'},
        {'image_id':'two','relative_path':'wide.JPG','group':'val'},
        {'image_id':'one','relative_path':'nested/square.PNG','group':'train'},
        {'image_id':'three','relative_path':'missing.png','group':'test'},
        {'image_id':'four','relative_path':'彩色.png','group':'../escape'},
        {'image_id':'five','relative_path':'broken.png','group':'test'},
        {'image_id':'six','relative_path':'../background.png','group':'test'},
    ]
    with manifest.open('w',newline='',encoding='utf-8-sig') as f:
        writer=csv.DictWriter(f,fieldnames=['image_id','relative_path','group'])
        writer.writeheader()
        writer.writerows(manifest_rows)
    def organize():
        result=json.loads(run('organize_images.py',inputs,manifest,out/'groups'))
        assert (result['success'],result['failed'])==(2,5),result
        assert len(rows(out/'groups/clean.csv'))==2
        assert len(rows(out/'groups/errors.csv'))==5
    record('organize valid records and five invalid cases',organize)
    record('organize preserves supplied labels',lambda:assert_equal(sorted(r['relative_path'] for r in rows(out/'groups/clean.csv')),['train/one.png','val/two.jpg']))
    def organize_repeat():
        before=hashlib.sha256((out/'groups/train/one.png').read_bytes()).hexdigest()
        result=json.loads(run('organize_images.py',inputs,manifest,out/'groups'))
        assert (result['success'],result['failed'])==(0,7),result
        assert before==hashlib.sha256((out/'groups/train/one.png').read_bytes()).hexdigest()
    record('organize repeat run rejects overwrites',organize_repeat)
    for name in ['彩色.png','wide.JPG']:
        record('overlay '+name,lambda n=name:run('overlay.py',inputs/n,out/'logo.png',out/('overlay-'+Path(n).stem+'.png'),'--width',40))
    def alpha():
        image=cv2.imdecode(np.fromfile(out/'overlay-彩色.png',dtype=np.uint8),cv2.IMREAD_COLOR)
        assert np.allclose(image[15,15],np.array([105,105,233],dtype=np.uint8),atol=1),image[15,15]
        assert np.array_equal(image[0,0],np.array([210,210,210],dtype=np.uint8))
    record('overlay checks alpha blending and untouched pixels',alpha)
    record('overlay rejects out-of-bounds',lambda:run('overlay.py',inputs/'彩色.png',out/'logo.png',out/'invalid.png','--x',10000,expected=2))
    for name in ['Ada','Lin']:
        record('certificate '+name,lambda n=name:run('certificate.py',out/'background.png',n,out/('certificate-'+n+'.png')))
    record('certificate changes with object parameter',lambda:assert_equal((out/'certificate-Ada.png').read_bytes()==(out/'certificate-Lin.png').read_bytes(),False))
    record('seasons rejects invalid date',lambda:run('seasons/seasons.py',stdin='2021-02-29\n',expected=1))
    record('seasons accepts valid birthday',lambda:assert_equal('minutes' in run('seasons/seasons.py',stdin='2000-01-01\n'),True))
    def jar_behaviour():
        snippet = """from jar import Jar
j = Jar(3)
assert j.capacity == 3 and j.size == 0
j.deposit(2)
assert j.size == 2 and str(j) == '🍪🍪'
j.withdraw(1)
assert j.size == 1
try:
    j.deposit(10)
except ValueError:
    pass
else:
    raise AssertionError('overflow should raise ValueError')
assert j.size == 1
try:
    j.withdraw(10)
except ValueError:
    pass
else:
    raise AssertionError('underflow should raise ValueError')
assert j.size == 1
try:
    j.capacity = 20
except AttributeError:
    pass
else:
    raise AssertionError('capacity is read-only')
"""
        result=subprocess.run([sys.executable,'-c',snippet],cwd=source/'jar',capture_output=True,text=True,encoding='utf-8',timeout=15,env={**os.environ,'PYTHONIOENCODING':'utf-8'})
        assert result.returncode==0,result.stdout+result.stderr
    record('Jar public behaviour without student test files',jar_behaviour)
    after={p.relative_to(inputs).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs.rglob('*') if p.is_file()}
    record('all original inputs retain their hashes',lambda:assert_equal(after,original_hashes))

    def organize_groups():
        extra_manifest=out/'extra-groups.csv'
        data=[
            {'image_id':'one','relative_path':'彩色.png','group':'unknown'},
            {'image_id':'ONE','relative_path':'wide.JPG','group':'train'},
            {'image_id':'valid','relative_path':'彩色.png','group':'test'},
        ]
        with extra_manifest.open('w',newline='',encoding='utf-8-sig') as f:
            writer=csv.DictWriter(f,fieldnames=['image_id','relative_path','group'])
            writer.writeheader()
            writer.writerows(data)
        result=json.loads(run('organize_images.py',inputs,extra_manifest,out/'extra-groups'))
        assert (result['success'],result['failed'])==(1,2),result
        assert [r['image_id'] for r in rows(out/'extra-groups/clean.csv')]==['valid']
    record('organize rejects unknown group and case-insensitive duplicate IDs',organize_groups)

    report={'task':'phase1/task04','python':sys.executable,'passed':sum(c['passed'] for c in checks),
            'total':len(checks),'checks':checks,'commands':commands,'original_hashes':original_hashes,
            'fixtures':'procedurally generated non-game images; tests do not prove robustness on arbitrary photographs'}
    (out/'results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f"{report['passed']}/{report['total']} passed")
    return int(report['passed']!=report['total'])


if __name__=='__main__':
    raise SystemExit(main())
