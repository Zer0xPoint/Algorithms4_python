import random

a = [random.random() * 1000 for i in range(100)]
a.sort()  # 排序 复杂度logN
min_difference = a[len(a) - 1]
min_numbers = [0, 0]
for i in range(len(a) - 1):
    if a[i + 1] - a[i] < min_difference:
        min_difference = a[i + 1] - a[i]
        min_numbers[0] = a[i]
        min_numbers[1] = a[i + 1]
print(min_numbers)
