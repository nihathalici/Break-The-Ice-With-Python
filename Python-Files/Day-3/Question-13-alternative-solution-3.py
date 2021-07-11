"""
Question 13
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123

Then, the output should be:

LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

'''Solution by: hajimalung
'''
#using reduce for to count
from functools import reduce

def count_letters_digits(counters, char_to_check):
    counters[0] += char_to_check.isalpha()
    counters[1] += char_to_check.isnumeric()
    return counters

print('LETTERS {0}\nDIGITS {1}'.format(*reduce(count_letters_digits, input(), [0,0])))
