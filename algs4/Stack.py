class Stack:
    def __init__(self):
        self.__first = None
        self.__N = 0

    def is_empty(self):
        return self.__first is None

    def size(self):
        return self.__N

    def push(self, item):
        __old_first = self.__first
        # self.__first = Node(item, __old_first)
        self.__first = Node()
        self.__first.item = item
        self.__first.next = __old_first
        self.__N += 1

    def pop(self):
        __item = self.__first.item
        self.__first = self.__first.next
        self.__N -= 1
        # print(__item)
        return __item

    def peek(self):
        __item = self.pop()
        self.push(__item)
        return __item

    def __iter__(self):
        self.__current = self.__first
        while self.__current is not None:
            yield self.__current.item
            self.__current = self.__current.next


class Node:
    # def __init__(self, item, old_first):
    #     self.item = item
    #     self.next = old_first
    def __init__(self):
        self.item = None
        self.next = None


# test_list = ['hello', '-', 'pop', 'pop', 'world', 'pop']
# s = Stack()
#
# for i in test_list:
#     s.push(i)
# for i in s:
#     print(i)
