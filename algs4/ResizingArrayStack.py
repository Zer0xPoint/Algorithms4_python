class ResizingArrayStack:
    def __init__(self):
        self.__a = [0]
        self.__N = 0
        self.__i = self.__N - 1

    def is_empty(self):
        return self.__N == 0

    def size(self):
        return self.__N

    def resize(self, max):
        temp = [0 for i in range(max)]
        for i in range(self.__N):
            temp[i] = self.__a[i]
        self.__a = temp

    def push(self, item):
        if self.__N == len(self.__a):
            self.resize(2 * len(self.__a))
        self.__a[self.__N] = item
        self.__N += 1

    def pop(self):
        self.__N -= 1
        item = self.__a[self.__N]
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


s = ResizingArrayStack()
# s.push('to')
s.push('be')
s.push('or')
s.push('not')
s.push('to')
for i in s:
    print(i)