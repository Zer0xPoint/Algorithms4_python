from algs4.BinarySearch import BinarySearch


class BinarySearchMinIndex:
    @classmethod
    def rank(cls, key, a):
        lo = 0
        hi = len(a) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if a[mid] < key:
                lo = mid + 1
            elif a[mid] > key:
                hi = mid - 1
            else:
                min_index = cls.rank(key, a[:mid])
                return min_index if mid > min_index > 0 else mid
        return -1


# random_num_list = list(map(int, open('random_numbers').readline().strip().split(',')))
# random_num_list.sort()
random_num_list = [1, 1, 1, 1, 2, 3, 4]
print(BinarySearch.rank(1, random_num_list))
print(BinarySearchMinIndex.rank(1, random_num_list))
