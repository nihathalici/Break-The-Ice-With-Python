#!/usr/bin/env python
# coding: utf-8

# # Question 18
# 
# ### **Question:**
# 
# > **_A website requires the users to input username and password to register. Write a program to check the validity of password input by users._**
# 
# > **_Following are the criteria for checking the password:_**
# 
# - **_At least 1 letter between [a-z]_**
# - **_At least 1 number between [0-9]_**
# - **_At least 1 letter between [A-Z]_**
# - **_At least 1 character from [$#@]_**
# - **_Minimum length of transaction password: 6_**
# - **_Maximum length of transaction password: 12_**
# 
# > **_Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma._**
# 
# > **_Example_**
# 
# > **_If the following passwords are given as input to the program:_**
# 
# 
# ABd1234@1,a F1#,2w3E*,2We3345
# 
# 
# > **_Then, the output of the program should be:_**
# 
# 
# ABd1234@1
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


def is_low(x):  # Returns True  if the string has a lowercase
    for i in x:
        if "a" <= i and i <= "z":
            return True
    return False


def is_up(x):  # Returns True  if the string has a uppercase
    for i in x:
        if "A" <= i and i <= "Z":
            return True
    return False


def is_num(x):  # Returns True  if the string has a numeric digit
    for i in x:
        if "0" <= i and i <= "9":
            return True
    return False


def is_other(x):  # Returns True if the string has any "$#@"
    for i in x:
        if i == "$" or i == "#" or i == "@":
            return True
    return False


s = input().split(",")
lst = []

for i in s:
    length = len(i)
    if (
        6 <= length
        and length <= 12
        and is_low(i)
        and is_up(i)
        and is_num(i)
        and is_other(i)
    ):  # Checks if all the requirments are fulfilled
        lst.append(i)

print(",".join(lst))


# **OR**

# In[2]:


def check(x):
    cnt = 6 <= len(x) and len(x) <= 12
    for i in x:
        if i.isupper():
            cnt += 1
            break
    for i in x:
        if i.islower():
            cnt += 1
            break
    for i in x:
        if i.isnumeric():
            cnt += 1
            break
    for i in x:
        if i == "@" or i == "#" or i == "$":
            cnt += 1
            break
    return (
        cnt == 5
    )  # counting if total 5 all conditions are fulfilled then returns True


s = input().split(",")
lst = filter(
    check, s
)  # Filter function pick the words from s, those returns True by check() function
print(",".join(lst))


# **OR**

# In[3]:


import re

s = input().split(",")
lst = []

for i in s:
    cnt = 0
    cnt += 6 <= len(i) and len(i) <= 12
    cnt += bool(
        re.search("[a-z]", i)
    )  # here re module includes a function re.search() which returns the object information
    cnt += bool(
        re.search("[A-Z]", i)
    )  # of where the pattern string i is matched with any of the [a-z]/[A-z]/[0=9]/[@#$] characters
    cnt += bool(
        re.search("[0-9]", i)
    )  # if not a single match found then returns NONE which converts to False in boolean
    cnt += bool(re.search("[@#$]", i))  # expression otherwise True if found any.
    if cnt == 5:
        lst.append(i)

print(",".join(lst))


# ---
# 
# # Question 19
# 
# ### **Question:**
# 
# > **_You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:_**
# 
# - **_1: Sort based on name_**
# - **_2: Then sort based on age_**
# - **_3: Then sort by score_**
# 
# > **_The priority is that name > age > score._**
# 
# > **_If the following tuples are given as input to the program:_**
# 
# 
# Tom,19,80
# 
# John,20,90
# 
# Jony,17,91
# 
# Jony,17,93
# 
# Json,21,85
# 
# 
# > **_Then, the output of the program should be:_**
# 
# 
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
# 
# 
# ---
# 
# ### Hints:
# 
# > **_In case of input data being supplied to the question, it should be assumed to be a console input.We use itemgetter to enable multiple sort keys._**
# 
# ---
# 
# 
# 
# **Solutions:**

# In[ ]:


lst = []
while True:
    s = input().split(",")
    if not s[0]:  # breaks for blank input
        break
    lst.append(tuple(s))

lst.sort(
    key=lambda x: (x[0], x[1], x[2])
)  # here key is defined by lambda and the data is sorted by element priority 0>1>2 in accending order
print(lst)


# In[ ]:




