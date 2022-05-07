# Comment
"""
Multi line Comment 
"""
# Print
print("Hello Python!")

# ask the users
# input("Name:")
# Store it in a variable (! always store a string )
name = input("Name:")

# With int turn the result of the function input into an int
number = int(input("number:"))

# ? Concatenation
# print("HEllo, " + name)
# Other Way to concatenate width f for format String
print(f"Hello, {name}")

# if elif else (the indentation show what's inside the if elif )
n = 1
if n > 0:  # !don't forget the :
    print("Greater than 0")
elif n < 1:
    print("elif")
else:
    print("Else")


# ? Array
# list : array that can change
# tuple : array that cannot change
# set : array with unique values
# dict : pair of key and value S (dictionnary word and def )
name = "Python"
# Print only the first element (H)
print(f"The first letter of the word Python is ? {name[0]}")
# same for array
snakes = ["Python", "Anaconda", "Black Mamba"]
print(snakes[0])  # Print only the first element (Python)

# Add element on array
snakes.append("Basilic")
# Order the array
snakes.sort()

# create a set
s = set()

# add elements to set
s.add("What a what to add")
s.add(2)

# remove element
s.remove(2)
# ignore the ellement in double (only the second one)

# length of s
len(s)

# TODO Array for number maybe tuple
coordinate = (10.0, 20.0)

# dictionaries (object)
languages = {"Python": "Back-end", "Javascript": "Front-end"}
print(languages["Python"])
# add in a dictionaries
languages["C"] = "Back-end"
print(languages["C"])

# * Loop
# 2 types of for
for i in [0, 1, 2, 3, 4, 5]:  # print 6
    print(f"First Loop {i}")
for i in range(6):  # print 6
    print(f"Second Loop {i}")


# Single string for test character
walterWhiter = "Heisenberg"

# For each
for snake in snakes:
    print(f"Loop on an array : {snake}")
# Work with character but only for one element on the variable
for character in walterWhiter:
    print(f"Loop character :{character}")


# * function

# return the square of a number
def squares(x):  # juste need to add a , if I want to use multiple input
    # still indentation to significate that I'am inside
    return x * x


# * how to import function
# from nameOfTheFile import nameOfTheFunction (to import a single function)
# from nameOfTheFile (to import all the function in the file) but need to specify after
# print(f"The square of {i} is {nameOfTheFile.nameOfTheFunction(i)}")

#  * Classes (template for object)
