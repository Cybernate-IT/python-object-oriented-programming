class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self):
        return f"Car('{self.make}', '{self.model}', {self.year})"

# Creating an instance of Car
my_car = Car(make="Toyota", model="Camry", year=2022)

# Using magic methods for string representations
print(str(my_car))  # Calls __str__ method
print(repr(my_car))  # Calls __repr__ method

# Output:
# 2022 Toyota Camry
# Car('Toyota', 'Camry', 2022)
