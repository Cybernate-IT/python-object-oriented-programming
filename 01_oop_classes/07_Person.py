# Instantiating Objects from Classes

# Class definition
class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def introduce(self):
        print(f"Hi, I'm {self.name}. I'm {self.age} years old, and I work as a {self.occupation}.")

# Instantiating objects
person1 = Person("Alice", 25, "Software Engineer")
person2 = Person("Bob", 30, "Data Scientist")

# Accessing object attributes and methods
person1.introduce()
person2.introduce()
