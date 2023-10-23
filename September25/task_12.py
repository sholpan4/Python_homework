#. Зависимость от времени: Разработайте функцию, которая
#выполняет разные действия в зависимости от времени суток.

import datetime

def actions_by_time():
    current_time = datetime.datetime.now().time()
    if current_time < datetime.time(12, 0):
        #VN: и я увидел это сейчас, в 00:50 :))
        print("Good morning!")
    elif current_time < datetime.time(17, 0):
        print("Good day!")
    else:
        print("Good evening!")

actions_by_time()