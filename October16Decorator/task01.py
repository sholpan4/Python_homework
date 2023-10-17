#Задание 1
#Напишите декоратор `@measuretime`, который будет измерять время работы функции в мс и выводить в консоль в формате: "some_function() - XX мс".
#Продемонстрируйте его работу.

import time

def measuretime(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        result = function(*args)
        print(time.perf_counter_ns() - start_time)
        return result
    return wrapped

@measuretime
def func(first, second):
    return bin(int(first, 2) + int(second, 2))


print(func("111", "0000"))