# 第一阶段任务5：算法入门与 Agent

## 一、需要配置的环境和工具

沿用 Windows Python 3.13、编辑器和 Git。打开 [洛谷](https://www.luogu.com.cn/) 注册并登录；在题目页面点击提交，选择 Python 语言，粘贴代码并查看评测详情。

配置一种 Agent，练习读取当前作业并解释错误：

- **DeepSeek Harness：**打开 [官方下载页](https://www.deepseek.com/download/)，在 Harness 桌面端选择 Windows，运行安装包。前往 [DeepSeek 开放平台](https://platform.deepseek.com/) 注册并创建 API Key；在客户端模型设置中填写密钥，按平台当前模型列表选择模型，选择 `C:\robot-ai\course` 作为工作区，再请求解释一份自己写的代码。[官方入门教程](https://deepseek-harness.github.io/deepseek-harness/guide/quickstart)。
- **ZCode：**按 [中文安装教程](https://zcode.z.ai/cn/docs/install) 安装并打开 Windows 版；在模型设置中连接账号或按 [连接模型教程](https://zcode.z.ai/cn/docs/configuration) 配置 API，打开课程仓库作为工作区。也可按软件的 OpenAI 兼容提供商设置接入 DeepSeek，地址和模型 ID 以 [DeepSeek API 文档](https://api-docs.deepseek.com/) 为准。

密钥放在客户端的密钥设置或本地环境变量，不提交到作业仓库。查看生成的修改并自行运行验证。

## 二、最终任务与提交内容

### 需要学习的内容

- 按分支模拟、枚举与计数、排序去重、字符串匹配、二维网格的顺序学习算法；理解循环次数、边界和基本时间复杂度。
- 学习队列与 BFS，练习网格上下左右扩展、访问标记和越界处理；先手算小样例，再编程验证。
- 理解洛谷标准输入输出与评测结果；配置一种 Agent，练习描述目标、已有代码和错误，核对建议并独立运行。

**学习资源：**[OI Wiki 枚举](https://oi-wiki.org/basic/enumerate/)、[模拟](https://oi-wiki.org/basic/simulate/)和[BFS](https://oi-wiki.org/search/bfs/)；Python 队列可查 [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)。

完成以下八道洛谷题；逐题阅读题面，使用 Python 按标准输入输出提交，并将代码保存为 `phase1/task05/洛谷题号.py`：

- [P1422 电费](https://www.luogu.com.cn/problem/P1422)
- [P1046 摘苹果](https://www.luogu.com.cn/problem/P1046)
- [P1427 数字游戏](https://www.luogu.com.cn/problem/P1427)
- [P1059 随机数](https://www.luogu.com.cn/problem/P1059)
- [P1554 梦中的统计](https://www.luogu.com.cn/problem/P1554)
- [P1308 统计单词数](https://www.luogu.com.cn/problem/P1308)
- [P2670 扫雷](https://www.luogu.com.cn/problem/P2670)
- [P1162 填涂颜色](https://www.luogu.com.cn/problem/P1162)

提交八题 Python 文件及 `phase1/task05/REPORT.md`，列出每题 OJ 评测链接与状态，并解释一道网格／搜索题的思路。在根目录 `ENVIRONMENT.md` 记录所用 Agent、模型和一次辅助使用情况。

### 提交内容与检查

- 将八道题分别提交到洛谷评测，并在个人 Fork 的本任务分支提交八个同题号 Python 文件，例如 `phase1/task05/P1422.py`。
- 提交 `phase1/task05/REPORT.md`，记录八个洛谷评测结果与链接、一道网格或搜索题的思路；提交更新后的根目录 `ENVIRONMENT.md`，记录 Agent 工具、模型和使用情况。
- 在培训方仓库 PR 中填写洛谷结果和运行方式。

## 三、提交至作业仓库

培训方公开仓库：[https://github.com/o-1717986918/robot-ai-training-homework](https://github.com/o-1717986918/robot-ai-training-homework)。学员将仓库 Fork 到自己的 GitHub 账号，在自己的 Fork 中推送分支，再向培训方仓库创建 PR；无需培训方邀请或仓库写入权限。`GITHUB_USERNAME` 是占位符，请在下方所有命令和地址中替换为自己的 GitHub 用户名。仓库、Fork、分支及 PR 均公开。

1. 打开Windows CMD，在仓库目录从自己上一任务已推送的分支创建本任务分支：

```bat
cd /d C:\robot-ai\course
git status
git fetch origin
git switch -c student/GITHUB_USERNAME/phase1-task05 origin/student/GITHUB_USERNAME/phase1-task04
```

如果当前有需要保留的未提交修改，先完成提交。若本任务分支已在本机创建，将最后一条命令替换为 `git switch student/GITHUB_USERNAME/phase1-task05`。

2. 完成本项内容，在仓库根目录执行，确认 `git status` 后推送：

```bat
cd /d C:\robot-ai\course
git add -- phase1/task05 ENVIRONMENT.md
git status
git commit -m "Complete phase1-task05"
git push -u origin student/GITHUB_USERNAME/phase1-task05
```

3. 打开**培训方仓库**的 **Pull requests → New pull request → compare across forks**：选择 `base repository: o-1717986918/robot-ai-training-homework`、`base: main`、`head repository: GITHUB_USERNAME/robot-ai-training-homework`、`compare: student/GITHUB_USERNAME/phase1-task05`，填写任务名称、运行方法与结果，点击 **Create pull request**。在洛谷查看八题评测状态，PR 中列出对应链接。

4. 保留 PR 和已推送分支，下一任务从本分支继续。将大量数据、模型或视频放在培训方可访问的存储位置，在 README 提供链接与 SHA-256；少量结果放任务目录的 `samples/`。不要提交密钥、虚拟环境和完整数据集。
