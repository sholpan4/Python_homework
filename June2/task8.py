
    
sec = 1000
counter = 0

while sec > 60:
    minute = sec - 60
    counter += 1
    print(sec)

print(" %02d:%02d:" % minute, counter)

