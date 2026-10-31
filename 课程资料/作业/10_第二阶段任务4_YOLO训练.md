# 第二阶段任务4：YOLO 训练与 CS 视频推理

## 一、需要配置的环境和工具

Ubuntu、`robot-ai-vision`、Python 3.11、PyTorch、Ultralytics、OpenCV、FFmpeg 与 Git。先按第二阶段任务3安装 PyTorch，确认 CPU 或 NVIDIA 驱动和 CUDA 构建；然后在 Ubuntu 终端运行：

```bash
conda activate robot-ai-vision
python -m pip install ultralytics opencv-python
sudo apt update
sudo apt install -y ffmpeg
python -c "import torch, ultralytics, cv2; print(torch.__version__, ultralytics.__version__, torch.cuda.is_available())"
ffmpeg -version
```

首次推理需下载预训练权重，[Ultralytics 安装与预测教程](https://docs.ultralytics.com/quickstart/)列出运行方式。培训方需发放 CS 图片、标注、类别表、划分及独立视频。

## 二、最终任务与提交内容

### 需要学习的内容

- 认识目标检测框、类别、置信度、IoU 和 NMS；使用预训练 YOLO 模型对示例图片和视频推理，读取检测结果。
- 学习 YOLO 图片与标签配对、归一化坐标、类别表和数据 YAML；按场景或视频片段划分训练、验证和测试数据，并可视化检查标注。
- 学习迁移训练、权重保存、验证集选模，以及 Precision、Recall、mAP 和混淆矩阵的基础含义。
- 学习逐帧读取视频、写出检测 CSV 和可播放标注视频，区分视频播放 FPS 与推理 FPS。

**学习资源：**[霹雳吧啦 Wz YOLO 系列](https://www.bilibili.com/video/BV1yi4y1g7ro/) 的检测框、IoU 和检测基础；[Ultralytics 入门](https://docs.ultralytics.com/quickstart/)与[检测数据格式](https://docs.ultralytics.com/datasets/detect/)。

第二阶段可以使用 Agent 辅助；提交前自行运行、检查并解释代码。

### 必做：YOLO 原生推理、迁移训练与 CS 视频

**提交位置：** `phase2/task04/`。

#### 输入与前置材料

先使用 YOLO 官方预训练模型识别公开示例图片／视频；再使用培训方发放的 CS 人物图片、标注、类别表、片段分组和独立评测视频。类别语义为 `counter_terrorist`（警）与 `terrorist`（匪），编号以发放类别表为准。培训方尚需提供数据、标注、授权范围、类别表及独立视频。

#### 模型和数据要求

按录制片段或场景划分训练、验证、测试集；相邻帧不可跨集合。核对图片／标签配对、空标签、重复、越界和类别，至少可视化 20 张不同类别、尺寸或遮挡情况的标注图，记录数据版本与修正。编写与实际目录、类别相符的 YOLO YAML；先运行一轮小规模训练，再进行正式迁移训练，使用验证集选权重与参数，固定后在独立测试集评估。

#### 输出与验收

1. 保留原生模型图片／视频推理结果，列出类别、置信度和检测框；原生类别不等同于自定义警／匪类别。
2. 保存自定义模型、训练曲线、测试集分类别 Precision、Recall、mAP、混淆矩阵与失败样例。
3. 在完整 CS 评测视频逐帧推理，输出可播放的标注视频和 CSV。检测记录至少包含 `frame_id,timestamp_s,class_id,class_name,confidence,x1,y1,x2,y2`，对无检测帧保留帧级统计。记录输入视频 FPS、输出播放 FPS 与推理处理 FPS。
4. 提交源码、YAML、数据版本和划分、参数、评估摘要与 README。大数据、权重和视频通过可访问链接提供，附 SHA-256 与加载方式。

### 提交内容与检查

- 在个人 Fork 的本任务分支提交 `phase2/task04/` 下的推理和训练代码、数据 YAML、依赖、数据版本与划分说明、参数、评估摘要和 README。
- 提供原生模型结果、自定义模型评估与失败样例、视频逐帧 CSV 摘要；权重和可播放标注视频通过培训方可访问的链接提供并记录 SHA-256。
- 在培训方仓库 PR 中填写运行命令、评测指标及素材版本；等待培训方正式发放训练数据、标注和视频后完成对应部分。

## 三、提交至作业仓库

培训方公开仓库：[https://github.com/o-1717986918/robot-ai-training-homework](https://github.com/o-1717986918/robot-ai-training-homework)。学员将仓库 Fork 到自己的 GitHub 账号，在自己的 Fork 中推送分支，再向培训方仓库创建 PR；无需培训方邀请或仓库写入权限。`GITHUB_USERNAME` 是占位符，请在下方所有命令和地址中替换为自己的 GitHub 用户名。仓库、Fork、分支及 PR 均公开。

1. 打开Ubuntu 终端，在仓库目录从自己上一任务已推送的分支创建本任务分支：

```bash
cd ~/robot-ai/course
git status
git fetch origin
git switch -c student/GITHUB_USERNAME/phase2-task04 origin/student/GITHUB_USERNAME/phase2-task03
```

如果当前有需要保留的未提交修改，先完成提交。若本任务分支已在本机创建，将最后一条命令替换为 `git switch student/GITHUB_USERNAME/phase2-task04`。

2. 完成本项内容，在仓库根目录执行，确认 `git status` 后推送：

```bash
cd ~/robot-ai/course
git add -- phase2/task04
git status
git commit -m "Complete phase2-task04"
git push -u origin student/GITHUB_USERNAME/phase2-task04
```

3. 打开**培训方仓库**的 **Pull requests → New pull request → compare across forks**：选择 `base repository: o-1717986918/robot-ai-training-homework`、`base: main`、`head repository: GITHUB_USERNAME/robot-ai-training-homework`、`compare: student/GITHUB_USERNAME/phase2-task04`，填写任务名称、运行方法与结果，点击 **Create pull request**。按任务要求运行项目，检查输出并在 PR 中记录实际结果。

4. 保留 PR 和已推送分支，下一任务从本分支继续。将大量数据、模型或视频放在培训方可访问的存储位置，在 README 提供链接与 SHA-256；少量结果放任务目录的 `samples/`。不要提交密钥、虚拟环境和完整数据集。
