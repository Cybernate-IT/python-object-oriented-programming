# Encapsulating Methods
# Private Methods
# Access Modifiers
# Benefits and Use Cases of Encapsulation

# Class demonstrating encapsulated methods
class Calculator:
    def __init__(self):
        # Private attribute (encapsulated with double leading underscores)
        self.__result = 0

    # Public method for addition
    def add(self, a, b):
        result = a + b
        self.__update_result(result)  # Accessing private method for result update
        return result

    # Public method for subtraction
    def subtract(self, a, b):
        result = a - b
        self.__update_result(result)  # Accessing private method for result update
        return result

    # Private method for updating the result
    def __update_result(self, value):
        # Internal implementation details (hidden from external access)
        self.__result = value

    # Public method for displaying the result
    def display_result(self):
        return f"Result: {self.__result}"

# Creating an instance of the class
calculator = Calculator()

# Demonstrating encapsulated methods and benefits of encapsulation
print("Encapsulating Methods, Private Methods, Access Modifiers:")
# Attempting to access private methods directly (without using public methods)
# Note: This is not recommended in practice, but done here for demonstration purposes.
# Accessing private method __update_result directly
calculator._Calculator__update_result(42)
print("Result (Direct Access):", calculator.display_result())

# Using public methods for addition and subtraction
result_add = calculator.add(10, 5)
result_subtract = calculator.subtract(20, 8)

# Displaying results using public method for displaying the result
print("\nUsing Public Methods:")
print("Result (Addition):", calculator.display_result())
print("Result (Subtraction):", calculator.display_result())

# Attempting to access private attribute directly
# Note: This is not recommended in practice, but done here for demonstration purposes.
print("\nAttempting to Access Private Attribute (Direct Access):", calculator._Calculator__result)
