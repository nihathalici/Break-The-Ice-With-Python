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

'''Solution by: StartZer0'''


s = list(input())

dict_count_ = {k:s.count(k) for k in s}

list_of_tuples = [(k, v) for k, v in dict_count_.items()]

list_of_tuples.sort(key = lambda x: x[1], reverse = True)

for item in list_of_tuples:
    print(item[0], item[1])




