"""标注 JSON 转 YOLO TXT 格式（保存在同目录）"""

import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

INPUT_DIR = SCRIPT_DIR / '../your_data'  # JSON 文件所在目录
# 输出 TXT 保存在同目录

# 类别映射（改成你自己的类别列表，顺序决定 class_id）
CLASSES = [
    'pod-box', 'pod', 'branch fruiting node', 'fruiting node',
    'branch', 'shattered pod-box', 'shattered pod',
    'scale bar', 'root', 'main stem'
]

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

        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        x_min, x_max = min(xs), max(xs)
        y_min, y_max = min(ys), max(ys)

        cx = (x_min + x_max) / 2 / img_w
        cy = (y_min + y_max) / 2 / img_h
        w = (x_max - x_min) / img_w
        h = (y_max - y_min) / img_h

        lines.append(f"{class_id} {cx:.6f} {cy:.6f} {w:.6f} {h:.6f}")

    # 保存到同目录
    output_path = json_path.with_suffix('.txt')
    output_path.write_text('\n'.join(lines), encoding='utf-8')


# 批量转换
input_dir = INPUT_DIR.resolve()
json_files = list(input_dir.glob('*.json'))
for jf in json_files:
    json_to_yolo(jf)
    print(f'转换: {jf.name}')

print(f'完成: {len(json_files)} 个文件')
