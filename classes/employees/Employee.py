class Employee:
    num_of_employees = 0
    rais_amount = 1.04
    def __init__(self, first_name: str, last_name: str, pay: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name}.{last_name}@company.com"
        Employee.num_of_employees += 1

    def fullname(self)-> str:
        return f"{self.first_name} {self.last_name}"

    def applayRaise(self):
        self.pay = self.pay * self.rais_amount
