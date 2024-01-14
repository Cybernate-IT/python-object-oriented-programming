# Class Declaration

# Class definition
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

# Object instantiation
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Labrador")

# Accessing object attributes and methods
print(f"{dog1.name} is a {dog1.breed}.")
dog1.bark()

print(f"{dog2.name} is a {dog2.breed}.")
dog2.bark()
