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

''' Solution by: popomaticbubble
'''
import re

input_string = input('> ')
print()
counter = { "LETTERS":len(re.findall("[a-zA-Z]", input_string)), "NUMBERS": len(re.findall("[0-9]", input_string))}

print(counter)
