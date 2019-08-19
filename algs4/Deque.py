class Deque:
    def __init__(self):
        self.__first = Node()
        self.__last = Node()
        self.__N = 0

    def is_empty(self):
        return self.__N == 0

    def size(self):
        return self.__N

    def push_left(self, item):
        # __old_first = Node()
        __old_first = self.__first
        self.__first = Node()
        self.__first.item = item
        if self.is_empty():
            self.__last = self.__first
            # __old_first = Node()
        else:
            __old_first.prior = self.__first
            self.__first.next = __old_first
        self.__N += 1

    def push_right(self, item):
        # __old_last = Node()
        __old_last = self.__last
        self.__last = Node()
        self.__last.item = item
        if self.is_empty():
            self.__first = self.__last
        else:
            __old_last.next = self.__last
            self.__last.prior = __old_last
        self.__N += 1

    def pop_left(self):
        if self.size() <= 1:
            self.__last = self.__first = None
        else:
            self.__first = self.__first.next
            self.__first.prior = None
        self.__N -= 1
        return self.__first.item

    def pop_right(self):
        if self.size() <= 1:
            self.__last = self.__first = None
        else:
            self.__last = self.__last.prior
            self.__last.next = None
        self.__N -= 1
        return self.__last.item

    def __iter__(self):
        self.__current = Node()
        self.__current = self.__first
        while self.__current is not None:
            yield self.__current.item
            self.__current = self.__current.next


class Node:
    def __init__(self):
        self.item = None
        self.next = None
        self.prior = None
