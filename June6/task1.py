#task1
def recur(num):   
    if num < 0:  
        return
    recur(num-1)
    print("😎")

recur(4)