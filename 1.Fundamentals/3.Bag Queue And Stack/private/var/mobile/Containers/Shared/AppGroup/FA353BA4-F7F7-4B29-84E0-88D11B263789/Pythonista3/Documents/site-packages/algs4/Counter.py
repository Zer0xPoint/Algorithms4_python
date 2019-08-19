class Counter:
    def __init__(self, id):
        self.__id = id
        self.__count = 0

    def increment(self):
        self.__count += 1

    def tally(self):
        return self.__count
