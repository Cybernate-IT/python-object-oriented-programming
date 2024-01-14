# Declaration of Attributes in Classes, Instance Attributes, and Class Attributes

# Class definition
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
        self.is_hungry = True  # Instance attribute

    # Instance method
    def bark(self):
        print(f"{self.name} says: Woof!")

# Creating instances
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 2)

# Accessing instance attributes
print(f"{dog1.name} is {dog1.age} years old and is hungry: {dog1.is_hungry}")
print(f"{dog2.name} is {dog2.age} years old and is hungry: {dog2.is_hungry}")

# Accessing class attribute
print(f"All dogs belong to the species: {Dog.species}")

# Modifying instance attribute
dog1.is_hungry = False
print(f"{dog1.name} is hungry: {dog1.is_hungry}")

# Modifying class attribute (applies to all instances)
Dog.species = "Canis lupus familiaris"
print(f"All dogs now belong to the species: {Dog.species}")
