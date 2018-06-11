#Kelcy Gooch
#kjg116
#class Section 1

class GeometricObject:

    def __init__(self, filled = False, color = ""):
        self.color = color
        self.filled = filled

    def setColor(self, color):
        self.color = color

    def setFilled(self, filled):
        self.filled = filled

    def getColor(self):
        return self.color

    def getFilled(self):
        return self.filled

