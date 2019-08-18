class Accumulator:
    def __init__(self):
        self.__total = 0
        self.__N = 0

    def add_data_value(self, val):
        self.__N += 1
        self.__total += val

    def mean(self):
        return self.__total // self.__N
