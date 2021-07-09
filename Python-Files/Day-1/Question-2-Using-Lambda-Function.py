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
# Using Lambda Function

n = int(input())

def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
print(shortFact(n))
