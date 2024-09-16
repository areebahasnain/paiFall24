class Account:
    def __init__(self):
        self.__account_no = None
        self.__account_bal = None
        self.__security_code = None

    def initialize(self, account_no, account_bal, security_code):
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code

    def display(self):
        print("Account Number:", self.__account_no)
        print("Account Balance:", self.__account_bal)
        print("Security Code:", self.__security_code)


account = Account()
account.initialize("1234567890", 1000.0, "1234")
account.display()