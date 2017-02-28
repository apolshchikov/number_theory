from math import sqrt
from itertools import count, islice


class GaussInteger(object):
    def __init__(self, a, b):
        # GI = a + bi
        self.a = a
        self.b = b

    def is_prime(self):
        if self.a != 0 and self.b != 0:
            return self.check_prime(self.a**2 + self.b**2)
        elif self.a == 0 and self.b != 0:
            return self.check_prime(abs(self.b)) and self.check_inert(self.b)
        elif self.a != 0 and self.b == 0:
            return self.check_prime(abs(self.a)) and self.check_inert(self.a)
        else:
            return False

    @staticmethod
    def check_inert(x):
        return abs(x) % 4 == 3

    @staticmethod
    def check_prime(x):
        if x < 2:
            return False
        else:
            return x > 1 and all(x % i for i in islice(count(2), int(sqrt(x) - 1)))


