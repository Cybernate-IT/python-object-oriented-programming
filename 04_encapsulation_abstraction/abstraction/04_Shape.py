from abc import ABC, abstractmethod

# Abstract Class: Shape
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# Concrete Classes implementing Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Interface: Drawable
class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

# Concrete Classes implementing Drawable
class Canvas(Drawable):
    def draw(self):
        return "Drawing on canvas."

class Screen(Drawable):
    def draw(self):
        return "Displaying on screen."

# Function demonstrating the use of Shape and Drawable
def process_shapes_and_drawables(shapes, drawables):
    for shape in shapes:
        print(f"Area of {type(shape).__name__}: {shape.calculate_area()}")

    for drawable in drawables:
        print(f"{type(drawable).__name__}: {drawable.draw()}")

# Creating instances of concrete classes
circle = Circle(radius=5)
rectangle = Rectangle(length=4, width=6)
canvas = Canvas()
screen = Screen()

# Using the process_shapes_and_drawables function with lists of shapes and drawables
process_shapes_and_drawables(shapes=[circle, rectangle], drawables=[canvas, screen])
