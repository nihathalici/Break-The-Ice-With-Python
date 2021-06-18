#!/usr/bin/env python
# coding: utf-8

# # Question 10
# 
# ### **Question**
# 
# > **_Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically._**
# 
# > **_Suppose the following input is supplied to the program:_**
# 
# hello world and practice makes perfect and hello world again
# 
# > **_Then, the output should be:_**
# 
# again and hello makes perfect practice world
# 
# ---
# 
# ### Hints:
# 
# > **_In case of input data being supplied to the question, it should be assumed to be a console input.We use set container to remove duplicated data automatically and then use sorted() to sort the data._**
# 
# ---
# 
# **Solutions:**

# In[1]:


word = input().split()

for i in word:
    if (
        word.count(i) > 1
    ):  # count function returns total repeatation of an element that is send as argument
        word.remove(i)  # removes exactly one element per call

word.sort()
print(" ".join(word))


# **OR**

# In[2]:


word = input().split()
[
    word.remove(i) for i in word if word.count(i) > 1
]  # removal operation with comprehension method
word.sort()
print(" ".join(word))


# **OR**

# In[3]:


word = sorted(
    list(set(input().split()))
)  #  input string splits -> converting into set() to store unique
#  element -> converting into list to be able to apply sort
print(" ".join(word))


# ---
# 
# # Question 11
# 
# ### **Question**
# 
# > **_Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence._**
# 
# > **_Example:_**
# 
# 0100,0011,1010,1001
# 
# > **_Then the output should be:_**
# 
# 1010
# 
# > **_Notes: Assume the data is input by console._**
# 
# ---
# 
# ### Hints:
# 
# > **_In case of input data being supplied to the question, it should be assumed to be a console input._**
# 
# ---
# 
# **Solutions:**

# In[4]:


def check(x):  # converts binary to integer & returns zero if divisible by 5
    total, pw = 0, 1
    reversed(x)

    for i in x:
        total += pw * (ord(i) - 48)  # ord() function returns ASCII value
        pw *= 2
    return total % 5


data = input().split(",")  # inputs taken here and splited in ',' position
lst = []

for i in data:
    if check(i) == 0:  # if zero found it means divisible by zero and added to the list
        lst.append(i)

print(",".join(lst))


# **OR**

# In[5]:


def check(x):  # check function returns true if divisible by 5
    return int(x, 2) % 5 == 0  # int(x,b) takes x as string and b as base from which
    # it will be converted to decimal


data = input().split(",")

data = list(
    filter(check, data)
)  # in filter(func,object) function, elements are picked from 'data' if found True by 'check' function
print(",".join(data))


# **OR**

# In[6]:


data = input().split(",")
data = list(
    filter(lambda i: int(i, 2) % 5 == 0, data)
)  # lambda is an operator that helps to write function of one line
print(",".join(data))


# ---
# 
# # Question 12
# 
# ### **Question:**
# 
# > **_Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line._**
# 
# ---
# 
# ### Hints:
# 
# > **_In case of input data being supplied to the question, it should be assumed to be a console input._**
# 
# ---
# 
# **Solutions:**

# In[7]:


lst = []

for i in range(1000, 3001):
    flag = 1
    for j in str(i):  # every integer number i is converted into string
        if ord(j) % 2 != 0:  # ord returns ASCII value and j is every digit of i
            flag = 0  # flag becomes zero if any odd digit found
    if flag == 1:
        lst.append(str(i))  # i is stored in list as string

print(",".join(lst))


# **OR**

# In[8]:


def check(element):
    return all(
        ord(i) % 2 == 0 for i in element
    )  # all returns True if all digits i is even in element


lst = [
    str(i) for i in range(1000, 3001)
]  # creates list of all given numbers with string data type
lst = list(
    filter(check, lst)
)  # filter removes element from list if check condition fails
print(",".join(lst))


# **OR**

# In[9]:


lst = [str(i) for i in range(1000, 3001)]
lst = list(
    filter(lambda i: all(ord(j) % 2 == 0 for j in i), lst)
)  # using lambda to define function inside filter function
print(",".join(lst))


# ---
# 
# # Question 13
# 
# ### **Question:**
# 
# > **_Write a program that accepts a sentence and calculate the number of letters and digits._**
# 
# > **_Suppose the following input is supplied to the program:_**
# 
# hello world! 123
# 
# > **_Then, the output should be:_**
# 
# LETTERS 10
# 
# DIGITS 3
# 
# ---
# 
# ### Hints:
# 
# > **_In case of input data being supplied to the question, it should be assumed to be a console input._**
# 
# ---
# 
# **Solutions:**

# In[10]:


word = input()
letter, digit = 0, 0

for i in word:
    if ("a" <= i and i <= "z") or ("A" <= i and i <= "Z"):
        letter += 1
    if "0" <= i and i <= "9":
        digit += 1

print("LETTERS {0}\nDIGITS {1}".format(letter, digit))


# **OR**

# In[ ]:


word = input()
letter, digit = 0, 0

for i in word:
    if i.isalpha():  # returns True if alphabet
        letter += 1
    elif i.isnumeric():  # returns True if numeric
        digit += 1
print(
    f"LETTERS {letter}\n{digits}"
)  # two different types of formating method is shown in both solution


# ---
# 
# ## Conclusion
# 
# **_All the above problems are mostly string related problems. Major parts of the solution includes string releted functions and comprehension method to write down the code in more shorter form._**

# In[ ]:




