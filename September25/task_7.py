import datetime
# Разбор строки в дату и время
date_str ="2023-09-01 12:00:00"
parsed = datetime.datetime.strptime(date_str,"%Y-%m-%d %H:%M:%S")
print(parsed)
#какой должен быть результат? у меня результат: 2023-09-01 12:00:00