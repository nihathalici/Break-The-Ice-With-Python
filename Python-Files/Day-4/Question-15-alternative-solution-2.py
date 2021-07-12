"""
Question 15
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program:

9
Then, the output should be:

11106
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input."""


'''Solution by: apenam7
'''

a = input()

print(sum(int(i*a) for i in range(1,5)))
