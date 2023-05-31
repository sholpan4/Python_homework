#task7
user_in = input("Enter your year of bith:")
year = int(user_in)

user_in = input("Enter your bith month:")
month = int(user_in)

user_in = input("Enter your date of bith:")
date = int(user_in)

print(date, month, year, sep=".")

# VN: Формат "дд.мм.гггг" предполагает, что если пользователь введёт 2010, 3, 3, то вывести надо "03.03.2010"
# Ваша программа выводит не так. Это можно поправить, используя шаблон и оператор подстановки %
