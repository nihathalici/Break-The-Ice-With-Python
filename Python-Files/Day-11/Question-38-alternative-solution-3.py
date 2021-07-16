"""
Question 38
Question:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the
first half values in one line and the last half values in one line.

Hints:
Use [n1:n2] notation to get a slice from a tuple.
"""

'''
Solution by: AasaiAlangaram
'''

tp = (1,2,3,4,5,6,7,8,9,10)

print('The Original Tuple:',tp)

[print('Splitted List :{List}'.format(List = tp[x:x+5])) for x in range(0, len(tp),5)]
