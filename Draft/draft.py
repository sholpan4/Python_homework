user_in = input("Enter the cost of purchase:")
cost = float(user_in)

if 200 <= cost < 300:
    print("The discount is 2%.")
    result = float(cost - cost * 0.02)
    template = "Total amount to pay: $ %.2f"
    message = template % result
else:
    message = "Please enter a number!"
    
print(message)