# Система учета заказов

# У вас есть JSON-файл orders.json,
# содержащий данные о заказах интернет-магазина.
# Каждый заказ включает информацию о клиенте,
# заказанных товарах, количестве и цене.

# Напишите программу, которая:
# Выводит общую сумму каждого заказа.
# Находит клиента с наибольшей суммой заказа и выводит его имя и сумму.

import json
import os

os.chdir("task_5")

with open("orders.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    
    orders = data["orders"]
    order_sum_lst = []

    for order in orders:
        order_sum = 0

        for item in order["items"]:
            order_sum += item["quantity"] * item["price"]
        order_sum_lst.append(order_sum)
        print(f'Сумма заказа: {order_sum}')

    max_order = max(order_sum_lst)
    index_max_order = order_sum_lst.index(max_order)
    best_sell = orders[index_max_order]
    print(best_sell["customer"]["name"], max(order_sum_lst))
