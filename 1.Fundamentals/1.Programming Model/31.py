import math
import random

import matplotlib.pyplot as plt

N = 45
p = 0.5
angle = 360 / N  # 计算每个点相隔的角度

point = []
for i in range(N + 1):
    point.append([0] * 2)  # 新建一个N*2的二位列表 用来保存点x，y轴的坐标

for i in range(N):
    point[i][0] = math.cos(2 * math.pi * i / N) / 5.0  # x轴
    point[i][1] = math.sin(2 * math.pi * i / N) / 5.0  # y轴
    plt.scatter(point[i][0], point[i][1], c='black', linewidth='0.0001')  # 绘制散点图

    if i > 0 and p > random.random():  # 如果不是列表第一个点 并且大于概率p
        plt.plot([point[i][0], point[i - 1][0]], [point[i][1], point[i - 1][1]])

print(point)

plt.axes().set_aspect('equal')
plt.show()
