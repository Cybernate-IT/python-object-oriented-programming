# Access Modifiers (Public, Private, Protected)

# Class definition
class BankAccount:
    def __init__(self, account_number, balance):
        # Public attribute
        self.account_number = account_number
        # Protected attribute
        self._balance = balance
        # Private attribute
        self.__pin = "1234"

    # Public method
    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self._balance}")

    # Protected method
    def _withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawal successful. New balance: ${self._balance}")
        else:
            print("Insufficient funds.")

    # Private method
    def __change_pin(self, new_pin):
        self.__pin = new_pin
        print("PIN changed successfully.")

# Creating an instance
account = BankAccount("123456789", 1000)

# Accessing public attributes and methods
account.display_balance()

# Accessing protected attribute and method (not recommended, just for demonstration)
account._withdraw(500)

# Accessing private attribute (not recommended, just for demonstration)
print(f"PIN: {account._BankAccount__pin}")

# Accessing private method (not recommended, just for demonstration)
account._BankAccount__change_pin("5678")
account.display_balance()
