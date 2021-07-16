"""
Question 40
Question:
Write a program which accepts a string as input to print "Yes"
if the string is "yes" or "YES" or "Yes", otherwise print "No".

Hints:
Use if statement to judge condition.
"""

'''
Solution by: Seawolf159
'''
text = input("Please type something. --> ")

if text == "yes" or text == "YES" or text == "Yes":
    print("Yes")
else:
    print("No")

