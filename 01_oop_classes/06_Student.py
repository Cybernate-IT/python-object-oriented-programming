# Constructors and Destructors

# Class definition
class Student:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Student {self.name} created!")

    # Destructor (not a true destructor, but __del__ is called before object destruction)
    def __del__(self):
        print(f"Student {self.name} is being destroyed!")

# Creating instances
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Accessing object attributes
print(f"{student1.name} is {student1.age} years old.")
print(f"{student2.name} is {student2.age} years old.")

# Deleting an object (calling __del__)
del student1
del student2
