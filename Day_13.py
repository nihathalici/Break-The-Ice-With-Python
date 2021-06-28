#!/usr/bin/env python
# coding: utf-8

# # Question 47
# 
# ### **Question**
# 
# > **_Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area._**
# 
# ---
# 
# ### Hints
# 
# > **_Use def methodName(self) to define a method._**
# 
# ---
# 
# 
# 
# **Solutions:**

# In[1]:


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return 3.1416 * (self.radius ** 2)


circle = Circle(5)
print(circle.area())


# ---
# 
# # Question 48
# 
# ### **Question**
# 
# > **_Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area._**
# 
# ---
# 
# ### Hints
# 
# > **_Use def methodName(self) to define a method._**
# 
# ---
# 
# 
# 
# **Solutions:**

# In[2]:


class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width


rect = Rectangle(2, 4)
print(rect.area())


# ---
# 
# # Question 49
# 
# ### **Question**
# 
# > **_Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default._**
# 
# ---
# 
# ### Hints
# 
# > **_To override a method in super class, we can define a method with the same name in the super class._**
# 
# ---
# 
# 
# 
# **Solutions:**

# In[3]:


class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length * self.length


Asqr = Square(5)
print(Asqr.area())  # prints 25 as given argument

print(Square().area())  # prints zero as default area


# ---
# 
# # Question 50
# 
# ### **Question**
# 
# > **_Please raise a RuntimeError exception._**
# 
# ---
# 
# ### Hints
# 
# > **_Use raise to raise an exception._**
# 
# ---
# 
# **Solution:**

# In[4]:


raise RuntimeError("something wrong")


# ---
# 
# ## Conclusion
# 
# **_Well It seems that the above problems are very much focused on basic concpets and implimantation of object oriented programming.As the concepts are not about to solve any functional problem rather design the structure , so both codes are very much similar in there implimantation part._**
