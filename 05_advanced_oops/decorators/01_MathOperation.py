# Decorator function for logging
def log_decorator(method):
    def wrapper(self, *args, **kwargs):
        print(f"Calling {method.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = method(self, *args, **kwargs)
        print(f"{method.__name__} returned {result}")
        return result
    return wrapper

# Decorator function for timing
def timing_decorator(method):
    import time

    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        result = method(self, *args, **kwargs)
        end_time = time.time()
        print(f"{method.__name__} took {end_time - start_time:.5f} seconds to execute")
        return result
    return wrapper

# Class with decorated methods
class MathOperations:
    def __init__(self):
        pass

    @log_decorator
    @timing_decorator
    def add(self, x, y):
        return x + y

    @log_decorator
    @timing_decorator
    def multiply(self, x, y):
        return x * y

# Creating an instance of the class
math_operations_instance = MathOperations()

# Calling the decorated methods
result_add = math_operations_instance.add(5, 7)
result_multiply = math_operations_instance.multiply(3, 4)

print("Result of addition:", result_add)
print("Result of multiplication:", result_multiply)
