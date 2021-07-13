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

'''Solution by: shagun'''

# splits in comma position and set up in list
lst = input().split(',')

seq = []
# converts string to integer
lst = [int(i) for i in lst]

for i in lst:
    if i % 2 != 0:
        i = i * i
        seq.append(i)

# All the integers are converted to string to be able to apply join operation
seq = [str(i) for i in seq]

print(",".join(seq))
