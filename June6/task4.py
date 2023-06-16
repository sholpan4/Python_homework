
import random

def get_random_int(min, max):
    
    result = random.random() * (max - min) + min

    return int(result)

print("Let's play game. You have to guess the number with 7 attempts. Good luck!")


def game():
    
    user_in = input("Your number from 0 tll 100:")
    counter = 7
   
    try:
        num = int(user_in)
    except ValueError:
        print("Enter only number!")
        game()
    
    if my_random > num:
        counter -= 1
        print("Take bigger. You have %d attempts left." % counter)
        game()
    elif my_random < num:
        counter -= 1
        print("Take smaller. You have %d attempts left." % counter)
        game()
    elif counter == 0:
        print("You lose! The number was %d" % random)
    else:
        print("Congratulation! You have won with %d attemts. The number is %d" % (counter, my_random))
        return

my_random = get_random_int (0, 100)
game()