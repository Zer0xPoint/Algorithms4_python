from algs4.BinarySearch import BinarySearch
from algs4.BinarySearchMinIndex import BinarySearchMinIndex


class StaticSETofInts:
    def __init__(self, keys):
        self.__a = []
        for i in range(len(keys)):
            self.__a.append(keys[i])
        self.__a.sort()

    def contains(self, key):
        return True if BinarySearch.rank(key, self.__a) > 0 else False

    def how_many(self, key):
        count = 0
        min_key_index = BinarySearchMinIndex.rank(key, self.__a)
        if min_key_index > 0:
            count += 1
            current_index = min_key_index + 1
            while current_index < len(self.__a):
                while self.__a[current_index] == key:
                    current_index += 1
                    count += 1
                    break
                current_index += 1
        return count


random_num_list = list(map(int, open('random_numbers').readline().strip().split(',')))
s = StaticSETofInts(random_num_list)
print(s.contains(109867))
print(s.how_many(109867))

