class BankAccount:

    def __init__(self, balance):

        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):

        if (
            amount > 0 and
            amount <= self.__balance
        ):
            self.__balance -= amount


account = BankAccount(1000)

account.deposit(500)

account.withdraw(300)

print(account.get_balance())
