import random

from algs4.DoubleNode import DoubleNode


def move_to_front(s):
    d = DoubleNode()
    for item in s:
        is_duplicate = False
        for node in d:
            if node == item:
                is_duplicate = True
                d.delete_node(item)
                d.insert_head_node(item)
        if not is_duplicate:
            d.insert_head_node(item)
    return d


test_str = [random.randint(0, 10) for i in range(100)]
# test_str = [8, 0, 9, 8]
print(test_str)
print(*move_to_front(test_str))
