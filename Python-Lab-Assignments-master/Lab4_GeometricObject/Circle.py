#Kelcy Gooch
#kjg116
#class Section 1

#imports GeometricObject File
from math import pi
from GeometricObject import *

class Circle(GeometricObject):

    def __init__(self, radius = 0, filled = False, color = ""):
        #initializes base class
        super().__init__(filled, color)
        self.radius = radius

    def area(self):
        area = (self.radius * self.radius) * pi
        return area

    def circumference(self):
        circumference = 2 * self.radius * pi
        return circumference

