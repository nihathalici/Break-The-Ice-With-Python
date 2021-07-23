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


'''Solution by: lcastrooliveira
'''

def question_15(string_digit):
    return sum(int(string_digit * n) for n in range(1, 5))

inp = input()

print(question_15(inp))
