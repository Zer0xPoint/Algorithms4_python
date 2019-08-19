import random


def binary_search(key, a):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if key > a[mid]:
            lo = mid + 1
        elif key < a[mid]:
            hi = mid - 1
        else:
            return mid
    return -1


def random_match(T):
    for n in range(3, 7):
        N = 10 ** n
        count = 0
        for i in range(T):
            n1 = []
            n2 = []
            n1 = create_size_n_random_int_list(n1, N)
            n2 = create_size_n_random_int_list(n2, N)
            n2.sort()
            for n1_num in n1:
                if binary_search(n1_num, n2) == -1:
                    continue
                count += 1
            print(count)
        print(count / T)
    # print(n1, n2)


def create_size_n_random_int_list(a, N):
    for i in range(N):
        a.append([random.randint(0, 10 ** 6)])
    return a


random_match(4)
