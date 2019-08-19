class RingBuffer:
    def __init__(self):
        self.__list = [0 for i in range(8)]
        self.__N = 0
        self.__current_index = 0

    def is_empty(self):
        return self.__N == 0

    def size(self):
        return self.__N

    def insert(self, item):
        if self.__current_index >= len(self.__list):
            self.__current_index -= len(self.__list)
        self.__list[self.__current_index] = item
        self.__current_index += 1
        self.__N += 1
        pass

    def delete(self):
        __delete_index = self.__current_index - 1
        if __delete_index >= len(self.__list):
            __delete_index -= len(self.__list)
        item = __delete_index
        self.__list[__delete_index] = 0
        self.__current_index -= 1
        self.__N -= 1
        return item

    def __iter__(self):
        for i in self.__list:
            yield i


r = RingBuffer()
for i in range(10):
    r.insert(i)
for i in range(5):
    r.delete()
print(*r)
