import random

import matplotlib.pyplot as plt

N = 100
r = random.random() * 10
l = random.uniform(0, r)
step = (l + r) / N
print(l, r)
print(step)

a_list = []
for i in range(N):
    a_list.append(0)
for i in range(N):
    ran_num = random.random() * 10
    if ran_num > r or ran_num < l:
        continue
    index = int(ran_num // step)
    a_list[index] += 1
while 0 in a_list:
    a_list.remove(0)

print(a_list)
plt.hist(a_list, bins=N)
plt.show()
