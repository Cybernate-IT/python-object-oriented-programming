from abc import ABC, abstractmethod

# Abstract Class: Animal
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    # Abstract method to be implemented by subclasses
    @abstractmethod
    def make_sound(self):
        pass

# Interface: Swimmer
class Swimmer(ABC):
    # Abstract method to be implemented by classes
    @abstractmethod
    def swim(self):
        pass

# Concrete Class: Dog (inherits from Animal and implements Swimmer)
class Dog(Animal, Swimmer):
    def make_sound(self):
        return "Woof!"

    def swim(self):
        return f"{self.name} is swimming."

# Concrete Class: Cat (inherits from Animal)
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Creating instances of concrete classes
dog = Dog(name="Buddy")
cat = Cat(name="Whiskers")

# Displaying information about animals
print(f"{dog.name} says: {dog.make_sound()}")
print(f"{dog.name} can swim: {dog.swim()}")

print("\n")

print(f"{cat.name} says: {cat.make_sound()}")

