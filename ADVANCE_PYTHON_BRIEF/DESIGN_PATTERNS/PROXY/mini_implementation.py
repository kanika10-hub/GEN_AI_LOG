class BankAccount:

    def withdraw(self):
        print("Withdrawal Successful")


class BankProxy:

    def __init__(self, authenticated):
        self.authenticated = authenticated
        self.account = BankAccount()

    def withdraw(self):

        if not self.authenticated:
            print("Access Denied")
            return

        self.account.withdraw()


user = BankProxy(True)

user.withdraw()
