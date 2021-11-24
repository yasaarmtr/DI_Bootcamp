# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:30:45 2021

@author: Yasaar Mauthoor
"""

# class Door :
#     def __init__(self, is_opened):
#         self.is_opened = is_opened

    
# class BlockedDoor(Door):
    
#xp---------------------------------------------

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        
    def show_age (self):
        print({self.__age})

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Persian(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    


    
my_cats = [Bengal("oce",2), Chartreux("vars",4), Persian("ossi",6)]

mo_cat = Cat("momo", 5)

mo_cat.show_age()
                    
my_pets = Pets(my_cats)

my_pets.walk()       
           

#---------------------------------------------------------
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = int(age)
        self.weight = int(weight)
        
    def bark(self):
        return (f"{self.name} is barking")
        
    def run_speed(self):
        return (self.weight/self.age*10)
        
    def fight(self, other_dog):
        self.other_dog = other_dog
       if int(self.run_speed()) * int(self.weight) > int(other_dog.run_speed()) * int(other_dog.weight):
            print(f"{self.name} has won!")
            
        else:
            print(f"{other_dog} has won!")
            
my_dog1 = Dog("ruan", 7, 30)
my_dog2 = Dog("waf", 5, 20)
my_dog3 = Dog("tony", 6, 25)
my_dog1.fight(my_dog1)

#-------------------------------------
class family():
    def __inti__(self, is_child= False):
        self.members = [
            {'name':'Michael','age':35,'gender':'Male','is_child':False},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False}
        ]
        self.last.name = "LaSossette"
     
    def born(self, **kwargs):
         self.members.append(kwargs)
         born(name = "Oce", age = 1, gender = "Male", is_child = True )
         print(f"Congratulation for the new born {self.name}")
      
    def is_18 (self, name, age):
          self.name = name
          self.age = age
          if age >17 :
              self.is_child = False
          else:
              self.is_child = True
    
        return is_18

           
           
           