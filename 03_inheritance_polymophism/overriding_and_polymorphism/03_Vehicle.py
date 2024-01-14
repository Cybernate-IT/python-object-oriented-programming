# Demonstrating Polymorphism with Examples

# Parent Class (Base Class)
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        raise NotImplementedError("Subclasses must implement the start_engine method.")

# Subclasses (Derived Classes)
class Car(Vehicle):
    def start_engine(self):
        return f"{self.brand} Car: Engine started."

class Motorcycle(Vehicle):
    def start_engine(self):
        return f"{self.brand} Motorcycle: Engine started."

# Function demonstrating polymorphism
def start_vehicle_engine(vehicle):
    return vehicle.start_engine()

# Creating instances of the classes
honda_civic = Car(brand="Honda Civic")
harley_davidson = Motorcycle(brand="Harley Davidson")

# Demonstrating polymorphism with examples
print("Demonstrating Polymorphism with Examples:")
print(start_vehicle_engine(honda_civic))
print(start_vehicle_engine(harley_davidson))
