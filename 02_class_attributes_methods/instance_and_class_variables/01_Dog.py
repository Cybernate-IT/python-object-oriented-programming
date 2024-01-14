# Introduction to Instance and Class Variables

# Class definition
class Dog:
    # Class variable
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
        self.is_hungry = True  # Instance variable

    # Method to display information
    def display_info(self):
        print(f"{self.name} is {self.age} years old.")
        print(f"Species: {self.species}")
        print(f"Hungry: {'Yes' if self.is_hungry else 'No'}")

# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 2)

# Displaying information about the dogs
print("Dog 1 Information:")
dog1.display_info()

print("\nDog 2 Information:")
dog2.display_info()

# Modifying instance variables
dog1.is_hungry = False

# Displaying updated information
print("\nUpdated Dog 1 Information:")
dog1.display_info()
