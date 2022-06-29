# Creating a list of 5 integers.
intlist = [1, 2, 3, 4, 5]

# Using length function len() - to determine how many items the integers list has and range() function to create an iterable.
# Printing the value of that item added to the value of the next item in the list. If it is the last item, added it to the value of the first item instead (since there is no next item).

for x in range(len(intlist)):
    if x == len(intlist) -1:
        print(intlist[0] + intlist[x])

    else:
        sum = (intlist[x] + intlist[x + 1])
        print(sum)