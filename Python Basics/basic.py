# !IMPORTANT
# Split the terminal
# Type py -3.9 in the right terminal to get a python interpretor side by side
# One side compiler and one side interpretor 

# In the interpretor type dir() - to get names of all the functions in that particular class
# dir(list)

# help(classname.functionname) - help(list.append)
# This gives a description of the function

# dir(__builtins__) - To get all the inbuilt functions in python

# to clear windows shell - type clear
# to clear python interpretor - ctrl+l / q

name = input("Enter your name : ")
message = f"Hello {name}"
print(message)

color = list([1,2,3,4,5])
for c in color:
    print(c)