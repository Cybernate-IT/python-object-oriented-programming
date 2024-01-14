# Defining Methods in Classes: Instance Methods, Class Methods, and Static Methods

# Class definition
class MathOperations:
    # Class attribute
    pi = 3.14159

    def __init__(self, value):
        # Instance attribute
        self.value = value

    # Instance method
    def square(self):
        return self.value ** 2

    # Class method
    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius ** 2

    # Static method
    @staticmethod
    def add(x, y):
        return x + y

# Using instance method
result_square = MathOperations(5).square()
print(f"Square: {result_square}")

# Using class method
result_circle_area = MathOperations.circle_area(4)
print(f"Circle Area: {result_circle_area}")

# Using static method
result_addition = MathOperations.add(3, 7)
print(f"Addition: {result_addition}")
