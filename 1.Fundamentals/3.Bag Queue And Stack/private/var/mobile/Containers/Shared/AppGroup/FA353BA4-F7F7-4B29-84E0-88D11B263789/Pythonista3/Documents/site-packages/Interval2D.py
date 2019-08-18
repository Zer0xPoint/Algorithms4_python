class Interval2D:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def intersects(self, that):
        if not self.__x.intersects(that.__x):
            return False
        if not self.__y.intersects(that.__y):
            return False
        return True

    def contains(self, p):
        return self.__x.contains(p.x()) and self.__y.contains(p.y())
