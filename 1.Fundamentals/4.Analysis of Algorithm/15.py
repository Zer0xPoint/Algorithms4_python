import random


def two_sum(list_a):
    list_a.sort()
    lo = 0
    hi = len(list_a) - 1
    count = 0
    while lo < hi:
        if list_a[lo] + list_a[hi] == 0:
            count += 1
            lo += 1
            # while list_a[lo] + list_a[hi] == 0:
            #     lo += 1
            #     count += 1
            hi -= 1
            # while list_a[lo] + list_a[hi] == 0:
            #     hi -= 1
            #     count += 1
        elif list_a[lo] + list_a[hi] < 0:
            lo += 1
        else:
            hi -= 1
    return count


def three_sum(list_a):
    list_a.sort()
    count = 0
    for i in range(len(list_a)):
        lo = i + 1
        hi = len(list_a) - 1
        while lo < hi:
            if list_a[lo] + list_a[hi] + list_a[i] == 0:
                lo += 1
                hi -= 1
                count += 1
            elif list_a[lo] + list_a[hi] + list_a[i] < 0:
                lo += 1
            else:
                hi -= 1
    return count


# 以上方法需要先对list进行排序 复杂度为O(logN)

# 空间换时间 用python自带的dict来完成查找
# 因为dict是一个hash_table 故查找复杂度为O(1)
# 对一个长度为N的数组进行查找 复杂度O(N)

def two_sum_faster(list_a):
    dict_a = {}
    count = 0
    for i in range(len(list_a)):
        if dict_a.__contains__(-list_a[i]) and i != dict_a.get(-list_a[i]):
            # dict_a.pop(-list_a[i])
            # print(list_a[i], dict_a.get(-list_a[i]), i)
            # del dict_a[-list_a[i]]
            count += 1
        dict_a[list_a[i]] = i
    return count


def three_sum_faster(list_a):
    dict_a = {}


a = [random.randint(-100, 100) for i in range(100)]
# print(two_sum(a))
# print(three_sum(a))
print(two_sum_faster(a))
