from abc import ABC, abstractmethod

# Abstract Class: Shape
class Shape(ABC):
    # Abstract method for calculating area (must be implemented by subclasses)
    @abstractmethod
    def calculate_area(self):
        pass

    # Concrete method in the abstract class
    def display_info(self):
        print("This is a shape.")

# Concrete Subclass: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implementation of the abstract method for calculating area
    def calculate_area(self):
        return 3.14 * self.radius**2

    # Additional method specific to Circle
    def display_radius(self):
        print(f"Radius: {self.radius}")

# Concrete Subclass: Square
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    # Implementation of the abstract method for calculating area
    def calculate_area(self):
        return self.side_length**2

    # Additional method specific to Square
    def display_side_length(self):
        print(f"Side Length: {self.side_length}")

# Creating instances of concrete subclasses
circle = Circle(radius=5)
square = Square(side_length=4)

# Displaying information about the shapes
print("Information about Shapes:")
circle.display_info()
circle.display_radius()
print(f"Area of Circle: {circle.calculate_area()}")

print("\n")

square.display_info()
square.display_side_length()
print(f"Area of Square: {square.calculate_area()}")
