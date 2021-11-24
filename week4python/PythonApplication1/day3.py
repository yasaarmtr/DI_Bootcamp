# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 14:16:29 2021

@author: Yasaar Mauthoor
"""
#ex1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]



dictionary = dict(zip(keys,values))
print(dictionary)


#exercise XP 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

age=int(input("Enter age or enter '0' to quit:"))
price = []
active= True
while age != 0:
    age=int(input("Enter age or enter '0' to quit:"))
    # for i in list:
    if age <= 3:
          price.append(0)
    elif age>3 and age<12:
          price.append(10)
    elif age== 0:
          active = False
    else:
          price.append(15)

print(price)
family_prices=zip(family.keys(),price)
prices={}
for i,j in family_prices:
    prices[i]= j
print(prices)