# Encapsulating Data

# Class demonstrating encapsulation
class Student:
    def __init__(self, name, age):
        # Private attributes (encapsulated with double leading underscores)
        self.__name = name
        self.__age = age

    # Getter methods for encapsulated attributes
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Setter methods for encapsulated attributes (with validation)
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            print("Invalid name. Name must be a string.")

    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age >= 0:
            self.__age = new_age
        else:
            print("Invalid age. Age must be a non-negative integer.")

    # Method to display student details
    def display_student_details(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age} years")

# Creating an instance of the class
student1 = Student(name="Alice", age=20)

# Demonstrating encapsulation of data
print("Encapsulating Data:")
# Attempting to access encapsulated attributes directly (without using getters)
# Note: This is not recommended in practice, but done here for demonstration purposes.
print(f"Name (Direct Access): {student1._Student__name}")
print(f"Age (Direct Access): {student1._Student__age}")

# Accessing encapsulated attributes using getters
print("\nAccessing Encapsulated Data Using Getters:")
print(f"Name (Using Getter): {student1.get_name()}")
print(f"Age (Using Getter): {student1.get_age()}")

# Using setter methods to modify encapsulated data
print("\nModifying Encapsulated Data Using Setters:")
student1.set_name(new_name="Bob")
student1.set_age(new_age=22)

# Displaying updated student details
print("\nUpdated Student Details:")
student1.display_student_details()
