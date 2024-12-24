from classes.bank_account.BankAccount import BankAccount


def bankAccounts():
    dave = BankAccount(1000, "Dave")
    john = BankAccount(2000, "John")
    dave.getBallance()
    john.getBallance()

    dave.deposit(500)
    john.deposit(1000)

    dave.withdraw(20000)
