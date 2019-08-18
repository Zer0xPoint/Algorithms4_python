n = 10000
l = range(1,n)

for i in l:
    res = i
    for a in range(1,6)[::-1]:
        res = ((res * 5) + a * 4) / 4.0
    if str(res).endswith('.0'):
        print(res)
        