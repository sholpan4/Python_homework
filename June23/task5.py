#task5
my_list = [3, 9, 8, 4, 5, 1]

list_max = max(my_list)
list_min = min(my_list)

a = my_list.index(list_max)
b = my_list.index(list_min)

if a < b:
    result = b - a
else:
    result = a - b

print(result)