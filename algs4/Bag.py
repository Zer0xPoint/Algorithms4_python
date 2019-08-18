class Bag:
    def __init__(self):
        self.__first = None

    def add(self, item):
        __old_first = self.__first
        self.__first = Node()
        # print(Node())
        self.__first.item = item
        self.__first.next = __old_first

    def __iter__(self):
        self.__current = self.__first
        while self.__current is not None:
            yield self.__current.item
            self.__current = self.__current.next


class Node:
    def __init__(self):
        self.item = None
        self.next = None


test_list = ['hello', '-', 'pop', 'pop', 'world', 'pop']
b = Bag()
for i in test_list:
    b.add(i)
for i in b:
    print(i)
