# Object Attributes and Methods

# Class definition
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.is_hungry = True  # Initial state

    def bark(self):
        print(f"{self.name} says: Woof!")

    def eat(self):
        if self.is_hungry:
            print(f"{self.name} is eating.")
            self.is_hungry = False
        else:
            print(f"{self.name} is not hungry right now.")

# Instantiating objects
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Max", "Labrador", 2)

# Accessing object attributes and methods
print(f"{dog1.name} is a {dog1.breed} and is {dog1.age} years old.")
dog1.bark()
dog1.eat()

print(f"{dog2.name} is a {dog2.breed} and is {dog2.age} years old.")
dog2.bark()
dog2.eat()
