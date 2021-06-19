#!/usr/bin/env python
# coding: utf-8

# # Question 14
# 
# ### **Question:**
# 
# > **_Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters._**
# 
# > **_Suppose the following input is supplied to the program:_**
# 
# 
# Hello world!
# 
# 
# > **_Then, the output should be:_**
# 
# 
# UPPER CASE 1
# 
# LOWER CASE 9
# 
# 
# ---
# 
# ### Hints:
# 
# > **_In case of input data being supplied to the question, it should be assumed to be a console input._**
# 
# ---
# 
# 
# 
# **Solutions:**

# In[1]:


word = input()
upper, lower = 0, 0

for i in word:
    if "a" <= i and i <= "z":
        lower += 1
    if "A" <= i and i <= "Z":
        upper += 1

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper, lower))


# **OR**

# In[2]:


word = input()
upper, lower = 0, 0

for i in word:
    lower += i.islower()
    upper += i.isupper()

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper, lower))


# **OR**

# In[3]:


word = input()
upper = sum(
    1 for i in word if i.isupper()
)  # sum function cumulatively sum up 1's if the condition is True
lower = sum(1 for i in word if i.islower())

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper, lower))


# **OR**

# In[4]:


# solution by Amitewu

string = input("Enter the sentense")
upper = 0
lower = 0
for x in string:
    if x.isupper() == True:
        upper += 1
    if x.islower() == True:
        lower += 1

print("UPPER CASE: ", upper)
print("LOWER CASE: ", lower)


# ---
# 
# # Question 15
# 
# ### **Question:**
# 
# > **_Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a._**
# 
# > **_Suppose the following input is supplied to the program:_**
# 
# 
# 9
# 
# 
# > **_Then, the output should be:_**
# 
# 
# 11106
# 
# 
# ---
# 
# ### Hints:
# 
# > **_In case of input data being supplied to the question, it should be assumed to be a console input._**
# 
# ---
# 
# 
# 
# **Solutions:**

# In[5]:


a = input()
total, tmp = 0, str()  # initialing an integer and empty string

for i in range(4):
    tmp += a  # concatenating 'a' to 'tmp'
    total += int(tmp)  # converting string type to integer type

print(total)


# **OR**
# 
# ```python
# a = input()
# total = int(a) + int(2*a) + int(3*a) + int(4*a)  # N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
# print(total)
# ```

# In[ ]:




