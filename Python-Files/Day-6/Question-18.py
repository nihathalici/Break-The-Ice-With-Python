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

# Returns True  if the string has a lowercase
def is_low(x):
    for i in x:
        if 'a' <= i and i <= 'z':
            return True
    return False

# Returns True  if the string has a uppercase
def is_up(x):
    for i in x:
        if 'A' <= i and i <= 'Z':
            return True

# Returns True  if the string has a numeric digit
def is_num(x):
    for i in x:
        if '0' <= i and i <= '9':
            return True
    return False

# Returns True if the string has any "$#@"
def is_other(x):
    for i in x:
        if i == '$' or i == '#' or i == '@':
            return True
    return False
    
s = input().split(',')
lst = []
    
for i in s:
    length = len(i)
    # Checks if all the requirements are fulfilled
    if 6 <= length and length <= 12 and is_low(i) and is_up(i) and is_num(i) and is_other(i):
        lst.append(i)

print(",".join(lst))





