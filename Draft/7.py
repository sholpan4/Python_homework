user_in = input("Enter the cost of purchase:")
cost = int(user_in)
#try:
    #cost = int(user_in)
#except ValueError:
    #cost = ""
    #message = "Please enter a number!"
#if type(cost) is int():
if cost < 200:
    result = cost + 1
    template = "There is no discount. Total amount is $ %d" 
    message = template % result
elif 200 < cost < 300:
    result = cost * 0.03
    template = "Discount 3%. Total amount is $ %d" 
    message = template % result
elif 300 <= cost <= 500:
    result = cost * 0.05
    template = "Discount 5%. Total amount is $ %d" 
    message = template % result
elif cost >= 500: # cost > 500:
    result = cost * 0.05
    template = "Discount 7%. Total amount is $ %d" 
    message = template % result
else:
    message = "Please enter a number!"
    
print(message)