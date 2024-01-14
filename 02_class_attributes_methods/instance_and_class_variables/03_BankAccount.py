# Differences Between Instance and Class Variables
# Use Cases for Instance and Class Variables
# Examples Demonstrating the Use of Instance and Class Variables

# Class definition
class BankAccount:
    # Class variable
    total_accounts = 0

    def __init__(self, account_number, balance):
        # Instance variables
        self.account_number = account_number
        self.balance = balance
        # Updating class variable on instance creation
        BankAccount.total_accounts += 1

    # Instance method to display account information
    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}")

# Creating instances of the BankAccount class
account1 = BankAccount("123456", 1000)
account2 = BankAccount("789012", 2000)

# Displaying information about the accounts
print("Account 1 Information:")
account1.display_info()

print("\nAccount 2 Information:")
account2.display_info()

# Accessing the class variable
print(f"\nTotal Bank Accounts Created: {BankAccount.total_accounts}")

# Modifying instance variables
account1.balance -= 500

# Displaying updated information
print("\nUpdated Account 1 Information:")
account1.display_info()
