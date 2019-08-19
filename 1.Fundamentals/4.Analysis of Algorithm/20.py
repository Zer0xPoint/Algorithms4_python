# 双调查找
# 要求算法复杂度为N(3lgN)
# 双调数组为一个先递增然后递减的数组
import random

# 生成一个双调数组
N = 100
Ni = N - random.randint(1, N)
list_a_first_half = [random.randint(0, N) for i in range(N - Ni)]
list_a_last_half = [random.randint(0, N) for i in range(Ni)]
list_a_first_half.sort()
list_a_last_half.sort(reverse=True)
list_a = list_a_first_half + list_a_last_half
list_a = [i for i in list_a if list_a.count(i) == 1]  # 保持list顺序 去重
print(list_a)


def find_target(list_a, target):
    max_num_index = find_max(list_a)
    if target == list_a[max_num_index]:
        target_index = max_num_index
    else:
        index_r = find_right(list_a[0: max_num_index], target)
        index_l = find_left(list_a[max_num_index: len(list_a)], target)
        target_index = index_r if index_r is not -1 else index_l
    # print('Find target in index in', target_index) if target_index is not -1 else print('Not find target in list')
    return target_index


def find_max(list_a):
    lo = 0
    hi = len(list_a)
    while lo < hi:
        i = lo + (hi - lo) // 2
        if list_a[i - 1] < list_a[i] > list_a[i + 1]:  # 不存在重复元素
            return i
        elif list_a[i - 1] < list_a[i] < list_a[i + 1]:
            lo = i + 1
        elif list_a[i - 1] > list_a[i] > list_a[i + 1]:
            hi = i
        # else:
        #     hi -= 1
        #     lo += 1


def find_right(list_r, target):
    lo = 0
    hi = len(list_r)
    while lo < hi:
        i = lo + (hi - lo) // 2
        if list_r[i] == target:
            return i
        elif list_r[i] > target:
            hi = i
        else:
            lo = i + 1
    return -1


def find_left(list_l, target):
    lo = 0
    hi = len(list_l)
    while lo < hi:
        i = lo + (hi - lo) // 2
        if list_l[i] == target:
            return i
        elif list_l[i] < target:
            hi = i
        else:
            lo = i + 1
    return -1


target = 7
print(find_target(list_a, target))
