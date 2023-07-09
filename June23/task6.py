#tas6
names = ['Tatyana', 'Alexandr', 'Vasiliy', 'Olessya', 'Alexandr']
cool_fish = []

for i in range(len(names)):
    doubled_names = names.count(names[i])
    if doubled_names >= 2:
        cool_fish.append(names[i])
        
print(cool_fish)