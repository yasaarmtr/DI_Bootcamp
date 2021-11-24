# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 00:58:02 2021

@author: Yasaar Mauthoor
"""
# Exercise 1: 

'''Your best friend.'''

def abs():
    """Return the absolute value of the argument. """
    pass
def int():
    """Return the value of the argument. """
    pass
def input():
    """Return the input of the argument. """
    pass


print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)







# Exercise 2: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    def __str__(self):
        return f"{self.amount} {self.currency}"
    def __int__(self):
        return self.amount
    def __repr__(self):
        return f"{self.amount} {self.currency}"
    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                return self.amount + other.amount
            else:
                raise Exception("Cannot add between Currency type <dollar> and <shekel>")
        else:
            raise Exception("Cannot add except objects and ints")
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
print(str(c1))
print(c1 + 5)
c1 +=c2
print(c1)
print(c1+c3)