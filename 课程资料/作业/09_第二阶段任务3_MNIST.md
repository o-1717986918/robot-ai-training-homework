# 第二阶段任务3：MNIST 手写数字识别

## 一、需要配置的环境和工具

Ubuntu、`robot-ai-vision`、Python 3.11、PyTorch、torchvision 和 Matplotlib。在 Ubuntu 终端先执行 `conda activate robot-ai-vision`。

CPU 路线：运行 `python -m pip install torch torchvision matplotlib`。NVIDIA GPU 路线：先运行 `nvidia-smi` 查看显卡与驱动，再打开 [PyTorch 安装选择器](https://pytorch.org/get-started/locally/) 选择 Linux、Pip、Python 及驱动支持的 CUDA 构建，复制页面生成的安装命令；随后运行 `python -m pip install matplotlib`。

运行 `python -c "import torch, torchvision; print(torch.__version__, torch.cuda.is_available())"` 验证；输出 `False` 时可继续使用 CPU。MNIST 使用 torchvision 下载官方数据，或使用培训方核验的副本。

## 二、最终任务与提交内容

### 需要学习的内容

- 学习张量、形状、数据类型、CPU/GPU 设备，以及 Dataset、DataLoader 和 MNIST 数据读取。
- 认识卷积、池化、分类输出、损失函数和优化器；理解前向计算、反向传播、参数更新与训练循环。
- 区分训练集、验证集和测试集，学习验证集选模、保存与加载权重、绘制 loss/accuracy 曲线和分析错误样例。
- 先用少量数据完成训练与预测，再按任务要求运行完整流程；NVIDIA 用户检查驱动与 PyTorch CUDA 可用性。

**学习资源：**[小土堆 PyTorch 教程](https://www.bilibili.com/video/BV1hE411t7RN/) 的张量、数据加载、卷积、损失、优化和训练保存章节；[PyTorch 入门](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)。

第二阶段可以使用 Agent 辅助；提交前自行运行、检查并解释代码。

### 必做：MNIST 手写数字识别

**提交位置：** `phase2/task03/`。

#### 输入与目标

使用 MNIST 的 28×28 灰度数字图片与标签，用 PyTorch 建立小型 CNN、训练并预测 0—9。将官方训练集以固定随机种子划分为 54,000 条训练与 6,000 条验证；官方 10,000 条测试数据用于最终独立评估。CPU 可完成基本流程，NVIDIA 设备可使用匹配驱动的 CUDA 构建。

#### 输出与约束

记录每轮训练、验证的 loss 和 accuracy，绘制曲线；使用验证集选择模型，保存并重新加载最佳权重，在独立测试集报告样本数与准确率，展示至少一组重新加载后的预测和错误样例。至少比较一次小改动，例如学习率或轮数；记录随机种子、数据划分、设备与依赖。先完成小数据短流程，再进行完整数据训练。

#### 交付与验收

提交训练与独立预测代码、少量曲线／结果图、日志摘要和 README；说明从仓库根目录启动训练、选择设备及加载权重预测的命令。数据和权重通过可访问链接提供，并附 SHA-256；样本数和达标阈值以培训方发布为准。

### 提交内容与检查

- 在培训方仓库的本任务分支提交 `phase2/task03/` 下的训练和预测程序、依赖、README、日志摘要及少量曲线、预测和错误样例。
- README 记录数据划分、随机种子、设备、训练和加载权重的命令、验证与测试结果，以及一次参数改动对比；数据和权重通过培训方可访问的链接提供并记录 SHA-256。
- 在培训方仓库 PR 中填写训练环境与最终测试结果。

## 三、提交至作业仓库

培训方仓库：[https://github.com/o-1717986918/robot-ai-training-homework](https://github.com/o-1717986918/robot-ai-training-homework)。培训方为每位学员开通该仓库的写入权限。本文的 `GITHUB_USERNAME` 是占位符：请在每条命令中替换为自己的 GitHub 用户名，例如 `student/robotlee/phase1-task01`。每位学员使用自己的分支；提交的 PR 保留在培训方仓库，**不合并到培训方 main**。其他有仓库访问权限的学员可能看到分支和 PR。

1. 打开Ubuntu 终端，在仓库目录从自己上一任务已推送的分支创建本任务分支：

```bash
cd ~/robot-ai/course
git status
git fetch origin
git switch -c student/GITHUB_USERNAME/phase2-task03 origin/student/GITHUB_USERNAME/phase2-task02
```

如果当前有需要保留的未提交修改，先完成提交。若本任务分支已在本机创建，将最后一条命令替换为 `git switch student/GITHUB_USERNAME/phase2-task03`。

2. 完成本项内容，在仓库根目录执行，确认 `git status` 后推送：

```bash
cd ~/robot-ai/course
git add -- phase2/task03
git status
git commit -m "Complete phase2-task03"
git push -u origin student/GITHUB_USERNAME/phase2-task03
```

3. 打开**培训方仓库**的 **Pull requests → New pull request**：选择 `base: main` 和 `compare: student/GITHUB_USERNAME/phase2-task03`，填写任务名称、运行方法与结果，点击 **Create pull request**。按任务要求运行项目，检查输出并在 PR 中记录实际结果。

4. 保留 PR 和已推送分支，下一任务从本分支继续。将大量数据、模型或视频放在培训方可访问的存储位置，在 README 提供链接与 SHA-256；少量结果放任务目录的 `samples/`。不要提交密钥、虚拟环境和完整数据集。
