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

word = input()
letter, digit = 0, 0

for i in word:
    if ('a' <= i and i <= 'z') or ('A' <= i and i <= 'Z'):
        letter += 1
    if '0' <= i and i <= '9':
        digit += 1

print("LETTERS {0}\n‚DIGITS {1}".format(letter, digit))
