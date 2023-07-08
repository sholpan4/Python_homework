orders = [
    {'product': 'apple', 'quantity': 500},
    {'product': 'banana', 'quantity': 300},
    {'product': 'apple', 'quantity': 200},
    {'product': 'orange', 'quantity': 400},
    {'product': 'banana', 'quantity': 1000},
]

product_quantity = {}

for order in orders:
    product = order['product'] #для ключей словаря в листе 'продукт' задаем переменную 'продукт'
    quantity = order['quantity'] #для ключей в словаря в листе 'количество' задаем переменную 'количество'
    
    if product in product_quantity: #для продукта в словаре
        product_quantity[product] += quantity #суммируем количество одинаковых продуктов и складываем с словарь
    else:
        product_quantity[product] = quantity #если не встечаем одинаковые продукты, записываем в словарь что есть
        
for product, quantity in product_quantity.items(): #продукт и количество в словаре 'продукт_количество.по паре'
    print(f'{product}: {quantity}') #печатаем словарь