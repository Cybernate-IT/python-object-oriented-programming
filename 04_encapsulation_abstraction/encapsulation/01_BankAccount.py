# Understanding Encapsulation
# Importance of Encapsulation in OOP

# Class demonstrating encapsulation
class BankAccount:
    def __init__(self, account_holder, balance):
        self._account_holder = account_holder  # Encapsulated attribute with a single leading underscore
        self._balance = balance  # Encapsulated attribute with a single leading underscore

    # Getter method for account holder
    def get_account_holder(self):
        return self._account_holder

    # Setter method for balance (with validation)
    def set_balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Invalid balance. Balance must be non-negative.")

    # Method to display account details
    def display_account_details(self):
        print(f"Account Holder: {self._account_holder}")
        print(f"Balance: ${self._balance}")

# Creating an instance of the class
account1 = BankAccount(account_holder="John Doe", balance=1000)

# Demonstrating encapsulation and its importance
print("Understanding Encapsulation:")
# Attempting to access encapsulated attributes directly (without using getters)
# Note: This is not recommended in practice, but done here for demonstration purposes.
print(f"Account Holder (Direct Access): {account1._account_holder}")
print(f"Balance (Direct Access): ${account1._balance}")

print("\nImportance of Encapsulation in OOP:")
# Accessing encapsulated attributes using getters and setters
print(f"Account Holder (Using Getter): {account1.get_account_holder()}")
account1.set_balance(new_balance=1500)  # Using setter method with validation
account1.display_account_details()  # Using a method to display account details
