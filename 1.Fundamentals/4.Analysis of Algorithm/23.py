# 分数的二分查找
# 要求复杂度在对数级别
import random

N = 100
x = 0.25
list_a = list(set([random.randint(1, N) for i in range(N)]))
print(list_a)
p = 0
q = 1
while p < q < len(list_a):
    # mid = p + (q - p) // 2
    if 0 < list_a[p] / list_a[q] - x <= 1 / N:
        print(p, q)
        # print(list_a[p] / list_a[q] - x, 1 / N)
        break
    elif list_a[p] / list_a[q] - x > 1 / N:
        # print(list_a[p] / list_a[q] - x, 1 / N)

        q += 1
    else:
        # print(list_a[p] / list_a[q] - x, 1 / N)

        p += 1
