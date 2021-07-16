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

"""
Solution by: saxenaharsh24
"""
def even(item):
    if item % 2 == 0:
        return item ** 2
    
lst = [i for i in range(1, 11)]

print(  list(filter(lambda j: j is not None, list(map(even, lst)))))
