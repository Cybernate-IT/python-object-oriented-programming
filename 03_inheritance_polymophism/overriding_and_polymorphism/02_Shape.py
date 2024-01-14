# Accessing Overridden Methods from the Subclass
# Polymorphism in Python
# Achieving Polymorphism through Method Overriding

# Parent Class (Base Class)
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the area method.")

# Subclasses (Derived Classes)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Function demonstrating polymorphism
def print_area(shape):
    print(f"Area: {shape.area()} square units")

# Creating instances of the classes
circle = Circle(radius=5)
rectangle = Rectangle(length=4, width=6)

# Accessing overridden methods from the subclass
print("Accessing Overridden Methods:")
print_area(circle)
print_area(rectangle)

# Achieving polymorphism through method overriding
shapes = [Circle(radius=3), Rectangle(length=5, width=8)]
print("\nPolymorphism in Action:")
for shape in shapes:
    print_area(shape)
