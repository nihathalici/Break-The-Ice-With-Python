"""
Question 10
Question
Write a program that accepts a sequence of whitespace separated words as input and
prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again

Then, the output should be:

again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.
"""
'''Solution by: Sukanya-Mahapatra
'''

inp_string = input("Enter string: ").split()
out_string = []

for words in inp_string:
    if words not in out_string:
        out_string.append(words)
print(" ".join(sorted(out_string)))
                                                     
