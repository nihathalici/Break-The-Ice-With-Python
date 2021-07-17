"""
Question 83
Question
By using list comprehension, please write a program to print the list
after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

Hints
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.
"""

"""Solution by: saxenaharsh24
"""

lst = [ 12, 24, 35, 70, 88, 120, 155 ]

print([ i for i in lst if lst.index(i) not in range(2, 5) ])
