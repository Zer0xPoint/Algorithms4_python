def exR2(n):
    s = exR2(n - 3) + n + exR2(n - 2) + n
    if n == 0: # <= cant be place
        return ""
    return s

print(exR2(3))

#StackoverflowError
