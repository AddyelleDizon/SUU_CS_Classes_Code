shapes = []

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_center(self):
        pass
    
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    PI = 3.14159
    def __init__(self, radius, centerX=0, centerY=0, defaultRad=1):
        self.__radius = radius
        self.__centerX = centerX
        self.__centerY = centerY
        self.__defaultRad = defaultRad
        self.__area = self.get_area()
        self.__center = self.set_center()

    def get_center(self):
        center = (self.__centerX, self.__centerY)
        return center
    
    def get_area(self):
        if self.__radius > 0:
            area = Circle.PI*self.__radius**2
            return area
        else:
            print("Radius cannot be {}. Setting radius to 1.".format(self.__radius))
            return self.__defaultRad
    
    def set_center(self):
        circleCenter = (self.__centerX, self.__centerY)
        return circleCenter
    
    def __str__(self):
        if self.__radius > 0:
            print("Circle with center {}".format(self.__center), "and radius {}. \n".format(self.__radius))
        else:
            print("Circle with center {}".format(self.__center), "and radius {}. \n".format(self.__defaultRad))

class Triangle(Shape):
    def __init__(self, base, height, centerX=0, centerY=0):
        self.__base = base
        self.__height = height
        self.__centerX = centerX
        self.__centerY = centerY
        self.__center = self.set_center()

    def get_center(self):
        center = (self.__centerX, self.__centerY)
        return center
    
    def get_area(self):
        if self.__base > 0 and self.__height > 0:
            area = self.__height*self.__base*0.5
            return area
        elif self.__base <= 0:
            print("Base cannot be {}. Setting base to 1.".format(self.__base))
            self.__base = 1
            return self.__base
        else:
            print("Height cannot be {}. Setting height to 1.".format(self.__height))
            self.__height = 1
            return self.__height
        
    def set_center(self):
        triangleCenter = (self.__centerX, self.__centerY)
        return triangleCenter

    def __str__(self):
        print("Triangle with center {},".format(self.__center), "base {}".format(self.__base), "and height {}. \n".format(self.__height))

class Square(Shape):
    def __init__(self, side, centerX=0, centerY=0):
        self.__side = side
        self.__centerX = centerX
        self.__centerY = centerY
        self.__area = self.get_area()
        self.__center = self.set_center()

    def get_center(self):
        center = (self.__centerX, self.__centerY)
        return center
    
    def get_area(self):
        if self.__side > 0:
            area = self.__side**2
            return area
        else:
            print("Side cannot be {}.".format(self.__side), "Setting height to 1.")
            self.__side = 1
            return self.__side
        
    def set_center(self):
        triangleCenter = (self.__centerX, self.__centerY)
        return triangleCenter

    def __str__(self):
        print("Square with center {},".format(self.__center), "and side length {}. \n".format(self.__side))   

def main():
    userInput = int(input("Please pick an option: \n 1. Create a Shape \n 2. Calculate distance between two shapes \n 3. Calculate the ratio of areas between two shapes \n 4. Quit. \n"))
    while userInput != 4:
        match userInput:
            case 1:
                shapeSelect = int(input("Which shape would you like to create? \n 1. Circle \n 2. Triangle \n 3. Square \n"))
                match shapeSelect:
                    case 1:
                        userRadius = int(input("What is the radius of your circle?: "))
                        userCenterX = int(input("What is the center-x coordinate of your circle?: "))
                        userCenterY = int(input("What is the center-y coordinate of your circle?: "))
                        circle = Circle(userRadius, userCenterX, userCenterY)
                        circle.__str__()

                    case 2:
                        userBase = int(input("What is the base of your triangle?: "))
                        userHeight = int(input("What is the height of your triangle?: "))
                        userCenterX = int(input("What is the center-x coordinate of your triangle?: "))
                        userCenterY = int(input("What is the center-y coordinate of your triangle?: "))
                        triangle = Triangle(userBase, userHeight, userCenterX, userCenterY)
                        triangle.__str__()
                    case 3:
                        userSide = int(input("What is the side of your square?: "))
                        userCenterX = int(input("What is the center-x coordinate of square?: "))
                        userCenterY = int(input("What is the center-y coordinate of your square?: "))
                        square = Square(userSide, userCenterX, userCenterY)
                        square.__str__()
                        
            #case 2: I don't know how to save these shapes to a list.
            #case 3: I don't know how to save these shapes to a list.

if __name__ == "__main__":
    main()
