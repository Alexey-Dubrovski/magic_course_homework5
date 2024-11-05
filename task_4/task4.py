#   В файле employees.csv содержится список сотрудников
# с полями: имя, возраст, должность, зарплата.
# Напишите программу, которая считывает данные
# и выводит только тех сотрудников,
# у которых зарплата больше 50,000.

import os
import csv

os.chdir("task_4")

with open("employees.csv", "r", encoding = "utf-8") as file:
    list_pers = csv.DictReader(file)
    low_lim = 50000
    for i in list_pers:
        if int(i["salary"]) > low_lim:
            print(*i.values(), sep = ' - ')