import math

class Point:
    def __init__(self, x=0, y=0):
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise TypeError("Both x and y should be numeric values (int or float).")
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("x-value must be a numeric.")
        self.x = x

    def set_y(self, y):
        if not isinstance(y, (int, float)):
            raise TypeError("y-value must be a numeric.")
        self.y = y
    
    def clone(self):
        return Point(self.x, self.y)
    
    def distance(self, other_point):
        if not isinstance(other_point, Point):
            raise TypeError("The argument must be a Point type.")
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
    
    def __str__(self):
        return "X: {}".format(self.x), "Y: {}".format(self.y)