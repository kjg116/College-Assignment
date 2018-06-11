#Kelcy Gooch
#kjg116
#class Section 1

from GeometricObject import *

class Square(GeometricObject):

    def __init__(self, side = 0, filled = False, color = ""):
        #intializes base class
        super().__init__(filled, color)
        self.side = side

    def area(self):
        area = self.side * self.side
        return area

    def perimeter(self):
        perimeter = self.side * 4
        return perimeter
