import time


def binary_search(key, a):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] < key:
            lo = mid + 1
        elif a[mid] > key:
            hi = mid - 1
        else:
            return mid
    return -1


def brute_force_search(key, a):
    for n in a:
        if n == key:
            return n
    return -1


data_w_dir = 'largeW.txt'
data_t_dir = 'largeT.txt'
data_w = []
with open(data_w_dir, 'r') as f:
    for line in f:
        data_w.append(int(line.strip()))
data_w.sort()
# data_t = []
with open(data_t_dir, 'r') as f:
    for line in f:
        line = int(line.strip())
        start_bin = time.time()
        binary_search(line, data_w)
        bin_time = time.time() - start_bin

        start_bru = time.time()
        brute_force_search(line, data_w)
        bru_time = time.time() - start_bru
        print(bin_time)
        print(bru_time)
