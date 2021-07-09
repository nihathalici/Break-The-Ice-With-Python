"""
Question 3
Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i x i)
such that is an integral number between 1 and n (both included).
and then the program should print the dictionary.

Suppose the following input is supplied to the program: 8

Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()
"""

'''Solution by: minnielahoti
   Corrected by: TheNobleKnight 
'''

try:
    num = int(input("Enter a number: "))
except ValueError as err:
    print(err)

dictio = dict()
for item in range(num+1):
    if item == 0:
        continue
    else:
        dictio[item] = item * item
print(dictio)








