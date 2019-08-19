def exR1(n):
    if n <= 0:
        return ""
    return exR1(n - 3) + str(n) + exR1(n - 2) + str(n)

print(exR1(6))
