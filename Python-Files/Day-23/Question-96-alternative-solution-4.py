"""
Question 96
Question
You are given a string S and width W.
Your task is to wrap the string into a paragraph of width.

If the following string is given as input to the program:

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Then, the output of the program should be:

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

Hints
Use wrap function of textwrap module
"""

"""solution by  : popomaticbubble
"""

import itertools

string = input("> ")

width_length = int(input("What is the width of the groupings? "))


def grouper(string, width):
    iters = [iter(string)] * width
    return itertools.zip_longest(*iters, fillvalue='')

def displayer(groups):
    for x in groups:
        if x == '':
            continue
        else:
            print(''.join(x))

displayer(grouper(string, width_length))

