# Сортировка выборкой
#select_sort
user_in = input("Введите числа через запятую: ")
user_in = user_in.split(',')
my_list = list(map(lambda x: int(x), user_in))

sorted_list = []
for _ in range(len(my_list)):
    # min_elem = min(my_list)
    # sorted_list.append(min_elem)
    # del my_list[my_list.index(min_elem)]
    min_index = 0
    for k in range(1, len(my_list)):
        if my_list[k] < my_list[min_index]:
            min_index = k
    sorted_list.append(my_list[min_index])
    del my_list[min_index]


my_list = sorted_list
print(my_list)
