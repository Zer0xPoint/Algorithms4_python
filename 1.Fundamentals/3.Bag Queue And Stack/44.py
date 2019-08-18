import random

from algs4.Stack import Stack


class Buffer:
    def __init__(self):
        self.__right = Stack()
        self.__left = Stack()
        self.__N = 0

    def insert(self, c):
        self.__right.push(c)
        self.__N += 1

    def delete(self):
        self.__N -= 1
        return self.__right.pop() if not self.__right.is_empty() else ''

    def left(self, k):
        for i in range(k):
            if self.__left.is_empty():
                return
            self.__right.push(self.__left.pop())

    def right(self, k):
        for i in range(k):
            if self.__right.is_empty():
                return
            self.__left.push(self.__right.pop())

    def size(self):
        return self.__N


b = Buffer()
for i in range(100):
    b.insert(random.randint(0, 99))

b.right(10)
print(b.delete())
b.left(5)
print(b.delete())
print(b.size())
