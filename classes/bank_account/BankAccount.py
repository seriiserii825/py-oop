from classes.bank_account.BallanceException import BallanceException


class BankAccount():
    def __init__(self, initial_amount, account_name):
        self.initial_amount = initial_amount
        self.account_name = account_name
        print(f"💁 Account {self.account_name} created with initial amount 💵 ${self.initial_amount:.2f}")

    def getBallance(self):
        print(f"🧔 Account {self.account_name} has 💵 ${self.initial_amount:.2f} left")

    def deposit(self, amount):
        self.initial_amount += amount
        self.getBallance()

    def viableTransaction(self, amount):
        if self.initial_amount >= amount:
            return True
        else:
            raise BallanceException(
                    f"🥵 Sorry, account {self.account_name} has insufficient funds to withdraw ${amount:.2f}"
                    )
    def withdraw(self, amount):
        try:
            if self.viableTransaction(amount):
                self.initial_amount -= amount
                print(f"🤞 Withdrawal of ${amount:.2f} complete")
                self.getBallance()
        except BallanceException as e:
            print(e)
            self.getBallance()
    
    def transfer(self, amount, account):
        try:
            if self.viableTransaction(amount):
                print("\n********** Transfer begins 🚀")
                self.viableTransaction(amount)
                self.withdraw(amount)
                account.deposit(amount)
                print("********** Transfer complete ✅")
        except BallanceException as e:
            print(e)
            print("Transfer failed 🚫")

