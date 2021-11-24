##ex1
#print("Hello world\n"*4)

##ex2
#print((99**3)*8)

##ex3
##5<3 true
##3 == 3 true
##3 == "3" true
##"3" > 3 false
##"Hello" == "hello" true


##ex4
#computer_brand = "dell"
#print(f"i have a {computer_brand} computer")

##ex5
#name = "yasaar"
#age = 22
#shoe_size = 42
#info = f"My name is {name}, i'm {age} years old and my shoe size is {shoe_size}"
#print(info)

##ex6
#a = 5
#b = 4
#if a > b : print("Hello world")


##ex7
#num = input("enter a number:")
#if num % 2 == 0 : print("it is odd")
#else: print("it is even")

##ex8
#name = input("what's your name?")
#my_name = "yasaar"
#if name == my_name: print("idiot why is your name same as mine")
#else: print("oufff, nice to meet u")

##ex9
#height = input("enter your height in inches please: ")
#if height =>


#day2--------------------------------------------------------------------------------------------------
#user_num = int(input("enter a num and get it's multiplication"))
#for i in range(0,20):
#   print (user_num * i)


#current_number = 0
#while current_number <= 10:    
#    print(current_number)   
#    current_number += 1

#print("Finished")

#---------------------------
my_fav_numbers ={2,5,8,12,15}
my_fav_numbers.add("69")
my_fav_numbers.add("46")
my_fav_numbers.remove("46")
friend_fav_numbers = {5,7,8,9,10}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

#---------------
no
#---------------
for i in range(1,20):
    print(i)
    
#---------------
#float is a number with decimal place (34.000)
#integer is a number without decimal
for i in range(0,5):
    print(i)
    print(i+0.5)
    
#---------------
user_input = input(“Please insert a 10 character string: “)
if len(user_input) > 10:
    print(“The input is larger than 10 characters”)
elif len(user_input) < 10:
    print(“The input is smaller than 10 characters”)
else:
    print(f”{user_input[0]} \n{user_input[-1]}“)
    result = “”
    for c in user_input:
        result += c
        print(result)
import random
str_list = list(result)
random.shuffle(str_list)
‘’.join(str_list)
example_list = [“Red”, “Green”, True, False, 0]
example_list[-1] = 1
my_tuple = (1+3, 2.7, ‘Thursday’)
my_tuple[0] = 5
example_list[2:4]
some_string = “Trou aux cerfs”
some_string[0:4]
example_list.append(1)
example_list.remove(True)
example_list.pop(1)
addition_list = [‘Green’, True]
complete_list = example_list + addition_list
for i in range(0, len(complete_list), 2):
    print(i)
abcd = [‘c’,‘b’,‘d’, ‘a’, ‘A’]
sorted(abcd)
complete_list.insert(3, [])
complete_list.extend([‘SOME’])
complete_list += [“Another one”]
list1 = [5, 10, 15, 20, 25, 50, 20]
for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200
“”"RANGE(start, end, step)“”"
number_range = range(1, 8, 2)
print(list(number_range))
numbers = list(range(1,6))
print(numbers)
a_tuple = (10, 20, 30, 40)
ten, twenty, thirty, forty = a_tuple
this_set = {“banana”, “apple”, “cherry”, “apple”}
duplicate_list1 = list1 + list1 + list1 + list1
duplicate_list1 = list(set(duplicate_list1))
password = ‘’
while password != ‘hello-world-123’:
  password = input(‘What is the top secret password? ’)
print(‘You guessed the right password!’)
while 1 == 1:
    print(“Looping...“)
current_number = 0
while current_number <= 10:
    current_number += 1
    if 3 < current_number < 7: # If the number is between 3 and 7
        continue                # Go back to the beginning of the loop
    print(current_number)

