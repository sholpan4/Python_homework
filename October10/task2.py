# Задание 2
# =========
# Напишите программу, которая будет извлекать title страницы и все заголовки из html-файла.
# Пример работы программы:
# ```
# > python hextractor.py index.html
# Учебник по программированию
# Введение
# Глава 1. Что такое язык программирования
#  - Компиляторы
#  - Интерпретаторы
# Глава 2. Переменные
# ...





#not sure((

import sys
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    print("Using: python hextraactor.py filename.html")
    sys.exit(1)

html_file = sys.argv[1]

try:
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.find('title')
        if title:
            print(title.text)
        headers = soup.find_all(['h1, h2, h3, h4, h5, h6'])
        for header in headers:
           print(header.text)
except FileNotFoundError:
    print(f"File '{html_file} not found")
except Exception as e:
    print(f"Error: {str(e)}")