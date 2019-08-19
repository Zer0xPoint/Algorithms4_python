from algs4.MyQueue import Node, MyQueue


def reverse(x):
    first = x
    reverse_node = Node()
    while first is not None:
        second = first.next
        first.next = reverse_node
        reverse_node = first
        first = second


q = MyQueue()
for i in range(10):
    q.enqueue(i)
first_node = q.get_first_node()
reverse(first_node)
print(q)
