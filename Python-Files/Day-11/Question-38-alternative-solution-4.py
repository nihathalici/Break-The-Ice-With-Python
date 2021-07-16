"""
Question 38
Question:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the
first half values in one line and the last half values in one line.

Hints:
Use [n1:n2] notation to get a slice from a tuple.
"""

'''
Solution by: saxenaharsh24
'''

tup = [i for i in range (1, 11)]

print(f'{tuple(tup[:5])} \n{tuple(tup[5:])}')
