class BankAccount:
    def __init__(self, account_number, customer_name, balance=0.0, date_of_opening=None):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs.{amount:.2f}. New balance: Rs.{self.balance:.2f}.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew Rs.{amount:.2f}. New balance: Rs.{self.balance:.2f}.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid amount.")

    def check_balance(self):
        print(f"Current balance: Rs.{self.balance:.2f}")

account = BankAccount(account_number="123456789", customer_name="Areeba Hasnain", balance=1000.0, date_of_opening="2024-09-01")

account.check_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.check_balance()
account.withdraw(2000.0) # Trying to withdraw more than the balance
