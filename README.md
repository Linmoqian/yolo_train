# YOLO 训练脚本

简洁的 YOLO 模型训练示例，基于 Ultralytics YOLO。

## 目录结构

```
yolo_train/
├── main.py              # 训练入口
├── config/
│   ├── train.yaml       # 训练参数
│   └── dataset.yaml     # 数据集配置
└── datasets/            # 数据集目录
    └── my_dataset/
        ├── images/
        │   ├── train/
        │   ├── val/
        │   └── test/
        └── labels/
            ├── train/
            ├── val/
            └── test/
```

## 数据集标注格式

```
class_id center_x center_y width height
0 0.5 0.5 0.3 0.4
```

- 坐标归一化到 `[0, 1]`
- `center_x, center_y`: 目标中心点
- `width, height`: 目标宽高