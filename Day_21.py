#!/usr/bin/env python
# coding: utf-8

# # Question 85
# 
# ### **Question**
# 
# > **_By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]._**
# 
# ---
# 
# ### Hints
# 
# > **_Use list comprehension to delete a bunch of element from a list.Use enumerate() to get (index, value) tuple._**
# 
# ---
# 
# 
# 
# **Solutions:**

# In[1]:


li = [12, 24, 35, 70, 88, 120, 155]
li = [li[i] for i in range(len(li)) if i not in (0, 4, 5)]
print(li)


# ---
# 
# # Question 86
# 
# ### **Question**
# 
# > **_By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155]._**
# 
# ---
# 
# ### Hints
# 
# > **_Use list's remove method to delete a value._**
# 
# ---
# 
# 
# 
# **Solutions:**

# In[2]:


li = [12, 24, 35, 24, 88, 120, 155]
li.remove(24)  # this will remove only the first occurrence of 24
print(li)


# ---
# 
# # Question 87
# 
# ### **Question**
# 
# > **_With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists._**
# 
# ---
# 
# ### Hints
# 
# > **_Use set() and "&=" to do set intersection operation._**
# 
# ---
# 
# 
# 
# **Solutions:**

# In[3]:


list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]
set1 = set(list1)
set2 = set(list2)
intersection = set1 & set2
print(intersection)


# **OR**

# In[4]:


list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]
set1 = set(list1)
set2 = set(list2)
intersection = set.intersection(set1, set2)
print(intersection)


# ---
# 
# # Question 88
# 
# ### **Question**
# 
# > **_With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved._**
# 
# ---
# 
# ### Hints
# 
# > **_Use set() to store a number of values without duplicate._**
# 
# ---
# 
# 
# 
# **Solutions:**

# In[5]:


li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
for i in li:
    if li.count(i) > 1:
        li.remove(i)
print(li)


# **OR**

# In[6]:


def removeDuplicate(li):
    seen = {}  # dictionary
    for item in li:
        if item not in seen:
            seen[item] = True
            yield item


li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
ans = list(removeDuplicate(li))
print(ans)


# ---
# 
# # Question 89
# 
# ### **Question**
# 
# > **_Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class._**
# 
# ---
# 
# ### Hints
# 
# > **_Use Subclass(Parentclass) to define a child class._**
# 
# ---
# 
# **Solution:**

# In[7]:


class Person(object):
    def getGender(self):
        return "Unknown"


class Male(Person):
    def getGender(self):
        return "Male"


class Female(Person):
    def getGender(self):
        return "Female"


aMale = Male()
aFemale = Female()
print(aMale.getGender())
print(aFemale.getGender())


# ---
