# Use Cases for Subclasses and Inheritance

# Parent Class (Base Class)
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement the area method.")

# Subclasses (Derived Classes)
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Creating instances of the classes
circle = Circle("Circle", 5)
rectangle = Rectangle("Rectangle", 4, 6)

# Calculating and displaying areas
print(f"Area of {circle.name}: {circle.area()} square units")
print(f"Area of {rectangle.name}: {rectangle.area()} square units")
