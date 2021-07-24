"""
Question 17
Question:
Write a program that computes the net amount of a bank account based a transaction log
from console input. The transaction log format is shown as following:

D 100
W 200

D means deposit while W means withdrawal.

Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100

Then, the output should be:

500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input."""

'''Solution by: ChichiLovesDonkeys
'''


money = 0

while 1:
    trans = input().split(' ')
    if trans[0] == 'D':
        money = money + int(trans[1])
    elif trans[0] == 'W':
        money = money - int(trans[1])
    elif input() == '':
        break
    print(f'Your current balance is: {money}')
        
















