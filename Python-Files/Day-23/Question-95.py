"""
Question 95
Question
Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score. You are given scores.
Store them in a list and find the score of the runner-up.

If the following string is given as input to the program:

5
2 3 6 6 5

Then, the output of the program should be:

5

Hints
Make the scores unique and then find 2nd best number
"""
'''
Solution by: mishrasunny-coder
'''

num = int(input("Enter num: "))

L = []

while True:
    L.append(num)
    num = int(input("Enter another: "))
    if num == 0:
        break

L1 = list(set(L[:]))
L2 = sorted(L1)
print(L2)

print(f'The runner up is {L2[-2]}')