#day3---------------
from datetime import datetime
“”"Taking input from user and converting it to datetime object”“”
birthday = input(‘What is your birthday? ex. DD/MM/YYYY’)
birthday_convert_to_date = datetime.strptime(birthday, “%d/%m/%Y”)
“”"Specifing the current date”“”
current_date = datetime.now()
“”"age”“”
age = int(current_date.year - birthday_convert_to_date.year)
age_to_string = str(age)
last_digit_age = int(age_to_string[-1])
candles = ‘i’ * last_digit_age
cake = f’‘'\n       ___{candles}___
      |:H:a:p:p:y:|
    __|___________|__
    |^^^^^^^^^^^^^^^^^|
    |:b:i:r:t:h:d:a:y:|
    |                 |
    ~~~~~~~~~~~~~~~~~~~‘’'
cake2 = f’‘'       ___{candles}___   \n      |:H:a:p:p:y:|   \n    __|___________|__   \n    |^^^^^^^^^^^^^^^^^|   \n    |:b:i:r:t:h:d:a:y:|   \n    |                 |    \n    ~~~~~~~~~~~~~~~~~~~‘’'
if birthday_convert_to_date.year % 4 == 0:
    print(cake * 2)
some_list = [1,2,3]
some_list[2]
some_list.append(4)
continents = {‘Asia’: [‘China’, ‘India’, ‘Russia’], ‘Europe’: [‘Germany’, ‘France’]}
continents[‘Asia’].append(‘Singapore’)
continents[‘America’] = [‘USA’, ‘Brazil’]
del continents[‘America’]
“”"Can’t have same names for keys, overwrites it”“”
continents[‘Asia’] = [‘Mongolia’]
print(‘Europe’ in continents.keys())
# Check if Germany inside the continets values
print(‘Germany’ in continents.values())
for key in continents.keys():
    print(key)
for value in continents.values():
    print(‘Germany’ in value)
americas = {‘Europe’: [‘Germany’, ‘France’, ‘Belgium’]}
continents.update(americas)
sample_dict = {
  “name”: “Kelly”,
  “age”:25,
  “salary”: 8000,
  “city”: “New york”
}
keys_to_remove = [“name”, “salary”]
for key in keys_to_remove:
    del sample_dict[key]
list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
new_dict = {}
for (index, val) in enumerate(list_of_lists):
    new_dict[index] = val
integer_list = [1,2,3,4]
updated_list = []
for num in integer_list:
    if num % 2 == 0:
        updated_list.append(num * 2)
    else:
        updated_list.append(num)
updated_list = [num ** 2 for num in list(range(0,10)) if num % 2 == 0]
dict_comprehension = {index : val for (index, val) in enumerate(list_of_lists)}
my_number = ‘1234’
my_list = []
my_list = [int(num) for num in my_number]
print(type(my_list[0]))
list_comprehension = [ITERATOR(STORED_VALUE) for ITERATOR in RANGE/LIST/STRING if CONDITION]
# check_type = continents.items()
# for key, value in continents.items():
#     print(key, value)
sample_dict = {
   “class”:{
      “student”:{
         “name”:“Mike”,
         “marks”:{
            “physics”:70,
            “history”:80
         }
      }
   }
}
sample_dict[‘class’][‘student’][‘marks’][‘history’] -= 10

#--------------------------------------
brand={"name":["Zara"], "creation_date":["1975"], "creator_date":["Amancio Ortega Gaona"],"type_of_clothes":["men", "women" , "children" , "home"],
       "international_competitors":["Gap","H&M"], "number_stores":["7000"], "major_color": {"France":"blue","Spain":"red","US":["pink","green"]}}
brand["number_stores"]=2

print("Zara's clients are:", brand['type_of_clothes'][0:3] )

brand["country_creation"]=["Spain"]
if 'international_competitors' in brand:
    brand['international_competitors'].append("Desigual")

del brand['creation_date']

print(brand)
print(brand['international_competitors'][-1])
print(brand['major_color']['US'])
print(len(brand))

print(brand.keys())

more_on_zara = {"creation_date":["1975"], "number_stores":["10 000"]}

brand.update(more_on_zara)

print(brand.keys())

