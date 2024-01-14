# Class vs. Instance Variables

# Class definition
class Employee:
    # Class variable
    total_employees = 0

    def __init__(self, name, salary):
        # Instance variables
        self.name = name
        self.salary = salary
        # Updating class variable
        Employee.total_employees += 1

    def display_info(self):
        print(f"Name: {self.name}, Salary: ${self.salary}")

# Instantiating objects
employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)

# Accessing object attributes and class variable
employee1.display_info()
employee2.display_info()

# Accessing class variable
print(f"Total Employees: {Employee.total_employees}")
