class FixedCapacityStackOfStrings:
    def __init__(self, cap):
        self.__a = [0 for i in range(cap)]
        self.__N = 0

    def is_empty(self):
        return self.__N == 0

    def size(self):
        return self.__N

    def push(self, item):
        if self.__N == len(self.__a):
            self.resize(2 * len(self.__a))
        self.__a[self.__N] = item
        self.__N += 1

    def pop(self):
        self.__N -= 1
        print(self.__a[self.__N])
        self.__a[self.__N] = None
        if 0 < self.__N < len(self.__a) // 4:
            self.resize(len(self.__a) // 2)

    def resize(self, max):
        temp = [0 for i in range(max)]
        for i in range(self.__N):
            temp[i] = self.__a[i]
        self.__a = temp


s = FixedCapacityStackOfStrings(1)
s.push('to')
s.push('be')
s.push('or')
s.push('not')
s.push('to')
s.pop()
s.push('be')
s.pop()
s.pop()
s.push('that')
s.pop()
s.pop()
s.pop()
s.push('is')
print(s.size())
