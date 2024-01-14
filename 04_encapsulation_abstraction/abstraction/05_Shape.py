
from abc import ABC, abstractmethod

# Abstract Class: Shape
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Abstract Class: Color
class Color(ABC):
    @abstractmethod
    def apply_color(self):
        pass

# Concrete Class implementing Shape and Color (Multiple Inheritance)
class ColoredShape(Shape, Color):
    def __init__(self, color):
        self.color = color

    def draw(self):
        return f"Drawing a {self.color} shape."

    def apply_color(self):
        return f"Applying {self.color} color."

# Concrete Class implementing only Shape
class Circle(Shape):
    def draw(self):
        return "Drawing a circle."

# Concrete Class implementing only Color
class RedColor(Color):
    def apply_color(self):
        return "Applying red color."

# Function demonstrating the use of classes with multiple inheritance
def process_shapes_and_colors(shapes_and_colors):
    for obj in shapes_and_colors:
        print(obj.draw())
        print(obj.apply_color())
        print("\n")

# Creating instances of concrete classes
colored_circle = ColoredShape(color="blue")
simple_circle = Circle()
red_color = RedColor()

# Using the process_shapes_and_colors function with a list of objects
process_shapes_and_colors(shapes_and_colors=[colored_circle, simple_circle, red_color])
