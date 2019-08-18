import random


def two_sum_faster(list_a):
    lo = 0
    hi = len(list_a) - 1
    count = 0
    while lo < hi:
        if list_a[lo] + list_a[hi] == 0:
            lo += 1
            hi -= 1
            count += 1
        elif list_a[lo] + list_a[hi] < 0:
            lo += 1
        else:
            hi -= 1
    return count


def three_sum_faster(list_a):
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


a = [random.randint(-100, 100) for i in range(100)]
a.sort()
print(two_sum_faster(a))
print(three_sum_faster(a))

# 以上是logN解决方法 需要线性N方法
# 故用空间换时间 用python自带的dict来完成查找
# 因为dict是一个hash_table 故查找只需要O1的时间完成
