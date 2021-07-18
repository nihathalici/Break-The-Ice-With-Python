"""
Question 90
Question
Please write a program which count and print the numbers
of each character in a string input by console.

Example: If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

Hints
Use dict to store key/value pairs. Use dict.get() method to lookup a key with default value.
"""

'''Solution by: popomaticbubble
'''

def character_counter(text):
    characters_list = list(text)
    char_count = {}
    for x in characters_list:
        if x in char_count.keys():
            char_count[x] += 1
        else:
            char_count[x] = 1
    return char_count

def dict_viewer(dictionary):
    for x, y in dictionary.items():
        print(f"{x}, {y}")

text = input("> ")
dict_viewer(character_counter(text))























