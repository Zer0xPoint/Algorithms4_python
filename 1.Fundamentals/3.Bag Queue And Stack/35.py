import random


class RandomQueue:
    def __init__(self):
        self.__list = [0 for i in range(1)]
        self.__N = 0

    def is_empty(self):
        return self.__N == 0

    def enqueue(self, item):
        if self.__N == len(self.__list):
            self.resizing(2 * self.__N)
        self.__list[self.__N] = item
        self.__N += 1

    def dequeue(self):
        self.__N -= 1
        item = self.__list[0]
        self.__list = self.__list[1:len(self.__list)]
        if self.__N > 0 and self.__N == len(self.__list) // 4:
            self.resizing(len(self.__list) // 2)
        return item

    def sample(self):
        # random.randint(0, len(self.__list))
        rand_index = random.randint(0, self.__N)
        print(self.__list[rand_index])

    def resizing(self, max):
        temp = [0 for i in range(max)]
        for i in range(self.__N):
            temp[i] = self.__list[i]
        self.__list = temp

    def __iter__(self):
        for i in range(self.__N):
            j = random.randint(0, self.__N)
            self.__list[i], self.__list[j] = self.__list[j], self.__list[i]

        for i in self.__list:
            yield i


r = RandomQueue()
for i in range(10):
    r.enqueue(i)
r.sample()
print(*r)
