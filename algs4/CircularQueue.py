class CircularQueue:
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
            self.__last.next = self.__first
        self.__N += 1

    def dequeue(self):
        item = self.__first.item
        self.__first = self.__first.next
        self.__N -= 1
        if self.is_empty():
            self.__last = None
        return item

    def find_node(self, key):
        __current_node = Node()
        __current_node = self.__first
        while __current_node.next is not None:
            if __current_node.item == key:
                return __current_node
            __current_node = __current_node.next

    def delete_node(self, key):
        __current_node = self.find_node(key)
        # __current_node.next.prior = __current_node.prior
        # __current_node.prior.next = __current_node.next
        __current_node = __current_node.next
        self.__N -= 1

    def get_first(self):
        return self.__first

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
# p = CircularQueue()
# for i in test_list:
#     p.enqueue(i)
# for i in p:
#     print(i)
