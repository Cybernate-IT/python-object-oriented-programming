# Adding Additional Attributes to the Subclass
# Overriding Methods in the Subclass
# Accessing the Parent Class from the Subclass

# Parent Class (Base Class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic animal sound.")

# Subclass (Derived Class)
class Dog(Animal):
    def __init__(self, name, breed, color):
        # Calling the constructor of the parent class using super()
        super().__init__(name, species="Dog")
        self.breed = breed
        self.color = color

    # Overriding the make_sound method
    def make_sound(self):
        print("Woof! Woof!")

    # Additional method specific to the Dog subclass
    def wag_tail(self):
        print(f"{self.name} is wagging its tail.")

# Creating instances of the classes
generic_animal = Animal("Generic", "Unknown")
golden_retriever = Dog("Buddy", "Golden Retriever", "Golden")

# Displaying information and making sounds
print("Generic Animal Information:")
print(f"Name: {generic_animal.name}")
print(f"Species: {generic_animal.species}")
generic_animal.make_sound()

print("\nDog Information:")
print(f"Name: {golden_retriever.name}")
print(f"Species: {golden_retriever.species}")
print(f"Breed: {golden_retriever.breed}")
print(f"Color: {golden_retriever.color}")
golden_retriever.make_sound()

# Accessing the parent class method from the subclass
golden_retriever.wag_tail()
