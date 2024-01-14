# Introduction to Inheritance
# Defining a Subclass in Python
# Inheriting Attributes from the Parent Class

# Parent Class (Base Class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic animal sound.")

# Subclass (Derived Class)
class Dog(Animal):
    def __init__(self, name, breed):
        # Calling the constructor of the parent class using super()
        super().__init__(name, species="Dog")
        self.breed = breed

    # Overriding the make_sound method
    def make_sound(self):
        print("Woof! Woof!")

# Creating instances of the classes
generic_animal = Animal("Generic", "Unknown")
golden_retriever = Dog("Buddy", "Golden Retriever")

# Displaying information and making sounds
print("Generic Animal Information:")
print(f"Name: {generic_animal.name}")
print(f"Species: {generic_animal.species}")
generic_animal.make_sound()

print("\nDog Information:")
print(f"Name: {golden_retriever.name}")
print(f"Species: {golden_retriever.species}")
print(f"Breed: {golden_retriever.breed}")
golden_retriever.make_sound()
