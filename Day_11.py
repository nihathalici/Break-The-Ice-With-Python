#!/usr/bin/env python
# coding: utf-8

# # Question 38
# 
# ### **Question:**
# 
# > **_With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line._**
# 
# ---
# 
# ### Hints:
# 
# > **_Use [n1:n2] notation to get a slice from a tuple._**
# 
# ---
# 
# 
# 
# **Solutions:**

# In[1]:


tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in range(0, 5):
    print(tpl[i], end=" ")
print()
for i in range(5, 10):
    print(tpl[i], end=" ")


# **OR**

# In[2]:


tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lst1, lst2 = [], []

for i in range(0, 5):
    lst1.append(tpl[i])

for i in range(5, 10):
    lst2.append(tpl[i])

print(lst1)
print(lst2)


# **OR**

# In[3]:


"""
Solution by: CoffeeBrakeInc
"""

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lt = int(len(tup) / 2)
print(tup[:lt], tup[lt:])


# ---
# 
# **OR**

# In[4]:


"""
Solution by: AasaiAlangaram
"""

tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("The Original Tuple:", tp)

[
    print("Splitted List :{List}".format(List=tp[x : x + 5]))
    for x in range(0, len(tp), 5)
]


# ---
# 
# # Question 39
# 
# ### **Question:**
# 
# > **_Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)._**
# 
# ---
# 
# ### Hints:
# 
# > **_Use "for" to iterate the tuple. Use tuple() to generate a tuple from a list._**
# 
# ---
# 
# 
# 
# **Solutions:**

# In[5]:


tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tpl1 = tuple(i for i in tpl if i % 2 == 0)
print(tpl1)


# **OR**

# In[6]:


tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tpl1 = tuple(
    filter(lambda x: x % 2 == 0, tpl)
)  # Lambda function returns True if found even element.
# Filter removes data for which function returns False
print(tpl1)


# ---
# 
# # Question 40
# 
# ### **Question:**
# 
# > **_Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No"._**
# 
# ---
# 
# ### Hints:
# 
# > **_Use if statement to judge condition._**
# 
# ---
# 
# 
# 
# **Solution: Python 3**

# In[7]:


"""
Solution by: Seawolf159
"""
text = input("Please type something. --> ")
if text == "yes" or text == "YES" or text == "Yes":
    print("Yes")
else:
    print("No")


# ---

# In[8]:


"""
Solution by: AasaiAlangaram
"""
input = input("Enter string:")
output = "".join(
    ["Yes" if input == "yes" or input == "YES" or input == "Yes" else "No"]
)
print(str(output))


# ---
# 
# # Question 41
# 
# ### **Question:**
# 
# > **_Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10]._**
# 
# ---
# 
# ### Hints:
# 
# > **_Use map() to generate a list.Use lambda to define anonymous functions._**
# 
# ---
# 
# 
# 
# **Solutions:**

# In[9]:


# No different way of code is written as the requirment is specificly mentioned in problem description

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squaredNumbers = map(lambda x: x ** 2, li)  # returns map type object data
print(list(squaredNumbers))  # converting the object into list


# ---
# 
# # Question 42
# 
# ### **Question:**
# 
# > **_Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]._**
# 
# ---
# 
# ### Hints:
# 
# > **_Use map() to generate a list.Use filter() to filter elements of a list.Use lambda to define anonymous functions._**
# 
# ---
# 
# 
# 
# **Solutions:**

# In[10]:


def even(x):
    return x % 2 == 0


def squer(x):
    return x * x


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li = map(
    squer, filter(even, li)
)  # first filters number by even number and the apply map() on the resultant elements
print(list(li))


# ---
# 
# # Question 43
# 
# ### **Question:**
# 
# > **_Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included)._**
# 
# ---
# 
# ### Hints:
# 
# > **_Use filter() to filter elements of a list.Use lambda to define anonymous functions._**
# 
# ---
# 
# 
# 
# **Solutions:**

# In[11]:


def even(x):
    return x % 2 == 0


evenNumbers = filter(even, range(1, 21))
print(list(evenNumbers))


# ---
