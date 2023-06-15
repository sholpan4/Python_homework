#task1
def recur(num):   
    if num < 0:  
        return
    recur(num-1)
    print("😎")

user_in = int(input("How many times print 😎?"))
recur(user_in - 1)