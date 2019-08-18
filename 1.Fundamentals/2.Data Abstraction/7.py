def mystery(s):
    N = len(s)
    if N <= 1:
        return s
    a = s[0:N // 2]
    b = s[N // 2:N]
    return mystery(a) + mystery(b)


print(mystery('hello world'))
