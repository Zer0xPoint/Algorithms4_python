import math


def ln(n):
    if n == 0: return 0
    return math.log(n) + ln(n - 1)


res = ln(3)
print(res)
