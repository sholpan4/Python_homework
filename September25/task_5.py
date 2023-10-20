import datetime
# Создание интервала времени
delta = datetime.timedelta(days=7, hours=3)
print(delta)
# Вычисление новой даты
new_date = datetime.datetime.now() + delta
print(new_date)
#works