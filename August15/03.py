# Быстрая сортировка
#quick_sort
user_in = input("Введите числа через запятую: ")
user_in = user_in.split(',')
my_list = list(map(lambda x: int(x), user_in))

def quick_sort(num_list, key = None):
    if len(num_list) <= 1:
        return num_list
    pivot = num_list[0]
    less = list(filter(lambda x:  x < pivot, num_list))
    # less = [x for x in the_list if x < pivot]
    equals = list(filter(lambda x: x == pivot, num_list))
    more = list(filter(lambda x: x > pivot, num_list))
    result = quick_sort(less) + equals + quick_sort(more)
    # return result

    if key:
        new_list = []
        for i in range(len(num_list)):
            if key(num_list[i]):
                new_list.append(num_list[i]) # не получается додумать
    else:
        return num_list

print(quick_sort(my_list, key=lambda x: x ** 2))