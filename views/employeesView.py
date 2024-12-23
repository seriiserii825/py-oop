from classes.employees.Employee import Employee

def employeesView():
    employee_1 = Employee('Serii', 'Burduja', 30000)
    employee_2 = Employee('Zezik', 'Test', 30000)

    print(employee_1.pay)
    print(employee_1.pay)
    print(Employee.num_of_employees)

    emp_str_1 = 'John-Doe-39999'
    employee_3 = Employee.fromString(emp_str_1)

    import datetime
    my_date = datetime.date(2016, 7, 10)
    print(Employee.isWorkDay(my_date))


# print(f'employee_1.fullname(): {employee_1.fullname()}')
