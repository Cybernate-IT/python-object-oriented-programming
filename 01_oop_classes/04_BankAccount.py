# Class Attributes

# Class definition
class BankAccount:
    # Class attribute
    interest_rate = 0.02

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def calculate_interest(self):
        # Accessing class attribute
        interest_amount = self.balance * BankAccount.interest_rate
        return interest_amount

# Object instantiation
account1 = BankAccount("123456", 1000)
account2 = BankAccount("789012", 2000)

# Accessing object attributes
print(f"Account 1 Balance: ${account1.balance}")
print(f"Account 2 Balance: ${account2.balance}")

# Accessing class attribute
print(f"Interest Rate: {BankAccount.interest_rate}")

# Calculating interest using class attribute
interest1 = account1.calculate_interest()
interest2 = account2.calculate_interest()

# Displaying results
print(f"Interest on Account 1: ${interest1}")
print(f"Interest on Account 2: ${interest2}")
