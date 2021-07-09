"""
Question 2
Question:
Write a program which can compute the factorial of a given numbers.The results should be printed
in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8
Then, the output should be:40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

'''Soltuion by: KruthikaSR
'''

from functools import reduce

def fun(acc, item):
    return acc*item

num = int(input())
print(reduce(fun, range(1, num+1), 1))




















