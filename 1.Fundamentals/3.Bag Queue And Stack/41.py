class MyQueue:
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__N = 0

    def is_empty(self):
        return self.__N == 0

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
        if self.is_empty():
            self.__last = None
        self.__N -= 1
        return item

    def get_first_node(self):
        return self.__first

    def recreate_queue(self):
        __new_queue = MyQueue()
        for item in self:
            __new_queue.enqueue(item)
        return __new_queue

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


# test_list = ['hello', '-', 'pop', 'pop', 'world', 'pop']
# p = MyQueue()
# for i in range(1):
#     p.enqueue(i)
# p.dequeue()
#
# for i in p:
#     print(i)
q = MyQueue()
for i in range(10):
    q.enqueue(i)
r = MyQueue.recreate_queue(q)
print(*q)
print(*r)

