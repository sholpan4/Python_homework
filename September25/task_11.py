#2. Логирование с временем: Создайте функцию-декоратор,
#которая добавляет временную метку к логам функций.
<<<<<<< HEAD
import logging
import functools
import time

logging.basicConfig(level=logging.INFO)
def log_with_timestamp(func):
    @functools.wraps(func)
    def wrapper(*args, ** kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_timee = end_time -start_time
        logging.info(f"{func.__name__} done in {elapsed_timee: .4f} seconds")
        return result
    return wrapper

@log_with_timestamp
def exm_function():
    for _ in range(10000000):
        pass

exm_function()
