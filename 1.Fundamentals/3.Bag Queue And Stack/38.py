# class GeneralizeQueue:
#     def __init__(self):
#         self.__list = []
#         self.__N = 0
#
#     def is_empty(self):
#         return self.__N == 0
#
#     def insert(self, item):
#         self.__list.append(item)
#         self.__N += 1
#
#     def delete(self):
#         item = self.__list[0]
#         self.__list = self.__list[1:len(self.__list)]
#         return item
#
#     def __iter__(self):
#         for item in self.__list:
#             yield item


class GeneralizeQueue:
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__N = 0

    def is_empty(self):
        return self.__N == 0

    def insert(self, item):
        __old_last = self.__last
        self.__last = Node()
        self.__last.item = item
        if self.is_empty():
            self.__first = self.__last
        else:
            __old_last.next = self.__last
        self.__N += 1

    def delete(self):
        item = self.__first.item
        self.__first = self.__first.next
        self.__N -= 1
        return item

    def __iter__(self):
        __current = Node()
        __current = self.__first
        while __current is not None:
            yield __current.item
            __current = __current.next


class Node:
    def __init__(self):
        self.next = None
        self.item = None


g = GeneralizeQueue()
for i in range(10):
    g.insert(i)
print(*g)
print(g.delete())
print(*g)
print(g.delete())
print(*g)
print(g.delete())
print(*g)
print(g.delete())
print(*g)
