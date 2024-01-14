# Demonstrating Encapsulation in Python

# Class representing a BankAccount with encapsulated attributes and methods
class BankAccount:
    def __init__(self, account_holder, balance):
        # Private attributes (encapsulated with double leading underscores)
        self.__account_holder = account_holder
        self.__balance = balance

    # Getter methods for encapsulated attributes
    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance

    # Public method for depositing money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit of ${amount} successful. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    # Public method for withdrawing money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0 and not exceed the balance.")

# Creating an instance of the class
account1 = BankAccount(account_holder="Alice", balance=1000.0)

# Demonstrating encapsulation in action
print("Demonstrating Encapsulation in Python:")
# Attempting to access private attributes directly (without using getters)
# Note: This is not recommended in practice, but done here for demonstration purposes.
print(f"Account Holder (Direct Access): {account1._BankAccount__account_holder}")
print(f"Balance (Direct Access): ${account1._BankAccount__balance}")

# Accessing encapsulated attributes using getters
print("\nAccessing Encapsulated Attributes Using Getters:")
print(f"Account Holder (Using Getter): {account1.get_account_holder()}")
print(f"Balance (Using Getter): ${account1.get_balance()}")

# Using public methods for deposit and withdrawal
account1.deposit(500.0)
account1.withdraw(200.0)

# Attempting to access private attributes directly (without using getters)
# Note: This is not recommended in practice, but done here for demonstration purposes.
print("\nAttempting to Access Private Attributes (Direct Access):")
print(f"Account Holder (Direct Access): {account1._BankAccount__account_holder}")
print(f"Balance (Direct Access): ${account1._BankAccount__balance}")
