# 扔鸡蛋
# 楼共N层高 在F层或F以上的楼层扔鸡蛋会碎
# 要求复杂度O(2lgF)

N = 100
F = 72
building = [i for i in range(1, N + 1)]
print(building)


def binary_search(lo_index, hi_index, F):
    while lo_index < hi_index:
        floor = lo_index + (hi_index - lo_index) // 2
        if building[floor] == F:
            # print(floor)
            return floor
        elif building[floor] > F:
            hi_index = floor
        else:
            lo_index = floor + 1


# 一般的二分查找法 复杂度为O(lgN)
lo = 0
hi = len(building)
print(binary_search(lo, hi, F))


# i以2的倍数递增的方式访问N 复杂度为lgF + lgF
# 循环判断 2 ** i 是否大于F 每次循环中i递增 大于F退出循环
# 对区间2**(i-1) ～ 2**i进行二分查找

# 应注意数组越界问题 2**i不应大于总楼层数N

i = 0
while 2 ** i < F:
    i += 1
F_lo = 2 ** (i - 1)
F_hi = min(2 ** i, N)  # 处理越界
print(binary_search(F_lo, F_hi, F))
