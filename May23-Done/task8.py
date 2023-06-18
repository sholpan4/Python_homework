#task8
user_in = input("Enter purchase price in $:")
price = int(user_in)

user_in = input("Enter amount of discount in %:")
discount = int(user_in)

result = price - price * discount / 100
template = "You have to pay: $ %.2f"
message = template % result
print(message)