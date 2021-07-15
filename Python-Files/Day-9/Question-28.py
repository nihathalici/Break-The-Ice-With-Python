"""
Question 28
Question:
Define a function that can receive two integer numbers in string form
and compute their sum and then print it in console.

Hints:
Use int() to convert a string to integer.
"""

sum = lambda s1, s2: int(s1) + int(s2)

print(sum("10", "45"))
