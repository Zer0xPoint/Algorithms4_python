import time

test_list = [1, 1, 1, 1, 1, 2, 3, 2, 4, 1, 5, 6, 7, 8, 9, 9, 1, 1, 1, 5]


def remove_repeat(test_list):
    new_list = []

    start = time.time()
    for i in test_list:
        flag = True
        for j in new_list:
            if i.__hash__() == j.__hash__() or i == j:  # 先比较hash值 相同的话直接跳过
                flag = False
                break
        if flag:
            new_list.append(i)
    stop = time.time()
    print(str(stop - start))

    start1 = time.time()
    new_set = set(test_list)  # 转换为set去重
    new_set_list = list(new_set)  # 转换为list
    stop1 = time.time()
    print(str(stop1 - start1))
    print(new_set_list)
    return new_list


print(remove_repeat(test_list))
