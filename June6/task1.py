#task1
# a = "😎"
# num = input("How many times to repeat?")
# #while num > 0:
# result = a * num
# print(result)
#     #a = a+1
# print("The end!")

# user_in = input("enter text:")
# num = "😎"
# result = user_in * num
# print(result)

def recur(num):
    
    if num < 0:  
        return

    recur(num-1)
    print(num)

recur(4)