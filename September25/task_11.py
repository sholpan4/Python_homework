#2. Логирование с временем: Создайте функцию-декоратор,
#которая добавляет временную метку к логам функций.

import logging

logging.basicConfig(level=logging.INFO)

def log_time(func):
    def wrapper(*args, **kwargs):
        star_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = 