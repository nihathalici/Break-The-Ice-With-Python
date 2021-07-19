"""
Question 101
Question
You are given a string. Your task is to count the frequency of letters
of the string and print the letters in descending order of frequency.

If the following string is given as input to the program:

aabbbccde

Then, the output of the program should be:

b 3
a 2
c 2
d 1
e 1

Hints
Count frequency with dictionary and sort by Value from dictionary Items
"""

'''Solution by: yuan1z'''

X = input()
my_set = set(X)
arr = []

for item in my_set:
    arr.append([item, X.count(item)])

tmp = sorted(arr, key = lambda x: (-x[1], x[0]))

for i in tmp:
    print(i[0] + ' ' + str(i[1]))






