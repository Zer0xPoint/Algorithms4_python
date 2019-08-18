import random

from algs4.Interval1D import Interval1D

N = 3
line_list = []
intersect_list = []
for i in range(N):
    lo = random.random()
    hi = lo + random.random()
    line = Interval1D(lo, hi)
    line_list.append(line)
    if i != 0:
        for j in range(i):
            if line.intersect(line_list[j]):
                intersect_list.append(str(line) + ' ' + str(line_list[j]))
print(intersect_list)
