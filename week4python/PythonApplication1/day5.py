# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:13:11 2021

@author: Yasaar for x in iterator]
"""


import string
alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
matrix = [[7,‘i’,3],
    [‘T’,‘s’,‘i’],
    [‘h’,‘%’,‘x’],
    [‘i’,' ‘,’#’],
    [‘s’,‘M’,' ‘],
    [‘$’,‘a’,' ‘],
    [‘#’,‘t’,‘%’],
    [‘^’,‘r’,‘!’]]
    
def decodematrix(matrix, items_per_list):
    decoded_words = ‘’
    i = 0
    while i < items_per_list:
        for char in matrix:
            try:
                if char[i] in alphabet_lower or char[i] in alphabet_upper:
                    decoded_words += char[i]
                else:
                    if decoded_words[-1] == ' ' or char[i] == ' ‘:
                        pass
                    elif type(char[i]) is int:
                        pass
                    else:
                        decoded_words += ’ '
            except:
                    pass
        i += 1
    return decoded_words
print(decodematrix(matrix, 3))


#----------------------------------------------------------------------------

# ex7
# def get_age(year=2021, month='November'):
#     year_born = input("Enter your birth year: ")
#     age = (year - int(year_born))
#     print(age)
#
#     def can_retire(gender,date_of_birth):
#         gender= input("Enter your gender(F or M): ")
#         print(gender)
#         if gender == 'M':
#             if age >= 67:
#                 print('Can retire')
#             else:
#                 print("Cannot retire")
#         elif gender == 'F':
#             if age >= 62:
#                 print('Can retire')
#             else:
#                 print('Cannot retire')
#     can_retire(gender='gender',date_of_birth='year_born')
# get_age()
# #XP2 exercise 8
# def get_value(num):
#     num=int(input("enter a number: "))
#     number = num + num*num + num*num*num + num*num*num*num
#     print(number)
# get_value(num='number')


#---------------------------------------------------------
#ex1
# def display_message():
#     print("i want chicken and waffles")
# display_message()

#ex2
# def favourite_book(title):
#     print("One of my favourite books is" + title)
# favourite_book(title = " Alice in wonderland")
#

#ex3
# def describe_city(city, country):
#     print(city + " is in " + country)
# describe_city(city="Kyoto", country="Japan")

#ex4
# import random
# def guess():
#    num=int(input("Enter a number from 1 to 100"))
#    print(num)
#    range=random.randrange(1,100)
#    print(int(range))
#
#    if num != range:
#        print("You lost")
#    else:
#        print("You win!")
# guess()

#ex5
# 123
# def make_shirt(shirt, text):
#     print(" size of shirt " + shirt + " , with message " + text)
#
# make_shirt(shirt= "small",text="nada")
# #4
# def make_shirt(shirt=" large ", text=" i love python"):
#     print(" shirt size: " + shirt + " with message " + text)
#

#5
# def make_shirt(shirt , text=" i love Python "):
#     print("Shirt of size: " + shirt+ " and with message: " + text)
# make_shirt("Medium")
# make_shirt("Large")
# make_shirt("Small","Vitamin Sea")
#     #6/
# def make_shirt(**kwargs):
#         print(kwargs)
#     make_shirt(size='Small', text="Get 'em!")


# ex6
# magician_names=["Apolla","Houdini","Blaine","Copperfield"]
# # def show_magicians():
# #     for i in magician_names:
# #         print("One of the magician is: "+i)
# # show_magicians()
#
# def show_magicians():
#     for i in magician_names:
#         print("One of the magician is: "+i)
#     def make_great():
#         for i in magician_names:
#             print("One of the magician is: "+ f"the Great {i}")
#     make_great()
# show_magicians()

#---------------------------------------------------------















































