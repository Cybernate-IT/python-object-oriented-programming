class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self._salary = salary  # Using a private attribute with a single leading underscore

    @property
    def full_name(self):
        # Property to get the full name of the employee
        return f"{self.first_name} {self.last_name}"

    @property
    def salary(self):
        # Property to get the salary
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        # Setter method with validation to update the salary
        if new_salary >= 0:
            self._salary = new_salary
        else:
            print("Salary cannot be negative.")

    @classmethod
    def create_dummy_employee(cls):
        # Class method to create a dummy employee with default values
        return cls(first_name="John", last_name="Doe", salary=50000)

    @staticmethod
    def calculate_bonus(base_salary, bonus_percentage):
        # Static method to calculate bonus based on the base salary and bonus percentage
        return base_salary * (bonus_percentage / 100)

# Creating an instance of Employee
employee = Employee(first_name="Alice", last_name="Smith", salary=60000)

# Accessing properties
print("Full Name:", employee.full_name)
print("Salary:", employee.salary)

# Setting a new salary using the setter method
employee.salary = 65000
print("Updated Salary:", employee.salary)

# Creating a dummy employee using the class method
dummy_employee = Employee.create_dummy_employee()
print("Dummy Employee Full Name:", dummy_employee.full_name)
print("Dummy Employee Salary:", dummy_employee.salary)

# Calculating bonus using the static method
bonus_amount = Employee.calculate_bonus(base_salary=60000, bonus_percentage=10)
print("Bonus Amount:", bonus_amount)
