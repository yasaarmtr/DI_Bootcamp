# # -*- coding: utf-8 -*-
# """
# Created on Mon Dec  6 12:34:45 2021

# @author: Yasaar Mauthoor
# """

# import numpy as np
# import pandas as pd

# # 1. Import data/ get data
# # Dataframe - object from Pandas - the SQL in Python (a table)
# dataframe = pd.read_csv('train.csv')
# # 2. Analyze data
# # To group by Sex values in dataframe
# mean_sex_vals = dataframe.groupby('Sex').apply(np.mean)
# # 3. Manipulate data
# # One column is a Series object. Here we access 1 column
# age_column = dataframe.loc[:, 'Age']
# # To access multiple columns use a [[‘column_1’, ‘column_2’]]
# multiple_cols = dataframe[['Age', 'Sex']]
# # To access one row - specify index - use iloc[] index location function
# fifth_instance = dataframe.iloc[4]
# # To access multiple instances use ‘:’
# multiple_instances = dataframe.iloc[4:8]
# # DataFrame.dropna() - drops all of the instances/rows that have null values
# age_column.dropna(inplace = True)
# # To get all of the unique values in a column
# dataframe['Sex'].unique()
# # To filter and get specific instance, only ‘male’ for example
# just_males = dataframe[dataframe['Sex'] == 'male']
# # To order by - use sort_values (column name, order type/ascending/descending)
# dataframe = dataframe.sort_values('Fare', ascending = False) (edited) 
# #-------------------------------------------
# df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# print (df[]
#---------------------  
# a = np.arange(9).reshape((3,3)) #arange is NumPy's version of the Python's range function
# a
# array([[0, 1, 2],
#        [3, 4, 5],
#        [6, 7, 8]])
# b = np.arange(20, 11, -1).reshape((3,3))
# b
# array([[20, 19, 18],
#        [17, 16, 15],
#        [14, 13, 12]])
# a + b
# array([[20, 20, 20],
#        [20, 20, 20],
#        [20, 20, 20]])
# a * b
# array([[ 0, 19, 36],
#        [51, 64, 75],
#        [84, 91, 96]])
# np.dot(a, b) #the dot product of 2 matrices
# array([[ 45,  42,  39],
#        [198, 186, 174],
#        [351, 330, 309]])

#-----------------------
# import numpy as np
# a = np.array([1,2,3,4,5,6,7,8,9])
# def maths(a):
#     min = np.amin(a)

#     return min
# # -----------------------
# import numpy as np
# import matplotlib.pyplot as plt #conventional syntax 


# a = np.random.randint(0,75,(50,1))
# print (a)


# plt.scatter(a[:,0], a[:,1])
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.show()
#-----------------------
# import numpy as np
# import matplotlib.pyplot as plt

# randnums = np.random.randint(0, 76, 100)

# fifty_by_two = randnums.reshape(50,2)
# # print(fifty_by_two)


# # plt.scatter(fifty_by_two[:,0], fifty_by_two[:,1])
# # plt.xlabel('num1')
# # plt.ylabel('num2')
# # plt.show(block=True)
# # plt.interactive(False)

# fig, ax=plt.subplots(1,2,figsize=(64, 64))

# ax[0].hist(fifty_by_two[:,0], color='g', label = 'num1')
# ax[1].hist( fifty_by_two[:,1], color='r', label = 'num2')

# ax[0].legend()
# ax[1].legend()

# ax[0].set_ylabel('Frequency')
# ax[1].set_ylabel('Frequency')

# ax[0].set_xlabel('num1')
# ax[1].set_xlabel('num2')

# plt.show()

#----------------------------------------
#dailychallenge

import numpy as np
import matplotlib.pyplot as plt
import random

N = random.randint(2, 39)
M = random.randint(2, 49)
def table(M,N):
    if M<50 and N<40:
        return np.random.randint(1,101,(M,N))
table_a = table(M,N)
# print(table_a)

# print(table_a[2])

# print(table_a)[:,2] #error

table_a[-1] = 7
# print(table_a)

table_a[:,-1] = table_a[:,0] + table_a[:,1]
print(table_a)















