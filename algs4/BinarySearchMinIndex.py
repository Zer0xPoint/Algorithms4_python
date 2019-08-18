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
