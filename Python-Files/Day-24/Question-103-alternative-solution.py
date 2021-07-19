"""
Question 103
Question
Given a number N.
Find Sum of 1 to N Using Recursion

Input

5

Output

15

Hints
Make a recursive function to get the sum
"""

"""Solution by: popomaticbubble
"""

def summer(counter, n, current):
    if n == 0:
        return 0
    if counter == n:
        return current + n
    else:
        current = current + counter
        counter += 1
        return summer(counter, n, current)

N = int(input("> "))
print(summer(1, N, 0))








