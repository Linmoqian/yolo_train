import yaml
from ultralytics import YOLO

MODEL = 'yolov12n.pt' # 模型权重文件路径（可以找其他的模型权重）
DATA = 'config/dataset.yaml' # 数据集配置文件路径

#加载训练参数
with open('config/train.yaml', encoding='utf-8') as f:
    cfg = yaml.safe_load(f)

YOLO(MODEL).train(data=DATA, **cfg)
