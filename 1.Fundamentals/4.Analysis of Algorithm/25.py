# 扔两个鸡蛋
# 与上一题不同 只有两个鸡蛋
# 成本模型是扔鸡蛋的次数

# 第一种方法
# 将N平均分sqrtN份 在每一份的尾部扔鸡蛋
# 当鸡蛋碎的时候 记录这一份的头部层数lo （第一个鸡蛋）
# 在此层中以lo + 1的方式 每次递增一层扔鸡蛋
# 当鸡蛋碎的时候 所在的一层则为F

import math

N = 2147483647
log_N = int(math.log(N, 10))
F = 123


def sqrt_n(F, log_N):
    hi = 0
    run_time_count01 = 0
    while hi < F:
        hi += log_N
    lo = hi - log_N
    for i in range(lo, hi):
        run_time_count01 += 1
        if i == F:
            print('Find')
            break
    return run_time_count01


# 第二种方法
# 需要在2sqrtF次数完成
# 将N分成 sqrtF份 每份以i**2递增 如 1，4，9，16
# 找到（i-1）**2 < F <= i**2的区间
# 因为 F <= i**2 故 sqrtF ≈ i
# 又因 区间中含有的元素数为 i**2 -（i-1）**2 = 2i - 1 ≈ 2i ≈ 2sqrtF
# 如当i = 3时 区间中有 3**2 - 2**2 = 5个元素
# 故在此区间内找到F最多需要2sqrtF次


def two_times_sqrt_f(F):
    run_time_count02 = 0
    i = 1
    hi = 0
    while hi < F:
        hi = i ** 2
        i += 1
        print(hi)
        # print(i)
    for j in range((i - 1) ** 2, i ** 2):
        run_time_count02 += 1
        if j == F:
            print('Find')
    return run_time_count02


print(sqrt_n(F, log_N))
print(two_times_sqrt_f(F))
