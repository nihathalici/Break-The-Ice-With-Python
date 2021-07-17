"""
Question 61
Question
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.

Example: If the following n is given as input to the program:

7

Then, the output of the program should be:

13

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints
We can define recursive function in Python.
"""
'''Solution by: NikolayEm
'''
n = int(input())

f = lambda x: 0 if x == 0 else 1 if x == 1 else f(x - 1) + f(x - 2)

print(','.join([str(f(x)) for x in range(0, n + 1)]))



