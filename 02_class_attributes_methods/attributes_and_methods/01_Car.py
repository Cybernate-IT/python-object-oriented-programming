# Overview of Attributes and Methods

# Class definition
class Car:
    def __init__(self, make, model, year):
        # Attributes
        self.make = make
        self.model = model
        self.year = year
        self.is_engine_running = False

    # Methods
    def start_engine(self):
        print(f"{self.year} {self.make} {self.model}'s engine is now running.")
        self.is_engine_running = True

    def drive(self):
        if self.is_engine_running:
            print(f"{self.year} {self.make} {self.model} is now moving.")
        else:
            print(f"Start the engine first to drive {self.year} {self.make} {self.model}.")

# Instantiating an object
my_car = Car("Toyota", "Camry", 2022)

# Accessing attributes and calling methods
print(f"{my_car.year} {my_car.make} {my_car.model}")
my_car.start_engine()
my_car.drive()
