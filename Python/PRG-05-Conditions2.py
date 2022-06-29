from multiprocessing.sharedctypes import Value
from tkinter import Variable


# Assigning a value to the variable
x = 0

# assigning a condition for the while loop
while x != 100:

# using try-except block to handle exceptions (in this case, when the user is not entering an integer).
   try:
        x = int(input("Please input a number: "))
    
        if x > 100:
            print("Wow,", x, "is a big number!")
        elif x < 100:
            print(x, "is pretty low, isn't it?")
        else:
            print(x, "is a nice number indeed.") 
    
    # if input isn't an integer; using except to specify for which error, the exception is applicable.
   except ValueError:
        print("This isn't a number.")
    

       