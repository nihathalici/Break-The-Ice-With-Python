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

def rec(n):
    if n == 0:
        return n
    return rec(n - 1) + n

n = int(input())

sum = rec(n)

print(sum)
