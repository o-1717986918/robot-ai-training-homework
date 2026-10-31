"""Select changed course task directories, independent of a student's branch name."""
from pathlib import Path
import argparse,json,os,re,subprocess

TASKS=["task01","task02","task03","task04"]

def select(changed,requested=""):
    if requested:
        if requested=="all":return TASKS
        if requested not in TASKS:raise ValueError("Unknown task")
        return [requested]
    if any(p.startswith((".course/grading/",".github/workflows/")) for p in changed):
        return TASKS
    return sorted({match.group(1) for p in changed
                   if (match:=re.match(r"^phase1/(task0[1-4])/",p))})


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--event",type=Path,default=Path(os.environ.get("GITHUB_EVENT_PATH","event.json")))
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    event=json.loads(args.event.read_text(encoding="utf-8"))
    requested=os.environ.get("REQUESTED_TASK","")
    base=event.get("pull_request",{}).get("base",{}).get("sha") or event.get("before","")
    if not base or set(base)=={"0"}:
        for fallback in ["origin/main","HEAD^"]:
            probe=subprocess.run(["git","rev-parse","--verify",fallback],capture_output=True,text=True)
            if probe.returncode==0:
                base=probe.stdout.strip();break
    if base:
        proc=subprocess.run(["git","diff","--name-only",base,"HEAD"],capture_output=True,text=True,encoding="utf-8")
        if proc.returncode:raise RuntimeError(proc.stderr)
        changed=proc.stdout.splitlines()
    else:
        changed=subprocess.check_output(["git","ls-files"],text=True,encoding="utf-8").splitlines()
    tasks=select(changed,requested)
    result="tasks="+json.dumps(tasks)+"\n"
    if args.output:
        with args.output.open("a",encoding="utf-8") as f:f.write(result)
    print(result,end="")

if __name__=="__main__":main()
