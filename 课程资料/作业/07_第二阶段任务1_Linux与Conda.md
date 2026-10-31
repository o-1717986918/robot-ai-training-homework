# 第二阶段任务1：Linux 与 Conda 开发环境

## 一、需要配置的环境和工具

选择 WSL2、虚拟机或双系统运行 **Ubuntu 24.04**；后续任务在 Linux 中开发。

**WSL2 推荐路线：**在 Windows 开始菜单搜索 PowerShell，右键 **以管理员身份运行**，执行：

```powershell
wsl --install -d Ubuntu-24.04
```

按提示重启，打开开始菜单中的 Ubuntu 24.04，首次启动设置 Linux 用户名和密码；密码输入时不显示字符。管理员 PowerShell 运行 `wsl -l -v`，确认发行版为版本 2。[WSL 中文安装教程](https://learn.microsoft.com/zh-cn/windows/wsl/install)。虚拟机可参考 [Ubuntu 虚拟机教程](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox)，双系统可参考 [Ubuntu 安装教程](https://ubuntu.com/tutorials/install-ubuntu-desktop)。

**Linux Miniconda：**在 Ubuntu 终端按 [Miniconda 官方 Linux 安装教程](https://www.anaconda.com/docs/getting-started/miniconda/install/linux-install) 下载 Linux 安装脚本并运行；安装时按提示同意条款、选择个人目录并初始化 shell，关闭终端后重新打开。x86-64 电脑可执行以下命令开始安装：

```bash
cd ~
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

然后执行：

```bash
conda --version
conda create -n robot-ai-basics python=3.11 -y
conda create -n robot-ai-vision python=3.11 -y
conda activate robot-ai-basics
python -c "import sys; print(sys.version); print(sys.executable)"
conda activate robot-ai-vision
python -c "import sys; print(sys.version); print(sys.executable)"
sudo apt update
sudo apt install -y git openssh-client openssh-server ripgrep tmux
git --version
rg --version
tmux -V
```

如果 `conda` 不存在，确认安装时执行了 shell 初始化，重新打开 Ubuntu 终端；仍失败按官方教程执行初始化。创建环境若提示 Anaconda 软件源使用条款，阅读并按提示选择是否接受，再重新执行创建命令。VS Code 安装 [WSL 扩展](https://code.visualstudio.com/docs/remote/wsl)，在 Ubuntu 的仓库目录运行 `code .`，选择 Linux 中的 Conda 解释器；PyCharm 用户参考 [WSL 解释器设置](https://www.jetbrains.com/help/pycharm/using-wsl-as-a-remote-interpreter.html)。

SSH 本机练习：在 Ubuntu 执行 `sudo service ssh start`，再运行 `ssh localhost`，首次确认主机指纹后输入 Linux 用户密码；退出连接输入 `exit`。Git 首次从 Linux 克隆和认证见本页第三部分。`tmux` 输入 `tmux new -s practice`，按 `Ctrl+B` 后按 `D` 分离，再输入 `tmux attach -t practice` 恢复。

## 二、最终任务与提交内容

### 需要学习的内容

- 选择 WSL2、虚拟机或双系统安装 Ubuntu，认识 Linux 用户、终端、工作目录、绝对路径和相对路径。
- 学习 `pwd`、`ls`、`cd`、`mkdir`、`cp`、`mv`、`rm`、`cat`、`chmod`，以及管道、进程、磁盘、`apt` 与 `rg` 搜索；练习 SSH 本机连接和 `tmux` 会话分离、恢复。
- 学习 Conda 环境创建、激活和切换，区分系统 Python、Conda 解释器及各自安装的包；在编辑器选择 Linux 解释器并运行此前程序。
- 学习在 Linux 克隆培训方仓库、认证、切换自己的任务分支并提交；第二阶段可使用 Agent 辅助，逐项验证运行结果。

**学习资源：**[计算机教育中缺失的一课](https://missing.csail.mit.edu/) 的 Shell、工具、版本控制和调试章节；[WSL 中文开发环境教程](https://learn.microsoft.com/zh-cn/windows/wsl/setup/environment)。

第二阶段可以使用 Agent 辅助；提交前自行运行、检查并解释代码。

### 必做：Linux 与 Conda 开发环境

**提交位置：** `phase2/task01/`；更新根目录 `ENVIRONMENT.md`。

#### 题目描述

从 WSL2、虚拟机或双系统中选一种安装 Ubuntu 24.04，在 Linux 中配置编辑器、Git、SSH、Miniconda，以及 Python 3.11 的 `robot-ai-basics` 和 `robot-ai-vision` 两个 Conda 环境。

#### 运行与验收

1. 在 Linux 终端演示目录创建、查看、复制、移动、权限修改，能查看进程、磁盘及搜索文件或代码。
2. 激活两个 Conda 环境，记录 `python --version` 与 `sys.executable`；编辑器选用 Linux 中相应解释器，运行第一阶段已有 Python／图片程序并记录输出。
3. 演示 Git 认证与提交、SSH 本机连接、`rg` 搜索，以及 `tmux` 会话分离和恢复。记录系统版本、安装方式、解释器路径、关键工具版本和操作结果。

#### 交付

在 `phase2/task01/README.md` 给出环境、运行命令和演示记录，并更新根目录环境摘要。记录去除账号密钥与密码；提交对应 PR。

### 提交内容与检查

- 在培训方仓库的本任务分支提交 `phase2/task01/README.md` 和更新后的根目录 `ENVIRONMENT.md`，记录 Ubuntu 安装方式、两个 Conda 解释器路径、工具版本、命令与实际输出。
- 报告覆盖基本文件操作、此前程序运行、SSH 本机连接、`rg` 搜索及 `tmux` 会话恢复；在培训方仓库 PR 中填写环境和操作结果。

## 三、提交至作业仓库

培训方仓库：[https://github.com/o-1717986918/robot-ai-training-homework](https://github.com/o-1717986918/robot-ai-training-homework)。培训方为每位学员开通该仓库的写入权限。本文的 `GITHUB_USERNAME` 是占位符：请在每条命令中替换为自己的 GitHub 用户名，例如 `student/robotlee/phase1-task01`。每位学员使用自己的分支；提交的 PR 保留在培训方仓库，**不合并到培训方 main**。其他有仓库访问权限的学员可能看到分支和 PR。

1. 在 Ubuntu 终端首次克隆培训方仓库。下方地址为培训方仓库，将姓名、邮箱和 `GITHUB_USERNAME` 换成自己的：

```bash
mkdir -p ~/robot-ai
cd ~/robot-ai
git clone https://github.com/o-1717986918/robot-ai-training-homework.git course
cd ~/robot-ai/course
git config user.name "你的姓名或代号"
git config user.email "你的GitHub邮箱"
git fetch origin
git switch -c student/GITHUB_USERNAME/phase2-task01 origin/student/GITHUB_USERNAME/phase1-assessment
```

若 `~/robot-ai/course` 已是该仓库，进入该目录后从 `git fetch origin` 开始。`origin/student/GITHUB_USERNAME/phase1-assessment` 是此前推送到培训方仓库的考核分支。HTTPS 要求密码时使用具备该仓库 Contents 读写权限的 [GitHub personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)，不要把令牌写进命令或提交到仓库。

2. 完成本项内容，在仓库根目录执行，确认 `git status` 后推送：

```bash
cd ~/robot-ai/course
git add -- phase2/task01 ENVIRONMENT.md
git status
git commit -m "Complete phase2-task01"
git push -u origin student/GITHUB_USERNAME/phase2-task01
```

3. 打开**培训方仓库**的 **Pull requests → New pull request**：选择 `base: main` 和 `compare: student/GITHUB_USERNAME/phase2-task01`，填写任务名称、运行方法与结果，点击 **Create pull request**。按任务要求运行项目，检查输出并在 PR 中记录实际结果。

4. 保留 PR 和已推送分支，下一任务从本分支继续。将大量数据、模型或视频放在培训方可访问的存储位置，在 README 提供链接与 SHA-256；少量结果放任务目录的 `samples/`。不要提交密钥、虚拟环境和完整数据集。
