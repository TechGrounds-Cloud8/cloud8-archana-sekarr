
# Using the input function to ask the user for their name.
name = input("What is your name? : ")

# By using conditions; if they input your name, print a personalized welcome message, else print a different message to send them away.
if name == "Archana":
    print("Welcome to our portal " + name)
else:
    print("You are", name, "not Archana, so go away")