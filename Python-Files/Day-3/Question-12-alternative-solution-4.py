"""
Question 12
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.The numbers obtained should be printed
in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

'''Solution by: hajimalung
'''
from functools import reduce

#using reduce to check if the number has only even digits or not
def is_even_and(bool_to_compare, num_as_char):
    return int(num_as_char) % 2 == 0 and bool_to_compare

print(*(i for i in range(1000, 3001) if reduce(is_even_and, str(i), True)), sep=',')

