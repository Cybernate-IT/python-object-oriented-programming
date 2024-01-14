# Setter and Getter Methods

# Class definition
class Person:
    def __init__(self, name, age):
        # Private attributes
        self._name = name
        self._age = age

    # Getter methods
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    # Setter methods
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print("Invalid name format. Name must be a string.")

    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age >= 0:
            self._age = new_age
        else:
            print("Invalid age format. Age must be a non-negative integer.")

# Creating an instance
person = Person("Alice", 25)

# Accessing attributes using getter methods
print(f"Name: {person.get_name()}")
print(f"Age: {person.get_age()}")

# Updating attributes using setter methods
person.set_name("Bob")
person.set_age(30)

# Accessing updated attributes
print(f"Updated Name: {person.get_name()}")
print(f"Updated Age: {person.get_age()}")

# Trying to set invalid values
person.set_name(123)
person.set_age(-5)
