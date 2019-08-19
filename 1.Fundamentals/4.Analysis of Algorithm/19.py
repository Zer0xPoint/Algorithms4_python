# 矩阵局部最小元素
# 要求算法复杂度O(N)

import random

N = 6
matrix_a = [[random.randint(0, N) for i in range(N)] for j in range(N)]
# 遍历数组，复杂度为O(N)
for i in range(N ** 2):
    x_index = i % N
    y_index = i // N
    if x_index > 0 and y_index > 0 and x_index + 1 < N and y_index + 1 < N:
        # 知道坐标直接访问数组，复杂度为O(1)
        print('Yes', matrix_a[y_index][x_index]) if matrix_a[y_index][x_index] < min(matrix_a[y_index - 1][x_index],
                                                                                     matrix_a[y_index + 1][x_index],
                                                                                     matrix_a[y_index][x_index - 1],
                                                                                     matrix_a[y_index][
                                                                                         x_index + 1]) else print('No')
for i in matrix_a:
    print(i)
