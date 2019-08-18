from algs4.Stack import Node


def insert_after(first, second):
    if first is None or second is None:
        pass
    second_last_node = Node()
    while second.next is not None:
        second_last_node = second.next

    second_last_node.next = first.next
    first.next = second
