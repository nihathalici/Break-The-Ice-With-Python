"""
Question 12
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.The numbers obtained should be printed
in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

def check(element):
    # all returns True if all digits i is even in element
    return all(ord(i) % 2 == 0 for i in element)

# creates list of all given numbers with string data type
lst = [str(i) for i in range(1000, 3001)]

# filter removes element from list if check condition fails
lst = list(filter(check, lst))

print(",".join(lst))
