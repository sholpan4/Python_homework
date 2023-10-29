import sys
import re

#VN: смотрим внимательно текст дз: `python mailvalidator.py list.txt`
# то есть, имя файла - первый аргумент вызова:
# filename = sys.argv[1]
# with open(filename) as ...
with open('list.txt', 'r') as data_file:
    data = data_file.read().split()

pattern = r"\w[\w\.-_]+\w@\w[\w\.-_]+\.[a-zA-Z]{2,3}"
for email in data:
    matched = re.search(pattern, email)
    #VN:      ^^^^^^^^^ здесь нужна функция re.match(), и тогда дальше будет всё верно
    # Вариант 1
    # if not matched: 
    #     print("Некорректный адрес: ", email)

    # Вариант 2
    if matched:
        data[data.index(email)] = ''

data = list(filter(lambda x: x != '', data))
print(*data, sep="\n")
