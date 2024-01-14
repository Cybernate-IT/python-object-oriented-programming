# Creating Classes in Python

# Class definition
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Object instantiation
rectangle1 = Rectangle(5, 8)
rectangle2 = Rectangle(3, 6)

# Accessing object attributes and methods
area1 = rectangle1.calculate_area()
area2 = rectangle2.calculate_area()

# Displaying results
print(f"Area of Rectangle 1: {area1} square units")
print(f"Area of Rectangle 2: {area2} square units")
