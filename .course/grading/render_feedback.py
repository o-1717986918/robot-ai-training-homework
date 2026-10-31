"""Readable check50 results and expected/actual differences in GitHub's job summary."""
from pathlib import Path
import argparse,html,json,os


def safe(value,limit=1500):
    return html.escape(str(value)[:limit]).replace("|","&#124;")


def render(root,task,student_root):
    lines=[f"# {task} · 逐题反馈","",
           "前13道原版题直接使用固定提交的官方check50；Seasons/Jar保留官方程序与类行为检查，移除学生测试文件要求（详见adaptation.json）；改编图片题使用课程行为检查。","",
           "| 题目 | 官方检查 | 结果 |","|---|---:|---|"]
    summary=root/f"check50-{task}/summary.json"
    if summary.exists():
        data=json.loads(summary.read_text(encoding="utf-8"))
        for item in data["exercises"]:
            path=student_root/item["student_path"]/(Path(item["student_path"]).name+".py")
            state="通过" if item["passed"] else "缺交" if not path.is_file() else "未通过"
            label=item['checks_path']+("（行为子集）" if "subset" in item.get("checks_mode","") else "")
            lines.append(f"| {safe(label)} | {item.get('passed_checks',0)}/{item.get('total_checks','?')} | {state} |")
        lines+=["",f"官方检查提交：`{safe(data['upstream_commit'])}`；check50 {safe(data['check50'])}。",""]
        for item in data["exercises"]:
            if item["passed"]:continue
            lines+=["## "+safe(item["checks_path"]),"",f"代码目录：`{safe(item['student_path'])}`。",""]
            if item.get("error"):lines+=[safe(item["error"]),""]
            raw=root/f"check50-{task}"/(item["checks_path"].replace("/","_")+".stdout.txt")
            if raw.exists():
                try:details=json.loads(raw.read_text(encoding="utf-8"))["results"]
                except (ValueError,KeyError):details=[]
                for check in details:
                    if check["passed"] is True:continue
                    status="跳过（前置检查失败）" if check["passed"] is None else "失败"
                    lines+=["### "+safe(check.get("description",check["name"]))+" · "+status,""]
                    cause=check.get("cause") or {}
                    if cause.get("rationale"):lines+=[safe(cause["rationale"]),""]
                    if "expected" in cause:lines+=["期望：","<pre>"+safe(cause["expected"])+"</pre>",""]
                    if "actual" in cause:lines+=["实际：","<pre>"+safe(cause["actual"])+"</pre>",""]
                    if cause.get("help"):lines+=["提示："+safe(cause["help"]),""]
    else:
        lines+=["| 尚无官方结果 | — | 先查看安装/拉取步骤 |",""]
    local=root/(task+"-local.json")
    if task=="task04":local=root/"task04-images/results.json"
    if local.exists():
        data=json.loads(local.read_text(encoding="utf-8"))
        checks=data.get("checks",data.get("results",[]))
        lines+=["## 课程补充检查","",
                "| 检查 | 结果 | 说明 |","|---|---|---|"]
        for check in checks:
            error=safe(check.get("error","")).replace("\r","").replace("\n","<br>")
            lines.append("| "+safe(check["name"])+" | "+("通过" if check["passed"] else "失败")+" | "+error+" |")
    lines+=["","完整原始结果在本次运行的Artifacts中；修正代码后commit/push，同一个PR会更新。",
            "评测基于实际提交代码。公开的仓库反馈不能替代培训方对固定提交版本的最终复核。",""]
    return "\n".join(lines)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--root",type=Path,default=Path("artifacts"))
    parser.add_argument("--task",required=True)
    parser.add_argument("--student-root",type=Path,default=Path("."))
    parser.add_argument("--output",type=Path,default=Path("artifacts/feedback.md"))
    args=parser.parse_args()
    result=render(args.root,args.task,args.student_root)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(result,encoding="utf-8")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"],"a",encoding="utf-8") as f:f.write(result)
    print(result)

if __name__=="__main__":main()
