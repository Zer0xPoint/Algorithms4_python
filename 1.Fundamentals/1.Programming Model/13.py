def lg (N):
    res = 0
    while N >= 2:
        N /= 2
        res += 1
    return res
    
N = 9
print(lg(N))
