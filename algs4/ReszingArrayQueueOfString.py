class ResizingArrayQueueOfStrings:
    def __init__(self):
        self.__a = [0]
        self.__N = 0
        self.__i = self.__N - 1

    def is_empty(self):
        return self.__N == 0

    def size(self):
        return self.__N == 0

    def resize(self, max):
        temp = [0 for i in range(max)]
        for i in range(self.__N):
            temp[i] = self.__a[i]
        self.__a = temp

    def enqueue(self, item):
        if self.__N == len(self.__a):
            self.resize(2 * len(self.__a))
        self.__a[self.__N] = item
        self.__N += 1

    def dequeue(self):
        self.__N -= 1
        item = self.__a[0]
        self.__a = self.__a[1:len(self.__a)]
        if self.__N > 0 and self.__N == len(self.__a) // 4:
            self.resize(len(self.__a) // 2)
        print(item)
        return item

    def __iter__(self):
        return self

    def __next__(self):
        self.__i += 1
        if self.__i == self.__N:
            raise StopIteration
        return self.__a[self.__i]


q = ResizingArrayQueueOfStrings()
q.enqueue('1')
q.enqueue('2')
q.enqueue('3')
q.dequeue()
q.dequeue()
q.enqueue('4')
q.enqueue('5')
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue('6')
q.enqueue('7')
q.enqueue('8')
q.enqueue('9')
q.enqueue('10')
q.enqueue('11')
q.enqueue('12')
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
