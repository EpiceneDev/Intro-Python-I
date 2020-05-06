"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []
for value in range(5):
    y.append(value + 1)
print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = []
for value in range(10):
    y.append(value**3)
print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [x.upper() for x in a]
print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
 
""" int type conversion is used because when you use input, the result is a string. 
    In order to do arithmetic on the input value, you need to convert it to integer or float """
y = [i for i in x if int(i) % 2 == 0]
print(y)

'''
from second part of lecture with Tim Roy https://www.youtube.com/watch?v=gLnJg2P4UCg&feature=youtu.be:

'''

# for (idx, el) in enumerate(my_list):
#     print(idx, el)

# numbers = [1, 2, 3, 4, 5]

# squares = [num*num for num in numbers]

# or 

# squares = []


# for num in numbers:
#     squares.append(num * num)

# print(squares)

# --------------------------------------

#halves = [num // 2 for num in numbers] <== // rounds down
# print(halves)

# evens = [num for num in numbers if num%2 == 0]
# print(evens)