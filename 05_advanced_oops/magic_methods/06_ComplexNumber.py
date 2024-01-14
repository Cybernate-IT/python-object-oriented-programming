class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        # String representation using __str__
        return f"{self.real} + {self.imag}j"

    def __add__(self, other):
        # Overloading the addition operator (+)
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        else:
            raise TypeError("Unsupported operand type for +: ComplexNumber and " + str(type(other)))

    def __sub__(self, other):
        # Overloading the subtraction operator (-)
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        else:
            raise TypeError("Unsupported operand type for -: ComplexNumber and " + str(type(other)))

# Creating instances of ComplexNumber
num1 = ComplexNumber(3, 4)
num2 = ComplexNumber(1, 2)

# Using operator overloading for addition
result_addition = num1 + num2
print("Addition Result:", result_addition)

# Using operator overloading for subtraction
result_subtraction = num1 - num2
print("Subtraction Result:", result_subtraction)
