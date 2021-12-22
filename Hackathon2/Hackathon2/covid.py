# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 19:32:42 2021

@author: Yasaar Mauthoor
"""
"""trials"""

# requests.get ("https://api.covid19api.com/dayone/country/south-africa/status/confirmed")

# response = requests.get("http://api.open-notify.org/iss-now.json")
# import numpy as np
# import requests
# import json

# url = 'https://api.covid19api.com/dayone/country/mauritius/status/recovered/live' # confirmed cases only since the begining
# url = 'https://api.covid19api.com/all' # not found
#url = 'https://api.covid19api.com/live/country/mauritius/status/confirmed/date/2020-03-21T13:13:30Z' #not since the begining
#url = 'https://api.covid19api.com/summary'
#url = 'https://api.covid19api.com/live/country/mauritius/status/confirmed' #4 variable period 6 months

# data = (requests.get(url)).json()

# # first_case = data["Countries"]
# TotalConfirmed = data["Countries"][110]["TotalConfirmed"]
# Date = data["Countries"][110]["Date"]
# print (TotalConfirmed)
# print (Date[:10])
# ---------------------------------------------------------------------------------------

import requests
import psycopg2   # importing a module to connect to postgres
import psycopg2.extras
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector




# def database():
# defining our connection criteria
HOSTNAME = 'localhost'
USERNAME = 'yasaar'
PASSWORD = 'Mypg12'
DATABASE = 'covid'

# # making the connection to the database
# connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

# accessing the query editor
# cursor = connection.cursor()
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

record_to_insert = ('case_confirmed' )

#defining the query
query = "SELECT * FROM actors"

#running the query
cursor.execute(query)

#fetching the results
results = cursor.fetchall()

#closing the connection
connection.close()
#-----
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yasaar",
#   password="Mypg12",
#   database="covid"
# )
#
# mycursor = mydb.cursor()
#
#
# def add_entry():
#     # id = 10
#     # case_confirmed = 10
#     # deaths = 3
#     # recovered = 7
#     sql = "INSERT INTO customers (id, case_confirmed, deaths, recovered) VALUES (%s, %s, %s, %s)"
#     val = (1,10,3,6)
#     mycursor.execute(sql, val)
#
#     mydb.commit()
#
#     print(mycursor.rowcount, "record inserted.")
# add_entry()




# def get_data():
    
# """Confirmed cases"""
# url_confirmed = 'https://api.covid19api.com/dayone/country/mauritius/status/confirmed/live'
# data_confirmed = (requests.get(url_confirmed)).json()
# case_confirmed = []
# for i in range(10): 
#     case_confirmed.append(data_confirmed[i]["Cases"])
#     case_confirmed.append(data_confirmed[i]["Date"])
#     # case_confirmed = data_confirmed[i]["Cases"]
#     # date = data_confirmed[i]["Date"]
#     # print (case_confirmed, date)
# next
    
# # Printing the variables
# print(case_confirmed)
# print(date)

# plt.plot(case_confirmed,date) # Function to plot
# plt.title('Confirm Cases') # Function to give title

# # Functions to give x and y labels
# plt.xlabel('Numeber of cases') 
# plt.ylabel('Date')

# # Functionn to show the graph  
# plt.show()



# -----------------
# def graft():
#     # Generation of variables 
#     x=np.arange(0,10) #Array of range 0 to 9
#     y=x**3
    
#     # Printing the variables
#     print(x)
#     print(y)
    
#     plt.plot(x,y) # Function to plot
#     plt.title('Line Chart') # Function to give title
    
#     # Functions to give x and y labels
#     plt.xlabel('X-Axis') 
#     plt.ylabel('Y-Axis')
    
#     # Functionn to show the graph  
#     plt.show()





#--------------------------------------------------------------


