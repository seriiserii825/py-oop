# Задача 13
# Импортируйте модуль pprint. Используя метод
# модуля pprint, напечатайте mappingproxy
# класса кортежей.
# Задача 14
# В классе среди школьников есть пять
# мальчиков, возраст которых 15 лет. У
# четверых одинаковый рост - 160 см. у пятого
# рост - 165 см. Смоделируйте данную систему,
# заполните список из смоделированных
# экземпляров.
# Один из мальчиков решил уйти из данного
# класса, сделайте так, чтобы программная
# система исключила данный объект.

import pprint
import random

ctuple = ('some', 1, 18)

cobj = {
        "age": 2,
        "name": 'some'
        }

pprint.pprint(ctuple)
pprint.pprint(cobj)

class Student:
    age: int = 15
    height: int = 160

students = [Student() for _ in range(5)]
students_height = [students[index].height for index in range(5)]
print(f"students_height: {students_height}")
students[4].height = 165
index = random.randint(0, 4)
del students[index]
print(f'len(students): {len(students)}')

pprint.pprint(students)
