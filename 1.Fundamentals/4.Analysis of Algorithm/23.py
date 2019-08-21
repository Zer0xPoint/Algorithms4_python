# 分数的二分查找
# 要求复杂度在对数级别
import random

N = 100
x = 0.25
list_a = list(set([random.randint(1, N) for i in range(N)]))
print(list_a)
# p = 0
# q = 1
# while p < q < len(list_a):
#     # mid = p + (q - p) // 2
#     if 0 < list_a[p] / list_a[q] - x <= 1 / N:
#         print(p, q)
#         break
#     elif list_a[p] / list_a[q] - x > 1 / N:
#         q += 1
#     else:
#         p += 1
p_lo = 0
q_lo = 0
p_hi = len(list_a)
q_hi = p_hi
while p_lo < p_hi and q_lo < q_hi:
    p_mid = p_lo + (p_hi - p_lo) // 2
    q_mid = q_lo + (q_hi - q_lo) // 2
    if x - list_a[p_mid] / list_a[q_mid] > 1 / N ** 2:
        print(p_mid, q_mid)
    elif x - list_a[p_mid] / list_a[q_mid] < 1 / N ** 2:
        pass
# todo
# 提示两个分母均小于N的数之差 不小于1/N**2
# x和p/q满足以上条件
