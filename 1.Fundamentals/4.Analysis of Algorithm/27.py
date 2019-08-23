# 两个栈实现的队列
# 实现的队列的所有操作均摊后为常数时间

from algs4.Stack import Stack
import random


class Deque_by_two_Stack:
    def __init__(self):
        self._list_two_stack = [Stack(), Stack()]
        # self.s1 = Stack()
        # self.s2 = Stack()
        self._N = 0
        # self._count = 0

    def is_empty(self):
        return self._N == 0

    def size(self):
        return self._N

    def push(self, item):
        self._list_two_stack[0].push(item)
        # self._count += 1
        self._N += 1

    def pop(self):
        if self.is_empty():
            print('Deque is Empty, Nothing to pop')
            return -1
        for i in range(self._N - 1):
            self._list_two_stack[1].push(self._list_two_stack[0].pop())
        self._list_two_stack[0].pop()
        for i in range(self._N - 1):
            self._list_two_stack[0].push(self._list_two_stack[1].pop())

        self._N -= 1
        # self._count += 1


N = 10
list_a = [i for i in range(N)]

# push_or_pop = [random.randint(0, 1) for i in range(2 * N)]

print(list_a)
# print(push_or_pop)

ds = Deque_by_two_Stack()

# for i in range(N):
#     if push_or_pop[i]:
#         ds.push()
# print(Deque_by_two_Stack()._list_two_stack)
ds.push(0)
ds.push(1)
ds.push(2)
ds.push(3)
ds.pop()
ds.push(4)
ds.pop()
ds.pop()
ds.push(5)