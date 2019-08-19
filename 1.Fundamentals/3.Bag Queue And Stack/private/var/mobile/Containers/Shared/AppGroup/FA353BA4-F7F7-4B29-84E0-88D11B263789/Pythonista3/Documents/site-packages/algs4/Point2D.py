import math


class Point2D:
    def __init__(self, x, y):
        if math.isinf(x) or math.isinf(y):
            raise ValueError('Coordinates must be finite')
        if math.isnan(x) or math.isnan(y):
            raise ValueError('Coordinates cannot be NaN')
        if x == 0.0:
            self.__x = 0.0
        else:
            self.__x = x
        if y == 0.0:
            self.__y = 0.0
        else:
            self.__y = y

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def __repr__(self) -> str:
        return super().__repr__()

    def distance_to(self, that):
        dx = self.__x - that.__x
        dy = self.__y - that.__y
        return dx * dx + dy * dy
