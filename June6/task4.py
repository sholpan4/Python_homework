
import random

def get_random_int(min, max):
    
    result = random.random() * (max - min) + min

    return int(result)

print("Let's play game. You have to guess the number with 7 attempts. Good luck!")

i = 0
def game(num, attemts = 7):
    num = input("Your number from 0 tll 100:")

    try:
        num = int(num)
    except ValueError:
        print("Enter only number!")
        game(num)

    if my_random > num:
        attemts -= 1
        print("Take bigger. %d attemts" % attemts) 
        game(num)
    elif my_random < num:
        attemts -= 1
        print("Take smaller. %d attemts" % attemts)    
        game(num)
    else:
        attemts -= 1
        print("Congratulation! You have won. The number is %d." % my_random)
    if attemts == 0:
        print("You lose!")

my_random = get_random_int (0, 100)
game()