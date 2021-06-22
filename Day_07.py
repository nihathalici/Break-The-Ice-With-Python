#!/usr/bin/env python
# coding: utf-8

# # Question 20
# 
# ### **Question:**
# 
# > **_Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n._**
# 
# ---
# 
# ### Hints:
# 
# > **_Consider use class, function and comprehension._**
# 
# ---
# 
# 
# 
# **Solution: Python 3**

# In[1]:


"""Solution by: ShalomPrinz
"""


class MyGen:
    def by_seven(self, n):
        for i in range(0, int(n / 7) + 1):
            yield i * 7


for i in MyGen().by_seven(int(input("Please enter a number... "))):
    print(i)


# ---

# In[2]:


"""Solution by: Seawolf159
"""


class Divisible:
    def by_seven(self, n):
        for number in range(n + 1):
            if number % 7 == 0:
                yield number


divisible = Divisible()
generator = divisible.by_seven(int(input("Please insert a number. --> ")))
for number in generator:
    print(number)


# ---
# 
# # Question 21
# 
# ### **Question:**
# 
# > **_A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:_**
# 
# ```
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ```
# > **_The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer._**
# > **_Example:_**
# > **_If the following tuples are given as input to the program:_**
# 
# ```
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ```
# 
# > **_Then, the output of the program should be:_**
# 
# ```
# 2
# ```
# ---
# 
# ### Hints:
# 
# > **_In case of input data being supplied to the question, it should be assumed to be a console input.Here distance indicates to euclidean distance.Import math module to use sqrt function._**
# 
# ---
# 
# 
# 
# **Solutions:**

# In[3]:


import math

x, y = 0, 0
while True:
    s = input().split()
    if not s:
        break
    if s[0] == "UP":  # s[0] indicates command
        x -= int(s[1])  # s[1] indicates unit of move
    if s[0] == "DOWN":
        x += int(s[1])
    if s[0] == "LEFT":
        y -= int(s[1])
    if s[0] == "RIGHT":
        y += int(s[1])
        # N**P means N^P
dist = round(
    math.sqrt(x ** 2 + y ** 2)
)  # euclidean distance = square root of (x^2+y^2) and rounding it to nearest integer
print(dist)


# ---
