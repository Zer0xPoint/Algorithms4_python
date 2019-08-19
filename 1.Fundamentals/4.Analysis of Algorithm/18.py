import random

a = [random.randint(0, 100) for i in range(100)]
a = list(set(a))
print(len(a))

n = len(a) // 2
lo = 0
hi = len(a)
while lo < hi:
    mid = lo + (hi - lo) // 2
    if a[mid + 1] > a[mid] and a[mid - 1] > a[mid]:
        print(a[mid])
        break
    elif a[mid + 1] <= a[mid]:
        lo = mid + 1
    else:
        hi = mid - 1
