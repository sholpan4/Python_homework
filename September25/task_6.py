import datetime
# Форматирование даты и времени
now = datetime.datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)
#works