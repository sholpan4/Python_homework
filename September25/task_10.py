#1. Сроки и дни: Напишите программу для расчета даты через
#определенное количество дней, недель и месяцев.

import datetime
from dateutil.relativedelta import relativedelta 


current_date = datetime.date.today()
days_to_add = 7
weeks_to_add = 2
months_to_add = 3

new_date = current_date + datetime.timedelta(days=days_to_add)
new_date_weeks = current_date + datetime.timedelta(weeks=weeks_to_add)

new_date_months = current_date + relativedelta(months=months_to_add)

print(f"Current date: {current_date}")
print(f"Date after {days_to_add}: {new_date}")
print(f"Date after {weeks_to_add}: {new_date_weeks}")
print(f"Date after {months_to_add}: {new_date_months}")