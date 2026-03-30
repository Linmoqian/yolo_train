"""标注 JSON 转 YOLO TXT 格式"""
import json
from pathlib import Path

# 脚本所在目录
SCRIPT_DIR = Path(__file__).parent

# 输入输出路径 （这里是你需要改的）
input_dir = SCRIPT_DIR / '../my_data'
output_dir = SCRIPT_DIR / '../dataset/labels'
# 类别映射，改成你自己的类别列表，顺序决定 class_id
CLASSES = [
    'pod-box', 'pod', 'branch fruiting node', 'fruiting node',
    'branch', 'shattered pod-box', 'shattered pod',
    'scale bar', 'root', 'main stem'
]
# 下面的不用关注
def json_to_yolo(json_path: Path):
    """转换单个 JSON 文件"""
    data = json.loads(json_path.read_text(encoding='utf-8'))
    img_w, img_h = data['imageWidth'], data['imageHeight']

    lines = []
    for shape in data['shapes']:
        if shape['label'] not in CLASSES:
            continue
        class_id = CLASSES.index(shape['label'])
        points = shape['points']

        # 计算边界框
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        x_min, x_max = min(xs), max(xs)
        y_min, y_max = min(ys), max(ys)

        # YOLO 格式: class_id cx cy w h (归一化)
        cx = (x_min + x_max) / 2 / img_w
        cy = (y_min + y_max) / 2 / img_h
        w = (x_max - x_min) / img_w
        h = (y_max - y_min) / img_h

        lines.append(f"{class_id} {cx:.6f} {cy:.6f} {w:.6f} {h:.6f}")

    # 保存
    output_path = output_dir / f"{json_path.stem}.txt"
    output_path.write_text('\n'.join(lines), encoding='utf-8')

# 批量转换
output_dir.mkdir(parents=True, exist_ok=True)
json_files = list(input_dir.glob('*.json'))
for jf in json_files:
    json_to_yolo(jf)
    print(f'转换: {jf.name}')

print(f'完成: {len(json_files)} 个文件')
