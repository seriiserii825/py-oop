from classes.bank_account.BankAccount import BankAccount


class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.initial_amount += amount * 1.05
        print(f"🤑 Deposit of ${amount:.2f} complete")
        self.getBallance()
