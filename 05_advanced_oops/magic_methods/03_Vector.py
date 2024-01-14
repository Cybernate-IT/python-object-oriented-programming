class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Overloading the addition operator
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        # Overloading the subtraction operator
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Creating instances of Vector
v1 = Vector(x=2, y=3)
v2 = Vector(x=1, y=2)

# Using operator overloading for addition
result_addition = v1 + v2
print("Addition Result:", result_addition)  # Calls __str__ method for string representation

# Using operator overloading for subtraction
result_subtraction = v1 - v2
print("Subtraction Result:", result_subtraction)

