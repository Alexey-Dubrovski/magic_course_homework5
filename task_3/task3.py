# Напишите программу, которая считывает данные из
# CSV-файла sales.csv, где содержатся данные о продажах
# (например, дата, товар, количество, цена).
# Программа должна вывести:
# - Общую сумму продаж.
# - Товар с наибольшим числом продаж.

import csv
import os

os.chdir("task_3")

with open("products.csv", "r", encoding="utf-8") as file:
    orders = csv.DictReader(file)
    income_sum = 0
    sellers = {}
    for i in orders:
        income_sum += float(i["quantity"]) * float(i["price"])
        if i["product"] in sellers:
            sellers[i["product"]] += int(i["quantity"])
        else:
            sellers[i["product"]] = int(i["quantity"])
    sorted_list = sorted(sellers.items(), key=lambda item: item[1])
    print(f'Общая выручка: {income_sum},\nСамый продаваемый продукт:', 
          *sorted_list[-1], "штук")