from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

rectangle = Rectangle(8, 3)
triangle = Triangle(4, 6)
square = Square(5)

print("Area of Rectangle:", rectangle.area())
print("Area of Triangle:", triangle.area())
print("Area of Square:", square.area())