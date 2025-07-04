class Employee:
    num_of_employees: int = 0
    rais_amount: float = 1.04

    def __init__(self, first_name: str, last_name: str, pay: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name}.{last_name}@company.com"
        Employee.num_of_employees += 1

    def fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def applayRaise(self):
        self.pay = self.pay * self.rais_amount

    # raise amount for all instance at once
    @classmethod
    def raiseAmount(cls, amount: int):
        cls.rais_amount = amount

    # alternative constructor to create new instance
    @classmethod
    def fromString(cls, employee_string: str):
        first, last, pay = employee_string.split("-")
        # convert pay to integer
        pay_int = int(pay)
        return cls(first, last, pay_int)

    @staticmethod
    def isWorkDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
