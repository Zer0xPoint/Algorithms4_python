def histogram(a, M):
    res = []
    for i in range(M):
        count = 0
        for item in a:
            if item == (i + 1):
                count += 1
        res.append(count)
    return res

a = [1,1,1,1,3,4,2,1,5,1,2,5,5,2]
M = 5
print(a)
print(histogram(a,M))    
