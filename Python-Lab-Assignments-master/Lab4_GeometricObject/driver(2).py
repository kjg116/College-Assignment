#############################
#Author:Kayla Huddleston
#Lab 4 - Inheritance
#Geometric Objects - driver
#############################

from GeometricObject import *
from Circle import *
from Square import *

def main():
    '''
    For these lines, rearrange the arguments so that they are in the same
    order as the ones you passed in your __init__ functions.
    '''
    
    circle = Circle(3, True, "red")
    if circle.getFilled() == True:
        print("The", circle.getColor()," circle has an area of", circle.area(), ", and a circumference of", circle.circumference())
    elif circle.getFilled() == False:
        print("The circle has an area of", circle.area(), ", a circumference of", circle.circumference())

    square = Square(5, False, "maroon")
    if square.getFilled() == True:
        print("The", square.getColor()," square has an area of", square.area(), ", and a perimeter of", square.perimeter())
    elif square.getFilled() == False:
        print("The square has an area of", square.area(), ", a perimeter of", square.perimeter())
    
main()
