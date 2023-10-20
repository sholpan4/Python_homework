import datetime
birthday = datetime.date(1990, 5, 15)
today = datetime.date.today()
age = today.year - birthday.year - \
((today.month, today.day) < (birthday.month, birthday.day))
print("Возраст:"
, age)
