# from classes.cats.BattleCat import BattleCat
# from classes.cats.Cat import Cat
# from classes.cats.Target import Target
# from modules.cats_functions import catsFunctions
# from modules.simple_cats import cat
#
#
# if __name__ == "__main__":
#     # cat()


from classes.employees.Employee import Employee

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


