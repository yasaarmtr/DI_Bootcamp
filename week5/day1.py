# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:37:58 2021

@author: Yasaar Mauthoor
"""

class Farm:
    def __init__(self, name):
        self.name = name
        self.animals={}


    def add_animal(self, animal_name, amount=1):
        if animal_name in self.animals:
            self.animals[animal_name] += amount

        else:
            self.animals[animal_name] = amount

macdonald=Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.add_animal('cow',3)

macdonald.animals


print("E-I-E-I-0!")
#ex1---------------------------------------------
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.cat ={}
        
    def oldest_cat(self, cat_name, cat_age):
        
        
        
    
    
print(dict(sorted(list_cat.felines.items(), key=lambda item: item[1]))) 
    
#----------------------------
cat = {'Blue' : 5, 'Yellow' : 6}

keys = list(cat.keys())

cat[list(cat.keys())[-1]]

#ex2---------------------------------------------
class Dog:
    def __init__(self,name,height):
        self.name = name
        self.height = int(height)
        self.dogs={}
        
    def bark(self):
        print(f"{self.name} goes woof!")
        
    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm high!")
        
sarahs_dog = Dog("Teacup", 20)
sarahs_dog.bark()
sarahs_dog.jump()
davids_dog = Dog("Rex", 50)
davids_dog.jump()

bigger_dog = sarahs_dog.name
if sarahs_dog.height > davids_dog.height:
    print(bigger_dog)

else:
  print(davids_dog.name)

#ex3---------------------------------------------

#XP exercise 3

class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)

stairway = Song(["There's a lady who's sure",
                      "all that glitters is gold",
                      "and she's buying a stairway to heaven"])

print(stairway.sing_me_a_song())

 #XP exercise 4--------------------------------------
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name= zoo_name
        self.animals=[]
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            pass
    def get_animals(self):
        print(self.animals)
    def sell_animals(self, animals_sold):
       animals_sold =  self.animals.pop()
       print(animals_sold)