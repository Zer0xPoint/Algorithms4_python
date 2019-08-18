n = 100000
l = range(1, n)
nums = range(10)

for i in l:
    sq = i * i
    cb = sq * i
    sq_l = list(str(sq))
    cb_l = list(str(cb))

    combine_l = sq_l + cb_l

    combine_l_reduce = list(set(combine_l))
    if len(combine_l_reduce) == 10:
        print(combine_l)
        print(i)
        break
