# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 16:00:50 2021

@author: Yasaar Mauthoor
"""

# exercise XP 1
my_fav_numbers = {12,6,8,70,69}
print(type(my_fav_numbers))

print(my_fav_numbers)
my_fav_numbers.add(2)
my_fav_numbers.add(3)
print(my_fav_numbers)
my_fav_numbers.remove(69)
print(my_fav_numbers)
friend_fav_numbers = {5,28,1}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)
​
#exercise XP 2
#no
​
#exercise XP 3
for i in range(1,21):
    print(i)
​
#exercise XP 4
​
current_number = 1.5
while current_number <= 5.5 :
        print(current_number)
        current_number += 0.5
​
#exercise XP 5
basket = ["Banana", "Apples", "Oranges", "Blueberries"];
basket.remove("Banana")
print (basket)
basket.remove("Blueberries")
print (basket)
basket.append("Kiwi")
print (basket)
basket.insert(0,"Apples")
print (basket)
print (basket.count("Apples"))
print(basket.clear())
​
#exercise XP 6

name =''
while name != "varshana":
    name = input("Enter name:")

print("You an imposter!")
​
#exercise XP 7
​
my_list = ['Apple', 'Grey', 'Hello', 'Goodbye', 'Loop', 'Waves']
for i in range(1, len(my_list), 2):
    print(my_list[i])
​
# #exercise XP 8
i=1500
while i <= 2500:
    if ( i % 5==0 and i % 7 ==0):
        print (i)
    i+=1
​
#exercise XP 9
fruits = input("Enter your favourite fruit(s)")
my_list = fruits.split()
print(my_list)

fruity = input("Enter any fruit")

if fruity in fruits:
        print("You chose one of your favorite fruits! Enjoy!")

else: print("You chose a new fruit. I hope you enjoy")
​
#exercise XP 10
toppings = input("Choose your topping")

active = True
while active:
    adding = input("Topping added, Choose more or quit?")
    if adding == 'quit':
        active = False

print("Your total is:", 10+2.5, "for each topping")
​
# # exercise XP 11
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
print(sum(price))
​
# exercise XP 12
name_list = ['Oce', 'Princess', 'Anna', 'Moi']

name = input("Enter your name")
if name in name_list:
      age= int(input("Enter your age"))
if age<16 :
    name_list.remove(name)

print(name_list)
​
# # exercise XP 13 and 14
sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")