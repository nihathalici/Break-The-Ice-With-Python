"""
Question 2
Question:
Write a program which can compute the factorial of a given numbers.The results should be printed
in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8
Then, the output should be:40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

'''Solution by: minnielahoti
'''

while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError as err:
        print(err)

org = num
fact = 1
while num:
    fact = num * fact
    num = num - 1
print(f'the factorial of {org} is {fact}')






















