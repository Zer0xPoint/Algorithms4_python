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

    def delete_k(self, k):
        if not self.__N > k > 1:
            raise KeyError
        k -= 1
        __temp = self.__first
        while __temp.next is not None:
            k -= 1
            if k <= 0:
                __temp.next = __temp.next.next
            __temp = __temp.next
        self.__N -= 1

    def delete_last_node(self):
        __temp = self.__first
        while __temp.next.next is not None:
            __temp = __temp.next
        self.__last = __temp
        __temp.next = None
        self.__N -= 1

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


test_linked_list = MyQueue()
for i in range(10):
    test_linked_list.enqueue(i)

test_linked_list.delete_last_node()
test_linked_list.delete_k(2)
print(test_linked_list)
