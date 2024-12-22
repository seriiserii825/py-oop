class Employee:
    def __init__(self, first_name: str, last_name: str, pay: int) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._pay = pay
        self._email = f"{first_name}.{last_name}@company.com"

    def fullname(self)-> str:
        return f"{self._first_name} {self._last_name}"
