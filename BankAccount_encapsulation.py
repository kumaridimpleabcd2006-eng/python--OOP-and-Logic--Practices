
class BankAccount:
    def __init__(self, balance, deposit, withdraw):
        self._balance = balance
        self._deposit = deposit
        self._withdraw = withdraw

    def show_balance(self,amount):
        self._balance = self._balance + amount
        print("Balance:", self._balance)
        
    def show_deposit(self, amount):
        self._deposit += amount
        print("Deposit:", self._deposit)

    def show_withdraw(self, amount):
        if amount <= self._balance:
            self._withdraw = amount
            print("Withdraw:", self._withdraw)
        else:
            print("Insufficient funds")

account = BankAccount(5000, 1000, 6000)
account.show_balance(5000)
account.show_deposit(1000)
account.show_withdraw(6000)
