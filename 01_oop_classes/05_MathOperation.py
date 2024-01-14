# Class Methods

# Class definition
class MathOperations:
    # Class method
    @classmethod
    def add(cls, num1, num2):
        print(f"Performing addition using class method.")
        return num1 + num2

    # Another class method
    @classmethod
    def multiply(cls, num1, num2):
        print(f"Performing multiplication using class method.")
        return num1 * num2

# Using class methods
sum_result = MathOperations.add(5, 3)
product_result = MathOperations.multiply(4, 6)

# Displaying results
print(f"Sum Result: {sum_result}")
print(f"Product Result: {product_result}")
