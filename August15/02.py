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
    # return num_list
        continue

    if key:
        new_list = []
        second_list = []
        for i in range(len(num_list)):
            if not key(num_list[i]):
                second_list.append(num_list[i])
            elif key(num_list[i]) is True:
                new_list.append(num_list[i])
            else:
                new_list.append(key(num_list[i]))
        return new_list + second_list
    else:
        return num_list

print(select_sort(my_list))
print(select_sort(my_list, key=lambda x: x ** 2))

# sorted_list = []
# for _ in range(len(my_list)):
#     # min_elem = min(my_list)
#     # sorted_list.append(min_elem)
#     # del my_list[my_list.index(min_elem)]
#     min_index = 0
#     for k in range(1, len(my_list)):
#         if my_list[k] < my_list[min_index]:
#             min_index = k
#     sorted_list.append(my_list[min_index])
#     del my_list[min_index]

# my_list = sorted_list
# print(my_list)