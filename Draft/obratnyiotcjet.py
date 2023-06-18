n = int(input(" Сколько секунд до старта :"))
if n >= 0 :
    while n >= 0:
        print(" Осталось секунд: " + str(n))
        n -= 1
    print(" Пуск!")
else:
    print(" Пуск!")