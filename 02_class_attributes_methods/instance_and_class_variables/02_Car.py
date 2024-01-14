# Class Variables

# Class definition
class Car:
    # Class variable
    total_cars = 0

    def __init__(self, make, model):
        # Instance variables
        self.make = make
        self.model = model
        # Updating class variable on instance creation
        Car.total_cars += 1

    # Method to display information
    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")

# Creating instances of the Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Mustang")

# Displaying information about the cars
print("Car 1 Information:")
car1.display_info()

print("\nCar 2 Information:")
car2.display_info()

print("\nCar 3 Information:")
car3.display_info()

# Accessing the class variable
print(f"\nTotal Cars Created: {Car.total_cars}")
