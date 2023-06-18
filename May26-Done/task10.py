#task10
user_in = input("Введите общую сумму продаж за месяц: ")
try:
      num = int(user_in)
      #$250 salary
except ValueError:
    message = "Error! You have entered not number!"
else:
      num1 = num * 10 / 100
      num2 = num1 + 250

      print("""
            Оклад: $ 250
            Бонусы: $""", num1,)
      message = print("Ваша зарплата вместе с бонусом составила: $", num2)
      
print(message)
