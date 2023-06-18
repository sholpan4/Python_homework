#task5
user_in1 = input("Enter amount in $: ")
user_in2 = input("""Choose the currency:
                       1. EUR
                       2. KZT
                       3. CNY
                       """)
try:
    amount = int(user_in1)
    currency = int(user_in2)
except ValueError:
    amount = ""
    currency = ""

if currency == 1:
    result = amount * 0.93
    message = "%.2f USD is equal to %.2f EUR" % (amount, result)
elif currency == 2:
    result = amount * 450.49
    message = "%.2f USD is equal to %.2f EUR" % (amount, result)
elif currency == 3:
    result = amount * 7.08
    message = "%.2f USD is equal to %.2f EUR" % (amount, result)
else:
    message = "Please enter a number!"

print(message)