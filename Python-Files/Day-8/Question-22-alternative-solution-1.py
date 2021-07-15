"""
Question 22
Question:
Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically.

Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

Then, the output should be:

2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

Hints
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
ss = input().split()

dict = {}

# setdefault() function takes key & value to set it as dictionary.
for i in ss:
    i = dict.setdefault(i, ss.count(i))

# items() function returns both key & value of dictionary as a list
# and then sorted. The sort by default occurs in order of 1st -> 2nd key
dict = sorted(dict.items())

for i in dict:
    print("%s:%d"%(i[0], i[1]))











