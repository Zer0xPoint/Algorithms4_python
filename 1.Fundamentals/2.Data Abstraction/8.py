from algs4.Counter import Counter


def rank(key, a, counter):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        counter.increment()
        mid = lo + (hi - lo) // 2
        if a[mid] < key:
            lo = mid + 1
        elif a[mid] > key:
            hi = mid - 1
        else:
            return mid
    return -1


list_a = []
for i in range(100000):
    list_a.append(i)
key = 5
rank_counter = Counter('rank')
rank(key, list_a, rank_counter)
print(rank_counter.tally())
