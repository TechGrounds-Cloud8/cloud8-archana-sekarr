
# Number guessing game

# importing the random module
import random

# generating a random number between 0 and 10 and assigning it to the variable y.
y = random.randint(0,10)
x = -1

# assigning a condition for the while loop
while x != y:

# using try-except block to handle exceptions (in this case, when the user is not entering an integer).
   try:
        x = int(input("Guess a number between 0 and 10: "))
    
        if x > y:
            print("Wow,", x, "is a big number!")
        elif x < y:
            print(x, "is pretty low, think bigger!")
        else:
            print(x, "yeah!!! you guessed the right number!!") 
    
    # if input isn't an integer; using except to specify for which error, the exception is applicable.
   except ValueError:
        print("This isn't a number.")
    