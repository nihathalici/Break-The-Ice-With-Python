"""
Question 6
Question:
Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 _ C _ D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.
For example Let us assume the following comma separated input sequence is given to the program:

100,150,180
The output of the program should be:

18,22,24
Hints:
If the output received is in decimal form, it should be rounded off to its nearest value
(for example, if the output received is 26.0, it should be printed as 26).
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
from math import *

C, H = 50, 30

def calc(D):
    D = int(D)
    return str(int(sqrt((2*C*D)/H)))

D = input().split(',')

# applying calc function on D and storing as a list
D = list(map(calc, D)) 

print(",".join(D))












