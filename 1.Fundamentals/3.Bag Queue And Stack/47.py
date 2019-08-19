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

    def catenation(self, second_queue):
        self.__last.next = second_queue.__first
        self.__last = second_queue.__last
        return self

    def __iter__(self):
        self.__current = self.__first
        while self.__current is not None:
            yield self.__current.item
            self.__current = self.__current.next


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

    def catenation(self, second_stack):
        __current = self.__first
        while __current.next is not None:
            __current = __current.next
        __current.next = second_stack.__first
        # __current = second_stack.__last
        return self

    def __iter__(self):
        self.__current = self.__first
        while self.__current is not None:
            yield self.__current.item
            self.__current = self.__current.next


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

    def catenation(self, second_steque):
        self.__last.next = second_steque.__first
        self.__last = second_steque.__last
        return self

    def __iter__(self):
        self.__current = Node()
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


q = MyQueue()
q1 = MyQueue()
s = Stack()
s1 = Stack()
sq = Steque()
sq1 = Steque()
for i in range(5):
    q.enqueue(i)
    q1.enqueue(i)
    s.push(i)
    s1.push(i)
    sq.push(i)
    sq1.push(i)

# p.dequeue()
# q1.dequeue()
q = q.catenation(q1)
s = s.catenation(s1)
sq = sq.catenation(sq1)
print(*q)
print(*s)
print(*sq)
