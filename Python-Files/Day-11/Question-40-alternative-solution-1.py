"""
Question 40
Question:
Write a program which accepts a string as input to print "Yes"
if the string is "yes" or "YES" or "Yes", otherwise print "No".

Hints:
Use if statement to judge condition.
"""

'''
Solution by: AasaiAlangaram
'''
input = input("Enter string:")

output = ''.join(['Yes' if input == 'yes' or input == 'YES' or input == 'Yes' else 'No'])

print(str(output))

