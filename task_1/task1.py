# Напишите программу, которая сравнивает два JSON-файла
# (file1.json и file2.json) и выводит различия между ними.
# Программа должна определить, какие ключи или значения отличаются.
# Сравнивать только ключи и значения первого уровня.

import json
import os

os.chdir("task_1")

with open("task1_1.json", "r", encoding="utf-8") as file1:
    file_1 = json.load(file1)

with open("task1_2.json", "r", encoding="utf-8") as file2:
    file_2 = json.load(file2)

if file_1 == file_2:
    print("Они одинаковые")
else:
    keys_1, keys_2 = [], []
    values_1, values_2 = [], []

    for k, v in file_1.items():
        keys_1.append(k)
        values_1.append(v)

    for k, v in file_2.items():
        keys_2.append(k)
        values_2.append(v)
    
    for i in range(len(keys_1)):
        if keys_1[i] != keys_2[i]:
            print(f'Отличаются ключи: {keys_1[i]} и {keys_2[i]}')
        if values_1[i] != values_2[i]:
            print(f'Отличаются значения: {values_1[i]} и {values_2[i]}')