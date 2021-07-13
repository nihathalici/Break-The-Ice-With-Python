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
In case of input data being supplied to the question, it should be assumed to be a console input.

"""
total = 0

while True:
    s = input().split()
    # break if the string is empty
    if not s:
        break
    # two inputs are distributed in cm and num in string data type
    cm, num = map(str, s)

    if cm == 'D':
        total += int(num)
    if cm == 'W':
        total -= int(num)

print(total)
