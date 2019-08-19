from algs4.Deque import Deque


class DoubleStack:
    def __init__(self):
        self.__right_stack = Deque()
        self.__left_stack = self.__right_stack
        self.__right_N = 0
        self.__left_N = 0

    def size_of_right_stack(self):
        return self.__right_N

    def size_of_left_stack(self):
        return self.__left_N

    def right_stack_is_empty(self):
        return self.__right_N == 0

    def left_stack_is_empty(self):
        return self.__left_N == 0

    def push_right(self, item):
        self.__right_stack.push_right(item)
        self.__right_N += 1

    def push_left(self, item):
        self.__left_stack.push_left(item)
        self.__left_N += 1

    def pop_right(self):
        return self.__right_stack.pop_right()

    def pop_left(self):
        return self.__left_stack.pop_left()


d = DoubleStack()
for i in range(10):
    d.push_right(i)
    print(d.size_of_right_stack())
    # print(d.size_of_left_stack())

for i in range(5):
    d.push_left(i)
    # print(d.size_of_right_stack())
    print(d.size_of_left_stack())

for i in range(3):
    print(d.pop_left())
    print(d.pop_right())
    # print(d.size_of_right_stack())
    # print(d.size_of_left_stack())
