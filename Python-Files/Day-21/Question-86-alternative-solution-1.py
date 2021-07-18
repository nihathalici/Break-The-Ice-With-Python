"""
Question 86
Question
By using list comprehension, please write a program to print
the list after removing the value 24 in [12,24,35,24,88,120,155].

Hints
Use list's remove method to delete a value.
"""

li = [12, 24, 35, 24, 88, 120, 155]

# this will remove only the first occurrence of 24
li.remove(24)

print(li)
