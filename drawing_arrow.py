import cv2
import pandas as pd
import numpy as np

# CSVファイルからデータを読み込む
df = pd.read_csv('data.csv')
df_bubbles = pd.read_csv('bubbles.csv')

# 2次元空間のサイズを指定
width = 800
height = 600

# 空の画像を生成
canvas = 255 * np.ones((height, width, 3), dtype=np.uint8)

# 矢印を描画する関数


def interpolate_color(count):
    red = min(255, 2 * count*12)
    blue = max(0, 255 - 2 * count*12)
    return (blue, 0, red)


def draw_arrow(image, x1, y1, x2, y2, color, thickness):
    arrowed_line = cv2.arrowedLine(image, (x1, y1), (x2, y2), color, thickness)


def draw_bubble(image, x, y, size):
    color = (200, 100, 100)  # 薄い青色
    thickness = -1  # 塗りつぶす
    radius = max(5, min(50, size))  # 円の半径を制限
    circle = cv2.circle(image, (x, y), radius, color, thickness)


# 各行のデータを使って矢印を描画
for index, row in df.iterrows():
    x1 = int(row['x1_plot'])
    y1 = int(row['y1_plot'])
    x2 = int(row['x2_plot'])
    y2 = int(row['y2_plot'])
    color = interpolate_color(int(row['count']))
    thickness = int(row['count'])
    draw_arrow(canvas, x1, y1, x2, y2, color, thickness)

for index, row in df_bubbles.iterrows():
    x = int(row['x1_plot'])
    y = int(row['y1_plot'])
    size = int(row['count'])
    draw_bubble(canvas, x, y, size)

# 矢印を表示
cv2.imshow('Arrows', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
