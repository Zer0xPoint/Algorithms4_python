# 一个队列实现的栈
# 要求每次操作复杂度均为线性

from algs4.MyQueue import MyQueue


class Stack_by_Queue:
    def __init__(self):
        self.__queue = MyQueue()
        self.__N = 0

    def is_empty(self):
        return self.__N == 0

    def size(self):
        return self.__N

    def push(self, item):
        self.__queue.enqueue(item)
        self.__N += 1

    def pop(self):
        for i in range(self.__N - 1):
            self.__queue.enqueue(self.__queue.dequeue())
        self.__queue.dequeue()
        self.__N -= 1
        # print(self.__queue)


sq = Stack_by_Queue()
sq.push(1)
sq.push(2)
sq.push(3)
sq.push(4)
sq.pop()
sq.push(5)
sq.pop()
sq.pop()
