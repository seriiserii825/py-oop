import datetime

from classes.employees.Employee import Employee


def employeesView():
    employee_1 = Employee("Serii", "Burduja", 30000)

    print(employee_1.pay)
    print(employee_1.pay)
    print(Employee.num_of_employees)

    my_date = datetime.date(2016, 7, 10)
    print(Employee.isWorkDay(my_date))


# print(f'employee_1.fullname(): {employee_1.fullname()}')
