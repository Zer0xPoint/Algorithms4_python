class DoubleNode:
    def __init__(self):
        self.__first = Node()
        self.__last = Node()
        self.__N = 0

    def is_empty(self):
        return self.__N == 0

    def size(self):
        return self.__N

    def insert_head_node(self, item):
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

    def insert_tail_node(self, item):
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

    def delete_head_node(self):
        if self.size() <= 1:
            self.__last = self.__first = None
        else:
            self.__first = self.__first.next
            self.__first.prior = None
        self.__N -= 1

    def delete_tail_node(self):
        if self.size() <= 1:
            self.__last = self.__first = None
        else:
            self.__last = self.__last.prior
            self.__last.next = None
        self.__N -= 1

    def find_node(self, key):
        __current_node = Node()
        __current_node = self.__first
        while __current_node.next is not None:
            if __current_node.item == key:
                return __current_node
            __current_node = __current_node.next

    def insert_node_before(self, key, item):
        __current_node = self.find_node(key)
        __insert_node = Node()
        __insert_node.item = item
        __insert_node.next = __current_node
        __insert_node.prior = __current_node.prior
        __current_node.prior.next = __insert_node
        __current_node.prior = __insert_node
        self.__N += 1

    def insert_node_after(self, key, item):
        __current_node = self.find_node(key)
        __insert_node = Node()
        __insert_node.item = item
        __insert_node.next = __current_node.next
        __insert_node.prior = __current_node
        __current_node.next.prior = __insert_node
        __current_node.next = __insert_node
        self.__N += 1

    def delete_node(self, key):
        __current_node = self.find_node(key)
        __current_node.next.prior = __current_node.prior
        __current_node.prior.next = __current_node.next
        self.__N -= 1

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


# test_list = ['hello', '-', 'pop', 'pop', 'world', 'pop']
l = DoubleNode()
for i in range(10):
    # l.insert_head_node(i)
    l.insert_tail_node(i)
# l.insert_head_node('hello')
l.delete_head_node()
l.delete_tail_node()
l.insert_node_before(2, 'hello')
l.insert_node_after(1, 'world')
l.delete_node('hello')
# for i in l:
#     print(i)
print(*l)
