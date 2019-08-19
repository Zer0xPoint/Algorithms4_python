import random


def print_max(a):  # 不用保存数组
    max_a = 0
    for n in a:
        if n < max_a:
            continue
        max_a = n
    print(max_a)


def print_mid(a):  # 不用保存数组
    len_a = len(a)
    mid_a = len_a // 2
    print(a[mid_a])


def print_kth_small_number(a):  # 不用保存数组
    k = 10
    list_k = []
    max_in_list = 0
    max_num_index = 0
    for i in range(len(a)):
        if i < k:
            list_k.append(a[i])
            if a[i] > max_in_list:
                max_in_list = a[i]
                max_num_index = i
        else:
            if a[i] < max_in_list:
                list_k[max_num_index] = a[i]
            max_in_list = 0
            max_num_index = 0
            for n in range(len(list_k)):
                if list_k[n] > max_in_list:
                    max_in_list = list_k[n]
                    max_num_index = n
    print(list_k)


def print_sum_of_squares(a):  # 不用保存数组
    res = 0
    for n in a:
        res += n * n
    print(res)


def print_ave(a):  # 不用保存数组
    sum_a = 0
    for n in a:
        sum_a += n
    res = sum_a / len(a)
    print(res)


def print_percentage_more_than_ave(a):  # 不用保存数组
    sum_a = 0
    len_a = len(a)
    for n in a:
        sum_a += n
    ave = sum_a / len_a
    count_more_than_ave = 0
    for n in a:
        if n > ave:
            count_more_than_ave += 1
    res = count_more_than_ave / len_a
    print(str(res * 100) + '%')


def print_rise_order(a):
    print(a.sort())


def print_random_order(a):
    N = len(a)
    for i in range(N):
        ran_num = i + random.randint(0, N - i - 1)  # 保证ran_num在0到N的范围内
        temp = a[i]
        a[i] = a[ran_num]
        a[ran_num] = temp
    print(a)


N = 32
list_a = []
for i in range(N):
    list_a.append(random.random())
print(list_a)

print_max(list_a)
print_mid(list_a)
print_kth_small_number(list_a)
print_sum_of_squares(list_a)
print_ave(list_a)
print_percentage_more_than_ave(list_a)
print_rise_order(list_a)
print_random_order(list_a)
