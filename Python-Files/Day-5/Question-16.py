"""
Question 16
Question:
Use a list comprehension to square each odd number in a list.
The list is input by a sequence of comma-separated numbers.

>Suppose the following input is supplied to the program:

1,2,3,4,5,6,7,8,9

Then, the output should be:

1,9,25,49,81

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
lst = [str(int(i)**2) for i in input().split(',') if int(i) % 2]

print(",".join(lst))
