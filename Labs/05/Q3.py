class Account:
    def __init__(self):
        self.__account_no = None
        self.__account_bal = None
        self.__security_code = None

    def set_Account(self, account_no, account_bal, security_code):
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code

    def print_account_info(self):
        print("Account Information:")
        print(f"Account Number: {self.__account_no}")
        print(f"Account Balance: {self.__account_bal}")
        print(f"Security Code: {self.__security_code}")


account = Account()
account.set_Account("123456", 50000.0, "4321")
account.print_account_info()