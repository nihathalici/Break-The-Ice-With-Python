"""
Question 42
Question:
Write a program which can map() and filter() to make a list
whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

Hints:
Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.
"""

def even(x):
    return x % 2 == 0

def square(x):
    return x * x

li = [1,2,3,4,5,6,7,8,9,10]

# first filters number by even number and then apply map() on the resultant elements
li = map(square,filter(even, li))

print(list(li))
