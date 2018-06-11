#Kelcy Gooch
#Sec 4 Lab
#Sec 1 Class
#KJG116

from fractions import gcd

class Rational:

    def __init__(self, a, b):
        #Used self.rational for the comparison functions
        self.rational = a / b
        #Used two below to represent given value
        self.numerator = a
        self.denominator = b
        #Used two below to represent new value when trying to add or subtract
        self.totalN = a // gcd(a,b)
        self.totalD = b // gcd(a,b)
        #Used to return total
        self.total = ""
        if b == 0:
            raise ZeroDivisionError

    def __str__(self):
        return str(self.totalN) + "/" + str(self.totalD)

    def __add__(self, other):
        self.totalD = (self.denominator * other.denominator)
        self.totalN = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        self.total = (str(self.totalN) + "/" + str(self.totalD))
        return self.total

    def __sub__(self, other):
        self.totalD = (self.denominator * other.denominator)
        self.totalN = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        self.total = (str(self.totalN) + "/" + str(self.totalD))
        return self.total

    def __mul__(self, other):
        self.totalN = (self.numerator * other.numerator)
        self.totalD = (self.denominator * other.denominator)
        self.total = (str(self.totalN) + "/" + str(self.totalD))
        return self.total

    def __truediv__(self, other):
        self.totalN = (self.numerator * other.denominator)
        self.totalD = (self.denominator * other.numerator)
        self.total = (str(self.totalN) + "/" + str(self.totalD))
        return self.total

    def __lt__(self, other):
        if self.rational < other.rational:
            return True
        else:
            return False
    def __le__(self, other):
        if self.rational <= other.rational:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.rational == other.rational:
            return True
        else:
            return False
    def __ge__(self, other):
        if self.rational >= other.rational:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.rational > other.rational:
            return True
        else:
            return False



