from random import random


class MyQueue:
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__N = 0

    def is_empty(self):
        return self.__first is None

    def size(self):
        return self.__N

    def enqueue(self, item):
        __old_last = self.__last
        # self.__last = Node(item)
        self.__last = Node()
        self.__last.item = item
        if self.is_empty():
            self.__first = self.__last
        else:
            __old_last.next = self.__last
        self.__N += 1

    def dequeue(self):
        item = self.__first.item
        self.__first = self.__first.next
        self.__N -= 1
        if self.is_empty():
            self.__last = None
        return item

    def max_num(self):
        max_num = self.__first.item
        __current = Node()
        __current = self.__first
        while __current.next is not None:
            if __current.item > max_num:
                max_num = __current.item
            __current = __current.next
        return max_num

    def __iter__(self):
        self.__current = self.__first
        while self.__current is not None:
            yield self.__current.item
            self.__current = self.__current.next


class Node:
    # def __init__(self, item):
    #     self.item = item
    #     self.next = None
    def __init__(self):
        self.item = None
        self.next = None


q = MyQueue()
for i in range(100):
    random_num = random()
    q.enqueue(random_num)
print(q.max_num())
