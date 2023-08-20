# Сортировка выборкой
#select_sort
user_in = input("Введите числа через запятую: ")
user_in = user_in.split(',')
my_list = list(map(lambda x: int(x), user_in))

def select_sort(num_list, key = None):
    for n in range(len(num_list)):
        min_index = n
        for i in range(n + 1, len(num_list)):
            if num_list[i] < num_list[min_index]:
                min_index = i
        num_list[n], num_list[min_index] = num_list[min_index], num_list[n]
    return num_list

print(select_sort(my_list))