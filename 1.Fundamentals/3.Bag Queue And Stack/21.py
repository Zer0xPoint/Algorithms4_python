from algs4.MyQueue import MyQueue


def find(linked_list, key):
    for item in linked_list:
        if item == key:
            return True
    return False


test_queue = MyQueue()
for i in range(10):
    test_queue.enqueue(i)

print(find(test_queue, 10))
