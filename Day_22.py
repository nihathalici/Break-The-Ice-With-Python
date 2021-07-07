#!/usr/bin/env python
# coding: utf-8

# # Question 90
# 
# ### **Question**
# 
# > **_Please write a program which count and print the numbers of each character in a string input by console._**
# 
# > **_Example:
# > If the following string is given as input to the program:_**
# 
# ```
# abcdefgabc
# ```
# 
# > **_Then, the output of the program should be:_**
# 
# ```
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1
# ```
# 
# ### Hints
# 
# > **_Use dict to store key/value pairs.
# > Use dict.get() method to lookup a key with default value._**
# 
# ---
# 
# **Solutions:**

# In[1]:


import string

s = input()
for letter in string.ascii_lowercase:
    cnt = s.count(letter)
    if cnt > 0:
        print("{},{}".format(letter, cnt))


# **OR**

# In[2]:


s = input()
for letter in range(ord("a"), ord("z") + 1):  # ord() gets the ascii value of a char
    letter = chr(letter)  # chr() gets the char of an ascii value
    cnt = s.count(letter)
    if cnt > 0:
        print("{},{}".format(letter, cnt))


# ---
# 
# # Question 91
# 
# ### **Question**
# 
# > **_Please write a program which accepts a string from console and print it in reverse order._**
# 
# > **Example:
# > If the following string is given as input to the program:\***
# 
# 
# rise to vote sir
# 
# 
# > **_Then, the output of the program should be:_**
# 
# ris etov ot esir
# 
# ### Hints
# 
# > **_Use list[::-1] to iterate a list in a reverse order._**
# 
# ---
# 
# **Solutions:**

# In[3]:


s = input()
s = "".join(reversed(s))
print(s)


# ---
# 
# # Question 92
# 
# ### **Question**
# 
# > **_Please write a program which accepts a string from console and print the characters that have even indexes._**
# 
# > **_Example:
# > If the following string is given as input to the program:_**
# ```
# H1e2l3l4o5w6o7r8l9d
# ```
# > **_Then, the output of the program should be:_**
# ```
# Helloworld
# ```
# ### Hints
# 
# > **_Use list[::2] to iterate a list by step 2._**
# 
# ---
# 
# 
# 
# **Solutions:**

# In[4]:


s = "H1e2l3l4o5w6o7r8l9d"
s = [s[i] for i in range(len(s)) if i % 2 == 0]
print("".join(s))


# **OR**

# In[5]:


s = "H1e2l3l4o5w6o7r8l9d"
ns = ""
for i in range(len(s)):
    if i % 2 == 0:
        ns += s[i]
print(ns)


# ---
# 
# # Question 93
# 
# ### **Question**
# 
# > **_Please write a program which prints all permutations of [1,2,3]_**
# 
# ---
# 
# ### Hints
# 
# > **_Use itertools.permutations() to get permutations of list._**
# 
# ---
# 
# **Solution:**

# In[6]:


import itertools

print(list(itertools.permutations([1, 2, 3])))


# ---
# 
# # Question 94
# 
# ### **Question**
# 
# > **_Write a program to solve a classic ancient Chinese puzzle:
# > We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?_**
# 
# ---
# 
# ### Hints
# 
# > **_Use for loop to iterate all possible solutions._**
# 
# ---
# 
# **Solution:**

# In[7]:


def solve(numheads, numlegs):
    ns = "No solutions!"
    for i in range(numheads + 1):
        j = numheads - i
        if 2 * i + 4 * j == numlegs:
            return i, j
    return ns, ns


numheads = 35
numlegs = 94
solutions = solve(numheads, numlegs)
print(solutions)


# ---
