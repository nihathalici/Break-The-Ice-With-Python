"""
Question 48
Question
Define a class named Rectangle which can be constructed by a length and width.
The Rectangle class has a method which can compute the area.

Hints
Use def methodName(self) to define a method.
"""


class Rectangle():

    def __init__(self, init_l, init_w):
        self.length = init_l
        self.width = init_w

    def area(self):
        return self.length * self.width

rect = Rectangle(2,4)
print(rect.area())
