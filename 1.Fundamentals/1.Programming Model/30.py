N = 10
t = []


def co_prime(i, j):
    print(i, j)
    if j == 0 or i == 0:
        return i if j == 0 else j
    return co_prime(min(i, j), max(i, j) % min(i, j))


for i in range(N):
    t.append([])
    for j in range(N):
        if co_prime(i, j) == 1:  # 验证是否为互质
            t[i].append(True)
        else:
            t[i].append(False)

print(t)
