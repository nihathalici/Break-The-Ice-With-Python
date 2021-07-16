"""
Question 38
Question:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the
first half values in one line and the last half values in one line.

Hints:
Use [n1:n2] notation to get a slice from a tuple.
"""

tpl = (1,2,3,4,5,6,7,8,9,10)

for i in range(0, 5):
    print(tpl[i], end= ' ')

print()

for i in range(5, 10):
    print(tpl[i], end= ' ')

