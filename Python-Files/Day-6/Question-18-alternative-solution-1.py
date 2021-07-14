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



def check(x):
    cnt = ( 6 <= len(x) and len(x) <= 12)
    for i in x:
        if i.isupper():
            cnt += 1
            break
    for i in x:
        if i.islower():
            cnt += 1
            break
    for i in x:
        if i.isnumeric():
            cnt += 1
            break
    for i in x:
        if i == '@' or i == '#' or i == '$':
            cnt += 1
            break
        
    # counting if total 5 all conditions are fulfilled then returns True
    return cnt == 5


s = input().split(',')
# Filter function pick the words from s, those returns True by check() function
lst = filter(check, s)
print(",".join(lst))

