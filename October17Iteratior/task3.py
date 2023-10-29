import random


def random_number_generator(start, end):
    while True:
        yield random.randint(start, end)
        
start_num = 1
end_num = 100

generator = random_number_generator(start_num, end_num)

for _ in range(10):
    random_number = next(generator)
    print(random_number)