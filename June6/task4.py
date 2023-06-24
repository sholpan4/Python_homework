#task4
import random
def get_random_int(min, max):
    result = random.random() * (max - min) + min
    return int(result)

print("Let's play game. You have to guess the number with 7 attempts. Good luck!")


def game(get_random_int, counter): 
    user_in = input("Your number from 0 tll 100:")
    
    try:
        num = int(user_in)
    except ValueError:
        print("Enter only number!")
        game(get_random_int, counter)

    if counter == 0:
        print("You lose! You have use all 7 attempts.")
        return
        
    if my_random > num:
        counter -= 1 != 0
        print("Take bigger. Left %d attempts." % counter)
        game(get_random_int, counter)
    elif my_random < num: 
        counter -= 1 != 0   
        print("Take smaller. Left %d attempts." % counter)
        game(get_random_int, counter)
    
    else:
        print("Congratulation! The random number was %d." % my_random)
        return

my_random = get_random_int (0, 100)
game(get_random_int, 7)

answer = input("Would you like to play once more?")
if answer == "yes" or answer == "да":
    game(get_random_int, 7)