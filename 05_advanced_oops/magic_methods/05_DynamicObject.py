class DynamicObject:
    def __init__(self):
        self._attributes = {}

    def __getattr__(self, name):
        # Customizing attribute retrieval using __getattr__
        if name in self._attributes:
            return self._attributes[name]
        else:
            raise AttributeError(f"'DynamicObject' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        # Customizing attribute assignment using __setattr__
        self._attributes[name] = value

    def __str__(self):
        return str(self._attributes)

# Creating an instance of DynamicObject
dynamic_obj = DynamicObject()

# Customizing attribute access
dynamic_obj.name = "John"
dynamic_obj.age = 25

# Accessing attributes
print("Name:", dynamic_obj.name)  # Calls __getattr__ method
print("Age:", dynamic_obj.age)  # Calls __getattr__ method

# Displaying the attributes using __str__
print("Attributes:", dynamic_obj)
