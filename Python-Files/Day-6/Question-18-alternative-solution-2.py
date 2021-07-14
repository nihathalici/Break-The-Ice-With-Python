"""
Question 18
Question:
A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12

Your program should accept a sequence of comma separated passwords
and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.

Example

If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345

Then, the output of the program should be:

ABd1234@1

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

import re

s = input().split(',')
lst = []

for i in s:
    cnt = 0
    cnt += (6 <= len(i) and len(i) <= 12)
    # here re module includes a function re.search() which returns the object information
    cnt += bool(re.search("[a-z]", i))
    # of where the pattern string i is matched with any of the [a-z]/[A-z]/[0=9]/[@#$] characters
    cnt += bool(re.search("[A-Z]", i))
    # if not a single match found then returns NONE which converts to False in boolean
    cnt += bool(re.search("[0-9]", i))
    # expression otherwise True if found any.
    cnt += bool(re.search("[@#$]", i))
    if cnt == 5:
        lst.append(i)

print(",".join(lst))
    













