class Steque:
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__N = 0

    def size(self):
        return self.__N

    def is_empty(self):
        return self.__N == 0

    def push(self, item):
        __old_first = self.__first
        self.__first = Node()
        self.__first.item = item
        self.__first.next = __old_first
        if self.is_empty():
            self.__last = self.__first
        self.__N += 1

    def pop(self):
        __item = self.__first.item
        self.__first = self.__first.next
        if self.is_empty():
            self.__last = None
        self.__N -= 1
        print(__item)
        return __item

    def enqueue(self, item):
        __old_last = self.__last
        self.__last = Node()
        self.__last.item = item
        if self.is_empty():
            self.__first = self.__last
        else:
            __old_last.next = self.__last
            self.__last.next = None
        self.__N += 1

    def __iter__(self):
        self.__current = Node()
        self.__current = self.__first
        while self.__current is not None:
            yield self.__current.item
            self.__current = self.__current.next


class Node:
    def __init(self):
        self.item = None
        self.next = None


s = Steque()
for i in range(3):
    s.push(i)
    s.enqueue(i)
    s.pop()

print(*s)
