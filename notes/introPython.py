###BASIC PYTHON INTRO###

#Python uses .py extension. 

#The basic python print statement is print()
print("Statement") 

#To run a python program we use python 3
  python3 example.py

#Python is a dynamically typed langauge, therefore we do not have to declare
#variable names. Infers type based on inputted data. 

#For comments use """Comment """ for multiline comments. 
"""Lets see if this 
is more effective!"""

#To cast between types use type(data)
  str("76") "Note that string here does not say String but str"




###Conditionals###
#Instead of the && || python uses
and or not

# If statements are in the form of if condition:
if condition:
    # Code to execute if condition is true

#Else if statements are in the form of elif condition:
elif another_condition:
    # Code to execute if the previous condition is false but this one is true

#Else else:
else:
    # Code to execute if all previous conditions are false

"""Make sure to use the : after all conditional and branching statements"""



###Loops###
# For loops are in this format. Similar to that of a for each.
for item in sequence:
    # Code to execute for each item in the sequence
#Note that item name does not matter, just sequence name (Arrayname)

#For loops like how we have seen them before, going 0 to 4.
for i in range(5):
    print(i) # 0, 1, 2, 3, 4
#This creates a list of numbers then loops over them. Good for lists[i]


#While loops are in this format
while condition:
    # Code to execute while the condition is true



###LISTS###
# Lists are similar to arrays but they can contain any type of data
# and they can grow and shrink in size.
  scores[200, 111, 8, 6, 75]

#To add an element to a list, a new piece of data.
  scores.append(199)

#To remove data.
  scores.pop(0) #Such that 0 is the first index like an array.
#pop() returns removed values. 

#To access data
 scores[0] #Access the first indexed element in the list
#Use a negative value to start from the back of the list.

###Dictionaries###
# Dictionaries are a collection of key value pairs, such that the key is a str
# and the value is an int
 scores{ "Nick": 803, "Tyler": 619}

#To access an element of a dictionary
 scores["Nick"] #Will give you 803.

#To add an element to a dictionary
 scores["Ayden"] = 410

#To remove an element
 scores.pop("Ayden")



###Functions### 
# Functions are defined using the def keyword. 
 def add(a, b): 
    return a + b

#Called same as other languages
 print(add(9, 10))



###Modules###
#We can import modules using the import keyword
 import math
 print(math.sqrt(16) #Will give us 4.

#We can give them aliases as well
 import math as m
 print(m.sqrt(16)



###Sorting###
#Python has a builtin list sorting function
 scores.sort() #Sorts the list based on the first number.

#A quick note on the lambda function
 lambda arguments: expression
    #Such that arguments are the input and the expression is what happens. 
    # arguments = (a, b) 
    # expression = a * b
    # Then , a's value, b's value

###Classes###
#Container of functions and values
class Person:
    def __init__(self, name): # __init__ is like the constructor
        self.name = name #Self is a parameter in everything, it is like the this
                         # in java. 

    def greet(self):
        print(f"Hello, {self.name}!")

friend = Person("John") #Construct new person object. 
friend.greet() # Hello, John!



###File Operations###
#To open a file for reading
file = open('example.txt', 'r')

#To open a file for writing, will overwrite everything
file = open('example.txt', 'w')

#To open a file for appending, adds to the end of the file
file = open('example.txt', 'a')

# Read the entire file read()
content = file.read()
print(content)

#To write a string to a file
file.write() 

# Read one line at a time readline()
line = file.readline()
print(line)

# Read all lines into a list readlines()
lines = file.readlines()
print(lines)

file.close()  # Close the file close()

#We can also use with since it keeps everything in scope.
#Open the file for reading, the word we will use for the file is 
#file
with open("file.txt", "r") as file:
    contents = file.read()
    print(contents)

# Reading a file line by line
with open("file.txt", "r") as file:
    for line in file:
        print(line)

# Writing to a file (overwrites existing content)
with open("file.txt", "w") as file:
    file.write("Hello, world!")

# Appending to a file
with open("file.txt", "a") as file:
    file.write("Hello, again!")




###PYTHON DOCUMENTATION###
https://docs.python.org/3/
