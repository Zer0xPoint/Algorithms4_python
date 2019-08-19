class Rational:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
        self.gcd()

    def plus(self, b):
        self.__numerator = self.__numerator * b.__denominator + b.__numerator * self.__denominator
        self.__denominator = self.__denominator * b.__denominator
        self.gcd()
        return self

    def minus(self, b):
        self.__numerator = self.__numerator * b.__denominator - b.__numerator * self.__denominator
        self.__denominator = self.__denominator * b.__denominator
        self.gcd()
        return self

    def times(self, b):
        self.__numerator = self.__numerator * b.__numerator
        self.__denominator = self.__denominator * b.__denominator
        self.gcd()
        return self

    def divides(self, b):
        self.__numerator = (self.__numerator * b.__denominator) / (b.__numerator * self.__denominator)
        if self.__numerator < 1:
            self.__denominator = 1 // self.__numerator * self.__denominator * b.__denominator
            self.__numerator = 1
        else:
            self.__denominator = self.__denominator * b.__denominator
        self.gcd()
        return self

    def gcd(self):
        denominator = self.__denominator
        numerator = self.__numerator
        while denominator != 0:
            t = numerator % denominator
            numerator = denominator
            denominator = t
        self.__numerator //= numerator
        self.__denominator //= numerator
        self.__numerator = int(self.__numerator)
        self.__denominator = int(self.__denominator)

    def __repr__(self) -> str:
        return '[' + str(self.__numerator) + ',' + str(self.__denominator) + ']'


r1 = Rational(1, 1233)
r2 = Rational(1, 3)
print(r1.plus(r2))
print(r1.minus(r2))
print(r1.times(r2))
print(r1.divides(r2))
