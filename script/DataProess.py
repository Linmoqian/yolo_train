"""数据集划分脚本：从 your_data 划分到 dataset"""

import os
import random
from shutil import copy
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

INPUT_DIR = SCRIPT_DIR / '../your_data'   # 源数据（放你的图片和json的地方，全复制到这，注意先运行json2txt.py）
OUTPUT_DIR = SCRIPT_DIR / '../dataset'   # 输出目录（自动划分）

# 改这里的比例
VAL_RATE = 0.3   # 验证集占比
TEST_RATE = 0.1  # 测试集占比
SEED = 0         # 随机种子

def main():
    random.seed(SEED)

    src = INPUT_DIR.resolve()
    out = OUTPUT_DIR.resolve()

    # 获取所有图片
    images = [f for f in os.listdir(src) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(images)

    # 计算划分数量
    n = len(images)
    n_val = int(n * VAL_RATE)
    n_test = int(n * TEST_RATE)
    n_train = n - n_val - n_test

    train_imgs = images[:n_train]
    val_imgs = images[n_train:n_train + n_val]
    test_imgs = images[n_train + n_val:]

    # 创建目录
    for split in ['train', 'val', 'test']:
        (out / 'images' / split).mkdir(parents=True, exist_ok=True)
        (out / 'labels' / split).mkdir(parents=True, exist_ok=True)

    # 复制文件
    def copy_set(img_list, split_name):
        for img in img_list:
            # 复制图片
            copy(src / img, out / 'images' / split_name / img)
            # 复制标签 (同名 .txt)
            label = Path(img).stem + '.txt'
            label_src = src / label
            if label_src.exists():
                copy(label_src, out / 'labels' / split_name / label)

    copy_set(train_imgs, 'train')
    copy_set(val_imgs, 'val')
    copy_set(test_imgs, 'test')

    print(f'总数: {n}')
    print(f'训练集: {n_train}')
    print(f'验证集: {n_val}')
    print(f'测试集: {n_test}')
    print('划分完成')


if __name__ == '__main__':
    main()
