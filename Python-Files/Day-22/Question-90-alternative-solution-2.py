"""
Question 90
Question
Please write a program which count and print the numbers
of each character in a string input by console.

Example: If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

Hints
Use dict to store key/value pairs. Use dict.get() method to lookup a key with default value.
"""

s = input()

# ord() gets the ascii value of a char
for letter in range(ord('a'), ord('z')+1):
    # chr() gets the char of an ascii value
    letter = chr(letter)
    cnt = s.count(letter)
    if cnt > 0:
        print("{}, {}".format(letter, cnt))
