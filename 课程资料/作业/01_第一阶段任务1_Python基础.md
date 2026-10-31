# 第一阶段任务1：Python基础、函数与条件

## 一、需要配置的环境和工具

Windows 64 位；Python 3.13、pip；VS Code + Python 扩展或 PyCharm；Git 和 GitHub。

1. 打开 [Python Windows 下载页](https://www.python.org/downloads/windows/)，选择 Python 3.13 的 **Windows installer (64-bit)**。启动安装器，勾选 **Add Python to PATH**，点击 **Install Now**。完成后重新打开 Windows 命令提示符（CMD），依次运行：

   ```bat
   python --version
   python -m pip --version
   ```

   Python 版本应为 3.13；若 `python` 找不到，检查安装时的 PATH 选项并重新打开 CMD。详见 [Windows 安装说明](https://docs.python.org/3/using/windows.html)。
2. 编辑器任选其一：
   - [VS Code](https://code.visualstudio.com/download)：安装后打开，点击左侧扩展图标，搜索并安装 Microsoft 的 **Python** 扩展；选择 **File → Open Folder** 打开作业仓库；按 `Ctrl+Shift+P`，运行 **Python: Select Interpreter**，选择 Python 3.13。[图文教程](https://code.visualstudio.com/docs/python/python-tutorial)。
   - [PyCharm](https://www.jetbrains.com/pycharm/download/)：安装并启动，使用 **Open** 打开作业仓库；在 **Settings → Project → Python Interpreter** 添加或选择现有 Python 3.13。[解释器配置教程](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)。
3. 安装 [Git for Windows](https://gitforwindows.org/)，安装向导使用默认选项即可；重新打开 CMD，运行 `git --version`。在 [GitHub](https://github.com/) 注册账号并验证邮箱，按本页第三部分 Fork 培训方仓库并完成登录授权。[Git/GitHub 视频教程](https://www.bilibili.com/video/BV1s3411g7PS/)。
4. 在编辑器中新建 Python 文件，输入 `print("Hello, robot!")` 并保存；在该文件所在目录的 CMD 运行 `python 文件名.py`，确认显示文字。

## 二、最终任务与提交内容

### 需要学习的内容

- 认识解释器、编辑器、终端和工作目录，学会创建、保存和运行 `.py` 文件，阅读报错并定位出错行。
- 学习变量，字符串、整数、浮点数与布尔值，输入输出和类型转换；练习字符串替换、去除空白、大小写处理和格式化输出。
- 学习函数定义、参数、返回值、作用域与 `main()`；学习比较运算、逻辑运算、`if / elif / else`，练习正常输入和边界输入。
- 学习 Git 仓库、分支、暂存、提交和 PR，能在个人 Fork 查看自动评测。建立自学习惯：看一段、运行、修改输入、解释结果。可通过 [CS 自学指南](https://csdiy.wiki/) 查找计算机基础课程。

**学习资源：**[黑马程序员 Python](https://www.bilibili.com/video/BV1qW4y1a7fU/) 的变量、基本数据类型、输入输出、字符串、函数和判断；可选 [CS50P 第0讲](https://cs50.harvard.edu/python/0/)与[第1讲](https://cs50.harvard.edu/python/1/)。

**中英字幕视频：**[哈佛大学 CS50 Python 编程全集（附课程课件）](https://www.bilibili.com/video/BV1fFyJBFE92/?p=2)。打开视频后，在选集中选择“函数与变量、条件判断”相关内容。

**题目编号：**必做 [P01](../题库/01_Python基础与CS50P题.md#p01)、[P02](../题库/01_Python基础与CS50P题.md#p02)、[P03](../题库/01_Python基础与CS50P题.md#p03)、[P04](../题库/01_Python基础与CS50P题.md#p04)。点击编号查看集中题面、接口和验收要求。

完成四题，分别提交 `faces/faces.py`、`tip/tip.py`、`bank/bank.py`、`meal/meal.py`。按题库保留函数接口、输入输出与边界处理。

在 `phase1/task01/REPORT.md` 记录运行命令、正常／边界输入及一次排错；在仓库根目录 `ENVIRONMENT.md` 记录 Python、pip、编辑器及 Git 信息。在个人 Fork 查看自动检查，并向培训方仓库提交 PR。

### 提交内容与检查

- 在个人 Fork 的本任务分支提交 `phase1/task01/faces/faces.py`、`tip/tip.py`、`bank/bank.py`、`meal/meal.py`；后三个路径同样位于 `phase1/task01/` 下。
- 提交 `phase1/task01/REPORT.md` 和仓库根目录 `ENVIRONMENT.md`。创建 PR 前填写运行与自查记录；个人 Fork 的 Actions 出现评测结果后，将结果补充到报告并再次推送。
- 在个人 Fork 的 Actions 查看四题自动检查结果，保留失败信息并修正。

## 三、提交至作业仓库

培训方公开仓库：[https://github.com/o-1717986918/robot-ai-training-homework](https://github.com/o-1717986918/robot-ai-training-homework)。学员将仓库 Fork 到自己的 GitHub 账号，在自己的 Fork 中推送分支，再向培训方仓库创建 PR；无需培训方邀请或仓库写入权限。`GITHUB_USERNAME` 是占位符，请在下方所有命令和地址中替换为自己的 GitHub 用户名。仓库、Fork、分支及 PR 均公开。

1. 注册或登录 GitHub，打开培训方仓库，点击右上角 **Fork → Create a new fork**；Owner 选自己的账号，保留默认仓库名 `robot-ai-training-homework`，点击 **Create fork**。记下浏览器显示的个人 Fork 地址 `https://github.com/你的用户名/robot-ai-training-homework`。

2. 在个人 Fork 页面打开 **Actions**，若出现启用提示，点击 **I understand my workflows, go ahead and enable them**；确认 `Phase1 automatic feedback` 已启用。以后在个人 Fork 的 Actions 查看推送触发的结果。

3. 打开 Windows CMD，把以下地址和分支里的 `GITHUB_USERNAME` 换成自己的 GitHub 用户名，姓名和邮箱换成自己的。`C:\robot-ai\course` 应为尚未存在的目录；若已存在，改用新的目录，并在后续命令中相应调整。

```bat
mkdir C:\robot-ai
cd /d C:\robot-ai
git clone https://github.com/GITHUB_USERNAME/robot-ai-training-homework.git course
cd /d C:\robot-ai\course
git config user.name "你的姓名或代号"
git config user.email "你的GitHub邮箱"
git remote add upstream https://github.com/o-1717986918/robot-ai-training-homework.git
git remote -v
git switch -c student/GITHUB_USERNAME/phase1-task01 origin/main
```

确认 `origin` 为自己的 Fork，`upstream` 为培训方仓库。首次推送时按弹出的浏览器提示登录 GitHub 并授权 Git Credential Manager；如未出现登录窗口，参考 [GitHub HTTPS 认证](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)。

4. 完成本项内容，在仓库根目录执行，确认 `git status` 后推送：

```bat
cd /d C:\robot-ai\course
git add -- phase1/task01 ENVIRONMENT.md
git status
git commit -m "Complete phase1-task01"
git push -u origin student/GITHUB_USERNAME/phase1-task01
```

5. 打开**培训方仓库**的 **Pull requests → New pull request → compare across forks**：选择 `base repository: o-1717986918/robot-ai-training-homework`、`base: main`、`head repository: GITHUB_USERNAME/robot-ai-training-homework`、`compare: student/GITHUB_USERNAME/phase1-task01`，填写任务名称、运行方法与结果，点击 **Create pull request**。在个人 Fork 的 **Actions → Phase1 automatic feedback** 找到本次分支的 push 运行，查看逐题结果与 Artifacts，把运行链接贴入培训方 PR。分支继承此前成果时，PR 检查可能同时包含先前任务。检查失败时修改文件后再次 `git add`、`git commit`、`git push`，PR 更新且 Fork 重新评测。培训方 PR 的 Actions 受 GitHub 外部贡献者审批策略影响，可能显示等待批准；个人 Fork 的 push 评测可供自查。

6. 保留 PR 和已推送分支，下一任务从本分支继续。将大量数据、模型或视频放在培训方可访问的存储位置，在 README 提供链接与 SHA-256；少量结果放任务目录的 `samples/`。不要提交密钥、虚拟环境和完整数据集。
