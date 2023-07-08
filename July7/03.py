fruits = {'apple': 5, 'banana': 2, 'cherry': 7, 'orange': 3}

result = {k: v for k, v in sorted(fruits.items(), key=lambda item: item[1])}
#k = key, v = value
#выводимый результат который нужно напечатать 'ключ: значение'

#с помощью функции сортед сортируем словарь по паре задавая в качестве ключа
# для сортировки значение(в данном решении указано как item [1] по индексу)
# через lambda 
print(result)