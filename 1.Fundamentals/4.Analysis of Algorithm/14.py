def four_sum(list_a):
    list_a.sort()
    count = 0
    for i in list_a:
        for j in list_a:
            for k in list_a:
                for l in list_a:
                    if i + j + k + l == 0:
                        count += 1
