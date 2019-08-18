import math


class Interval1D:

    def __init__(self, lo, hi):
        if math.isinf(lo) or math.isinf(hi):
            raise ValueError('Endpoints must be finite')
        if math.isnan(lo) or math.isnan(hi):
            raise ValueError('Endpoints cannot be NaN')

        if lo <= hi:
            self.__lo = lo
            self.__hi = hi
        else:
            raise ValueError('Illegal interval')

    def __repr__(self) -> str:
        return '[' + str(self.__lo) + ',' + str(self.__hi) + ']'

    def intersect(self, that):
        if self.__lo > that.__hi:
            return False
        if self.__hi < that.__lo:
            return False
        return True
