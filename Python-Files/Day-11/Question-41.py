"""
Question 41
Question:
Write a program which can map() to make a list whose elements
are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints:
Use map() to generate a list.
Use lambda to define anonymous functions.
"""

# No different way of code is written as the requirement is specifically mentioned in problem description

li = [1,2,3,4,5,6,7,8,9,10]

# returns map type object data
squaredNumbers = map(lambda x: x**2, li)

# converting the object into list
print(list(squaredNumbers))
