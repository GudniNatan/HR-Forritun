# Class Rectangle goes here
class Rectangle:
    def __init__(self, length=0, width=0):
        if length < 0:
            length = 0
        if width < 0:
            width = 0
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return self.__length * 2 + self.__width * 2

    def __str__(self):
        return "Length: {}, Width: {}".format(self.__length, self.__width)

    def __repr__(self):
        return "Rectangle({},{})".format(self.__length, self.__width)

    def __eq__(self, other):
        return self.area() == other.area()
