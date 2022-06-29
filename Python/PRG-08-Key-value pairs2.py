
# storing the user input in it's respective variable
a = input("Enter your first name : ")
b = input("Enter your last name : ")
c = input("Enter your job title ; ")
d = input("Enter your company name : ")

# Creating an empty user information dictionary.
userinfodict = {}

# adding 4 items to the dictionary created by using the update() method.
userinfodict.update({"firstname" : a})
userinfodict.update({"lastname" : b})
userinfodict.update({"jobtitle" : c})
userinfodict.update({"company" : d})

# using for loop to print the kay-value pairs in the dictionary 
for key in userinfodict:
    print(key,":", userinfodict[key])

# writing the contents of the dictionary into the csv file. 
# opening the file in append mode, "a", so that we dont overwrite the existing information in the file.
with open('test.csv', 'a') as f:
    for key in userinfodict.keys():
        f.write("%s,%s\n"%(key,userinfodict[key]))