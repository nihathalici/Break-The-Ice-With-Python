"""
Question 79
Question
Please write a program to generate all sentences where subject is in
["I", "You"]
and verb is in
["Play", "Love"]
and the object is in
["Hockey","Football"].

Hints
Use list[index] notation to get a element from a list.
"""

'''Solution by: lcastrooliveira
'''

from itertools import product

def question_79():
    subject = ["I", "You"]
    verb = ["Play", "Love"]
    object = ["Hockey", "Football"]
    prod = [p for p in product(range(2), repeat=3)]
    for combination in prod:
        print(f'{subject[combination[0]]} {verb[combination[1]]} {object[combination[2]]}.')

question_79()
    
