"""
Question 92
Question
Please write a program which accepts a string from
console and print the characters that have even indexes.

Example: If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld

Hints
Use list[::2] to iterate a list by step 2.
"""

s = "H1e2l3l4o5w6o7r8l9d"

ns = ''

for i in range(len(s)):
    if i % 2 == 0:
        ns += s[i]

print(ns)
