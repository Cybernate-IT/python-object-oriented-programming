class BankAccount:
    # Class variable to store the total number of accounts
    total_accounts = 0

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        # Incrementing the total number of accounts when a new instance is created
        BankAccount.total_accounts += 1

    @classmethod
    def display_total_accounts(cls):
        # Class method to display the total number of accounts
        print(f"Total number of accounts: {cls.total_accounts}")

    @classmethod
    def create_dummy_account(cls):
        # Class method to create a dummy account with a predefined account number and balance
        dummy_account = cls(account_number="Dummy123", balance=0)
        return dummy_account

# Creating instances of BankAccount
account1 = BankAccount(account_number="A123", balance=1000)
account2 = BankAccount(account_number="B456", balance=2000)

# Displaying the total number of accounts using the class method
BankAccount.display_total_accounts()

# Creating a dummy account using the class method
dummy_account = BankAccount.create_dummy_account()
print(f"Dummy Account Number: {dummy_account.account_number}")
print(f"Dummy Account Balance: {dummy_account.balance}")
