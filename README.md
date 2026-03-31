# YOLO 训练脚本

简洁的 YOLO 模型训练示例，基于 Ultralytics YOLO。

## 目录结构

```
yolo_train/
├── main.py              # 训练入口
├── config/
│   ├── train.yaml       # 训练参数
│   └── dataset.yaml     # 数据集配置
├── script/
│   ├── json2txt.py      # JSON 转 YOLO 格式
│   └── DataProess.py    # 数据集划分
├── your_data/           # 放你的原始数据
│   ├── *.jpg
│   └── *.json
└── dataset/             # 自动生成的训练数据
    ├── images/
    │   ├── train/
    │   ├── val/
    │   └── test/
    └── labels/
        ├── train/
        ├── val/
        └── test/
```

## 使用流程

### 1. 准备数据

将图片和标注文件放入 `your_data/` 目录

### 2. JSON 转 TXT

```bash
python script/json2txt.py
```

### 3. 划分数据集

修改 `script/DataProess.py` 中的比例。

运行：
```bash
python script/DataProess.py
```

### 4. 配置类别

修改 `config/dataset.yaml` 中的类别：
```yaml
nc: 10  # 类别数量
names:
  0: class_0
  1: class_1
  ...
```

### 5. 开始训练

```bash
python main.py
```

## 标注格式

YOLO 格式 (`.txt`)：
```
class_id center_x center_y width height
0 0.5 0.5 0.3 0.4
```
- 坐标归一化到 `[0, 1]`
- `center_x, center_y`: 目标中心点
- `width, height`: 目标宽高
