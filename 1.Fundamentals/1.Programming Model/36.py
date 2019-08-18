import random


def shuffle(original_a):
    N = len(original_a)
    a = list(original_a)
    for i in range(N):
        r = i + random.randint(0, N - i - 1)
        # r = 0 + random.randint(0, N - i - 1)  # 糟糕的打乱
        temp = a[i]
        a[i] = a[r]
        a[r] = temp
    return a


def shuffle_test(M, N):
    res = []
    for i in range(M):
        res.append([0] * M)
    for n in range(N):
        a = []
        for i in range(M):
            a.append(i)
        a = shuffle(a)
        print(a)
        for j in range(M):
            i = a[j]
            res[i][j] += 1
    return res


N = 32
list_a = []
for i in range(N):
    list_a.append(i)
print(list_a)
print(shuffle(list_a))
print(shuffle_test(10, 20))
