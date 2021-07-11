"""
Question 12
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.The numbers obtained should be printed
in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

'''Solution by: nikitaMogilev
'''
# map() digits of each number with lambda function and check if all() of them even
# str(num) gives us opportunity to iterate through number by map() and join()
print(','.join([str(num) for num in range(1000, 3001) if all( map(lambda num: int(num) % 2 == 0, str(num)))]))
