#task6
user_in = input("Enter the cost of purchase:")
cost = float(user_in)

if cost < 200:
    print("There is no discount.")
    result = cost
    template = "Total amount to pay: $ %.2f" 
    message = template % result
elif 200 <= cost <= 300:
    print("The discount is 3%.")
    result = float(cost - cost * 0.03)
    template = "Total amount to pay: $ %.2f"
    message = template % result
elif 300 <= cost <= 500:
    print("The discount is 5%.")
    result = float(cost - cost * 0.05)
    template = "Total amount to pay: $ %.2f"
    message = template % result
elif cost >= 500: 
    print("The discount is 7%.")
    result = float(cost - cost * 0.07)
    template = "Total amount to pay: $ %.2f"
    message = template % result
else:
    message = "Please enter a number!"
    
print(message)