"""
Question 11
Question
Write a program which accepts a sequence of comma separated 4 digit binary numbers
as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:

0100,0011,1010,1001

Then the output should be:

1010

Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

# check function returns true if divisible by 5
def check(x):
    # int(x,b) takes x as string and b as base from which
    # it will be converted to decimal
    return int(x,2) % 5 == 0

data = input().split(',')

# in filter(func,object) function, elements are picked from 'data' if found True by 'check' function
data = list(filter(check, data))

print(",".join(data))
