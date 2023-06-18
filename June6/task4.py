
import random

def get_random_int(min, max):
    
    result = random.random() * (max - min) + min

    return int(result)

print("Let's play game. You have to guess the number with 7 attempts. Good luck!")

i = 0
def game():
    user_in = input("Your number from 0 tll 100:")

    try:
        num = int(user_in)
    except ValueError:
        print("Enter only number!")
        game()

    if my_random > num:
        print("Take bigger.") 
        game()
    elif my_random < num:
        print("Take smaller. ")    
        game()
    else:
        print("Congratulation! You have won. The number is %d" % my_random)
        

   
    i += 1
    print(i, "attemts")

my_random = get_random_int (0, 100)
game()