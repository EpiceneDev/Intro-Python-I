# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print(x)

# Using y, 
# change x so that it is [1, 2, 3, 4, 8, 9, 10]
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)
print(x)

# Print the length of list x
print(len(x))

# Print all the values in x multiplied by 1000
print([value * 1000 for value in x])



"""
2 ITERATION WAYS:

Method 1 - for item in list:
for item in list:
  print item
Method 2 - iterate through indexes:
for i in range(len(list)):
  print list[i]
Method 1 is useful to loop through the list, but it’s not possible to modify the list this way.
Method 2 uses indexes to loop through the list, making it possible to also modify the list if needed. 
Lists of lists
list_of_lists = [[1, 2, 3], [4, 5, 6]]
for lst in list_of_lists:
  for item in lst:
    print item
"""