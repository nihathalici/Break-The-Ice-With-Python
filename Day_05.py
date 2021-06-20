#!/usr/bin/env python
# coding: utf-8

# # Question 16
# 
# ### **Question:**
# 
# > **_Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers._** >**_Suppose the following input is supplied to the program:_**
# 
# 
# 1,2,3,4,5,6,7,8,9
# 
# 
# > **_Then, the output should be:_**
# 
# 
# 1,9,25,49,81
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


lst = [str(int(i) ** 2) for i in input().split(",") if int(i) % 2]
print(",".join(lst))


# ---

# In[2]:


"""Solution by: shagun"""

lst = input().split(",")  # splits in comma position and set up in list

seq = []
lst = [int(i) for i in lst]  # converts string to integer
for i in lst:
    if i % 2 != 0:
        i = i * i
        seq.append(i)


seq = [
    str(i) for i in seq
]  # All the integers are converted to string to be able to apply join operation
print(",".join(seq))


# ---
# 
# **_There were a mistake in the the test case and the solution's whice were notified and fixed with the help of @dwedigital. My warm thanks to him._**
# 
# # Question 17
# 
# ### **Question:**
# 
# > **_Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:_**
# 
# ```
# D 100
# W 200
# ```
# 
# - D means deposit while W means withdrawal.
# 
# > **_Suppose the following input is supplied to the program:_**
# 
# ```
# D 300
# D 300
# W 200
# D 100
# ```
# 
# > **_Then, the output should be:_**
# 
# ```
# 500
# ```
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

# In[3]:


total = 0
while True:
    s = input().split()
    if not s:  # break if the string is empty
        break
    cm, num = map(
        str, s
    )  # two inputs are distributed in cm and num in string data type

    if cm == "D":
        total += int(num)
    if cm == "W":
        total -= int(num)

print(total)


# ---

# In[4]:


"""Solution by: leonedott"""

lst = []
while True:
    x = input()
    if len(x) == 0:
        break
    lst.append(x)

balance = 0
for item in lst:
    if "D" in item:
        balance += int(item.strip("D "))
    if "W" in item:
        balance -= int(item.strip("W "))
print(balance)


# ---

# In[ ]:


"""Solution by: AlexanderSro"""

account = 0
while True:
    action = input("Deposit/Whitdrow/Balance/Quit? D/W/B/Q: ").lower()
    if action == "d":
        deposit = input("How much would you like to deposit? ")
        account = account + int(deposit)
    elif action == "w":
        withdrow = input("How much would you like to withdrow? ")
        account = account - int(withdrow)
    elif action == "b":
        print(account)
    else:
        quit()


# ---

# In[ ]:


"""Solution by: ShalomPrinz
"""
lines = []
while True:
    loopInput = input()
    if loopInput == "done":
        break
    else:
        lines.append(loopInput)

lst = list(int(i[2:]) if i[0] == "D" else -int(i[2:]) for i in lines)
print(sum(lst))


# ---
