class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        # Overloading the equality operator (==)
        return self.age == other.age

    def __ne__(self, other):
        # Overloading the inequality operator (!=)
        return self.age != other.age

    def __lt__(self, other):
        # Overloading the less-than operator (<)
        return self.age < other.age

    def __gt__(self, other):
        # Overloading the greater-than operator (>)
        return self.age > other.age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

# Creating instances of Person
person1 = Person(name="Alice", age=25)
person2 = Person(name="Bob", age=30)

# Using overloaded comparison operators
print(f"{person1} == {person2}: {person1 == person2}")
print(f"{person1} != {person2}: {person1 != person2}")
print(f"{person1} < {person2}: {person1 < person2}")
print(f"{person1} > {person2}: {person1 > person2}")
