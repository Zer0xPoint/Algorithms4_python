from algs4.MyQueue import MyQueue

test_str = '0123456789'
k = 5
res = 0
test_queue = MyQueue()
for i in range(len(test_str)):
    test_queue.enqueue(i)

count = test_queue.size() - k + 1

for i in range(count):
    res = test_queue.dequeue()
print(res)
