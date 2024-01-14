# Understanding Method Overriding
# Overriding Methods in Subclasses

# Parent Class (Base Class)
class Animal:
    def make_sound(self):
        print("Some generic animal sound.")

# Subclass (Derived Class)
class Dog(Animal):
    # Overriding the make_sound method in the subclass
    def make_sound(self):
        print("Woof! Woof!")

# Subclass with additional method
class Cat(Animal):
    # Overriding the make_sound method in the subclass
    def make_sound(self):
        print("Meow!")

    # Additional method specific to the Cat subclass
    def purr(self):
        print("Purrrrr...")

# Creating instances of the classes
generic_animal = Animal()
golden_retriever = Dog()
persian_cat = Cat()

# Making sounds
print("Generic Animal Sound:")
generic_animal.make_sound()

print("\nDog Sound:")
golden_retriever.make_sound()

print("\nCat Sound:")
persian_cat.make_sound()

# Accessing additional method in the Cat subclass
persian_cat.purr()
