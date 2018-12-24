a = []
for i in range(10):
    a.append(9 - i)

for i in range(10):
    a[i] = a[a[i]]
    
print(a)
