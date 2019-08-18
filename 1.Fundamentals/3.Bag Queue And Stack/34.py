import random


class RandomBag:
    def __init__(self):
        self.__list = []
        self.__N = 0

    def is_empty(self):
        return self.__N == 0

    def size(self):
        return self.__N

    def add(self, item):
        self.__list.append(item)
        self.__N += 1

    def __iter__(self):
        random.shuffle(self.__list)
        for i in self.__list:
            yield i


r = RandomBag()
for i in range(10):
    r.add(i)
print(*r)
