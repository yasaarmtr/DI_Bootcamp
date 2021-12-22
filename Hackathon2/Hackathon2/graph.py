# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 00:19:29 2021

@author: Yasaar Mauthoor
"""
from config import Config

import requests
import psycopg2   # importing a module to connect to postgres
import psycopg2.extras
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



"""confirmed cases"""
url_confirmed = 'https://api.covid19api.com/dayone/country/mauritius/status/confirmed/live'
data_confirmed = (requests.get(url_confirmed)).json()
case_confirmed = []
for i in range(len(data_confirmed)): 
    case_confirmed.append(data_confirmed[i]["Cases"])
next

"""death cases"""
url_death = 'https://api.covid19api.com/dayone/country/mauritius/status/deaths/live'
data_death = (requests.get(url_death)).json()
case_death = []
for i in range(len(data_death)): 
    case_death.append(data_death[i]["Cases"])
next

"""recovered cases"""
url_recovered = 'https://api.covid19api.com/dayone/country/mauritius/status/recovered/live'
data_recovered = (requests.get(url_recovered)).json()
case_recovered= []
for i in range(len(data_recovered)): 
    case_recovered.append(data_recovered[i]["Cases"])
next

"""date"""
url_date = 'https://api.covid19api.com/dayone/country/mauritius/status/confirmed/live'
data_date = (requests.get(url_date)).json()
date = []
for i in range(len(data_date)): 
    date.append(data_date[i]["Date"][:10])
next


plt.plot(date, case_death)
plt.xlabel('time')
plt.ylabel('cases')
plt.title('deaths cases')
plt.show()
plt.savefig('C:/Users/Yasaar Mauthoor/OneDrive/Documents/DI/DI_Bootcamp/Hackathon2/deaths.png')


plt.plot(date, case_recovered)
plt.xlabel('time')
plt.ylabel('cases')
plt.title('recovered cases')
plt.show()
plt.savefig('C:/Users/Yasaar Mauthoor/OneDrive/Documents/DI/DI_Bootcamp/Hackathon2/recovered.png')


plt.plot(date, case_confirmed)
plt.xlabel('time')
plt.ylabel('cases')
plt.title('confirmed cases')
plt.show()
plt.savefig('C:/Users/Yasaar Mauthoor/OneDrive/Documents/DI/DI_Bootcamp/Hackathon2/confirmed.png')





















# def insert_data(data_date):
#     """ insert multiple vendors into the vendors table  """
#     sql = "INSERT INTO covid_cases(date) VALUES(%s)"
#     conn = None
#     try:
#         # read database configuration
#         params = config()
#         # connect to the PostgreSQL database
#         conn = psycopg2.connect(**params)
#         # create a new cursor
#         cur = conn.cursor()
#         # execute the INSERT statement
#         cur.executemany(sql,data_date)
#         # commit the changes to the database
#         conn.commit()
#         # close communication with the database
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()