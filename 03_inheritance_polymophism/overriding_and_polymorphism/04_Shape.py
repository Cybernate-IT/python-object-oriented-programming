from abc import ABC, abstractmethod

# Abstract Class (Interface)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete Implementation of the Abstract Class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Concrete Implementation of the Abstract Class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Function demonstrating abstraction with abstract classes
def print_shape_details(shape):
    print(f"Area: {shape.area()} square units")
    print(f"Perimeter: {shape.perimeter()} units")
    print()

# Creating instances of the classes
circle = Circle(radius=5)
rectangle = Rectangle(length=4, width=6)

# Demonstrating abstraction with abstract classes
print("Abstract Classes and Interfaces:")
print("Circle Details:")
print_shape_details(circle)

print("Rectangle Details:")
print_shape_details(rectangle)
