#task4
list_1 = [2, 35, 'hello', 'apple', 0, -1243]
list_2 = [24, 'hello', 2, 238]

new_list = list_1.copy()

for i in range(len(new_list)):
    for x in range(len(list_2)):
        if new_list[i] is list_2[x]:
            list_1.remove(list_2[x])
            
print(list_1)