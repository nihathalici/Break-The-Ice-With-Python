"""
Question 12
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.The numbers obtained should be printed
in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

lst = [str(i) for i in range(1000, 3001)]

# using lambda to define function inside filter function
lst = list(filter(lambda i: all(ord(j) % 2 == 0 for j in i), lst))

print(",".join(lst))

