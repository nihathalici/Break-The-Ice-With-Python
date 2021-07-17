"""
Question 74
Question
Please write a program to randomly generate a list with 5 numbers,
which are divisible by 5 and 7 , between 1 and 1000 inclusive.

Hints
Use random.sample() to generate a list of random values.
"""

import random

lst = [i for i in range(1, 1001) if i % 35 == 0]

resp = random.sample(lst, 5)

print(resp)
