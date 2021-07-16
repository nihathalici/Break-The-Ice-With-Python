"""
Question 43
Question:
Write a program which can filter() to make a list whose elements are
even number between 1 and 20 (both included).

Hints:
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.
"""

def even(x):
    return x % 2 == 0

evenNumbers = filter(even, range(1, 21))

print(list(evenNumbers))
