"""
Question 80
Question
Please write a program to print the list
after removing even numbers in [5,6,77,45,22,12,24].

Hints
Use list comprehension to delete a bunch of element from a list.
"""
li = [5,6,77,45,22,12,24]

li = [x for x in li if x % 2 != 0]

print(li)
