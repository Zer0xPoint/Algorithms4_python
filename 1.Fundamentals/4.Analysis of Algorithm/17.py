import random

a = [random.random() * 1000 for i in range(100)]
min_number = a[0]
max_number = a[0]
for i in a:
    if i > max_number:
        max_number = i
    elif i < min_number:
        min_number = i

print(max_number - min_number)