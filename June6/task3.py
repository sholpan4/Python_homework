#task3
list_a = [0,1,2,3,4,5,6,7,8,9,10]
list_b = [2,3,4,5,6,7,8,9,]

for b in list_b:
    for a in list_a:
        result = b * a
        print("%d * %d =" % (b, a), result)