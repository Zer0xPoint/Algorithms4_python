class VisualCounter:
    def __init__(self, N, max):
        self.__N = N
        self.__max = max
        self.__numbers_of_operation = 0
        self.__count = 0

    def increment(self):
        self.check_numbers_of_operation()
        self.__count += 1

    def decrement(self):
        self.check_numbers_of_operation()
        self.__count -= 1

    def check_numbers_of_operation(self):
        if self.__numbers_of_operation > self.__N:
            print('The number of operations is greater than N')
            return -1
        self.__numbers_of_operation += 1
