class MathOperations:
    @staticmethod
    def add(x, y):
        # Static method to add two numbers
        return x + y

    @staticmethod
    def multiply(x, y):
        # Static method to multiply two numbers
        return x * y

    @staticmethod
    def square_root(x):
        # Static method to calculate the square root of a number
        return x ** 0.5

# Using static methods without creating an instance of the class
sum_result = MathOperations.add(5, 7)
product_result = MathOperations.multiply(3, 4)
sqrt_result = MathOperations.square_root(25)

print("Sum:", sum_result)
print("Product:", product_result)
print("Square Root:", sqrt_result)
