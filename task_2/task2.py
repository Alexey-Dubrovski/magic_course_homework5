# В файле task2.json хранится список пользователей с полями:
# имя, возраст, город и профессия. Напишите программу,
# которая считывает файл и выводит только тех пользователей,
# которые старше 30 лет и работают в указанной профессии.

import os
import json

os.chdir("task_2")

def filtration(age_pers: int, prof_pers: str):
    with open("task2.json", "r", encoding="utf-8") as file:
        spk = json.load(file)
        for i in spk:
            if i.get('age') > age_pers and i.get('profession') == prof_pers:
                print(i)

age_pers = 30
prof_pers = 'программист'
filtration(age_pers, prof_pers)
