import math


class Circle(object):
    def __init__(self, radius):
        try:
            self.__radius = float(radius)
        except ValueError:
            self.__radius = 0.0
        self.__perimeter = 0.0
        self.__area = 0.0
        self.calculate_area()
        self.calculate_perimeter()

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            self.__radius = 0
        self.calculate_area()
        self.calculate_perimeter()

    def get_radius(self):
        return self.__radius

    def calculate_area(self):
        self.__area = (self.__radius ** 2) * math.pi

    def calculate_perimeter(self):
        self.__perimeter = (self.__radius * 2) * math.pi

    def __str__(self):
        return "Area: {:.2f}\nPerimeter: {:.2f}".format(
            self.__area, self.__perimeter)


def main():
    radius = input("Radius of circle: ")
    circle = Circle(radius)
    print(circle)
    circle.set_radius(circle.get_radius() + 1.0)
    print(circle)

main()
