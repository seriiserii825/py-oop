from classes.bank_account.BankAccount import BankAccount
from classes.bank_account.InterestRewardsAccount import InterestRewardsAccount


def bankAccounts():
    dave = BankAccount(1000, "Dave")
    sara = InterestRewardsAccount(500, "Sara")

    sara.getBallance()
    sara.deposit(100)
    sara.transfer(100, dave)
