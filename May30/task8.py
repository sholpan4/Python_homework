#task8
print("Mini test. Choose answer 1, 2 or 3.")

print("""Question 1. The capital of Grade Britain?
      1. Edinburgh
      2. Paris
      3. London
      """)
answer = int(input("Your answer is:"))

if answer == 1:
    result = 0
    message = "Wrong answer!"
elif answer == 2:
    result = 0
    message = "Wrong answer!"
elif answer == 3:
    result = 2
    message = "Right!"
else:
    message = "Please choose from 1 to 3!"
template1 = int(result)
print(message)
    
print("""Question 2. The biggest animal in the world?
      1. Elephant
      2. Blue Whale
      3. Giraffe
      """)
answer = int(input("Your answer is:"))

if answer == 1:
    result = 0
    message = "Wrong answer!"
elif answer == 2:
    result = 2
    message = "Right!"
elif answer == 3:
    result = 0
    message = "Wrong answer!"
else:
    message = "Please choose from 1 to 3!"
template2 = int(result)
print(message)
    
print("""Question 3. The biggest planet of solar system?
      1. Jupiter
      2. Saturn
      3. Mars
      """)
answer = int(input("Your answer is:"))

if answer == 1:
    result = 2
    message = "Right!"
elif answer == 2:
    result = 0
    message = "Wrong answer!"
elif answer == 3:
    result = 0
    message = "Wrong answer!"
else:
    message = "Please choose from 1 to 3!"
template3 = int(result)
print(message)

scoure = int(template1 + template2 + template3)
print("Your scour is: %d points." % scoure)