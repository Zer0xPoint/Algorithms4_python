import random


def compare_list_a_b(a, b):
    index_a = 0
    index_b = 0
    while index_a < len(a) and index_b < len(b):
        if a[index_a] < b[index_b]:
            index_a += 1
        elif a[index_a] > b[index_b]:
            index_b += 1
        else:
            print(a[index_a])
            index_a += 1
            index_b += 1


sorted_list_a = [random.randint(0, 100000) for i in range(10000)]
sorted_list_b = [random.randint(0, 100000) for i in range(10000)]
sorted_list_a.sort()
sorted_list_b.sort()
print(sorted_list_a)
print(sorted_list_b)

compare_list_a_b(sorted_list_a, sorted_list_b)
