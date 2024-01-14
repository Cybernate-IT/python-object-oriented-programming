from abc import ABC, abstractmethod

# Abstract Class: Animal
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

# Abstract Class: Swimmer
class Swimmer(ABC):
    @abstractmethod
    def swim(self):
        pass

# Concrete Class: Fish (inherits from Animal and Swimmer)
class Fish(Animal, Swimmer):
    def make_sound(self):
        return "Blub blub!"

    def swim(self):
        return f"{self.name} is swimming like a fish."

# Abstract Class: Flyer
class Flyer(ABC):
    @abstractmethod
    def fly(self):
        pass

# Concrete Class: Bird (inherits from Animal and Flyer)
class Bird(Animal, Flyer):
    def make_sound(self):
        return "Tweet tweet!"

    def fly(self):
        return f"{self.name} is flying like a bird."

# Concrete Class: Bat (inherits from Animal, Swimmer, and Flyer)
class Bat(Animal, Swimmer, Flyer):
    def make_sound(self):
        return "Squeak squeak!"

    def swim(self):
        return f"{self.name} is swimming upside down like a bat."

    def fly(self):
        return f"{self.name} is flying like a bat."

# Creating instances of concrete classes
goldfish = Fish(name="Goldie")
robin = Bird(name="Robin")
fruit_bat = Bat(name="Fruity")

# Displaying information about animals with multiple inheritance
print(goldfish.make_sound())
print(goldfish.swim())

print("\n")

print(robin.make_sound())
print(robin.fly())

print("\n")

print(fruit_bat.make_sound())
print(fruit_bat.swim())
print(fruit_bat.fly())
