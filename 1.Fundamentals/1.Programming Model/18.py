def mystery(a, b):
    if b == 0:
        return 0
    if b % 2 == 0:
        return mystery(a + a, b // 2)
    return mystery(a + a, b // 2) + a

print(mystery(3, 11))
print(mystery(2, 25))
