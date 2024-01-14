# Private Attributes
# Getter and Setter Methods

# Class demonstrating private attributes and getter/setter methods
class Employee:
    def __init__(self, name, salary):
        # Private attributes (encapsulated with double leading underscores)
        self.__name = name
        self.__salary = salary

    # Getter methods for encapsulated attributes
    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    # Setter methods for encapsulated attributes (with validation)
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            print("Invalid name. Name must be a string.")

    def set_salary(self, new_salary):
        if isinstance(new_salary, (int, float)) and new_salary >= 0:
            self.__salary = new_salary
        else:
            print("Invalid salary. Salary must be a non-negative number.")

    # Method to display employee details
    def display_employee_details(self):
        print(f"Name: {self.__name}")
        print(f"Salary: ${self.__salary}")

# Creating an instance of the class
employee1 = Employee(name="John Doe", salary=50000.0)

# Demonstrating private attributes and getter/setter methods
print("Private Attributes and Getter/Setter Methods:")
# Attempting to access private attributes directly (without using getters)
# Note: This is not recommended in practice, but done here for demonstration purposes.
print(f"Name (Direct Access): {employee1._Employee__name}")
print(f"Salary (Direct Access): ${employee1._Employee__salary}")

# Accessing private attributes using getters
print("\nAccessing Private Attributes Using Getters:")
print(f"Name (Using Getter): {employee1.get_name()}")
print(f"Salary (Using Getter): ${employee1.get_salary()}")

# Using setter methods to modify private attributes
print("\nModifying Private Attributes Using Setters:")
employee1.set_name(new_name="Jane Doe")
employee1.set_salary(new_salary=60000.0)

# Displaying updated employee details
print("\nUpdated Employee Details:")
employee1.display_employee_details()
