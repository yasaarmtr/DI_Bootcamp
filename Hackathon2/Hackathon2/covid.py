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

# defining our connection criteria
HOSTNAME = 'localhost'
USERNAME = 'yasaar'
PASSWORD = '1234'
DATABASE = 'covid'

# making the connection to the database
connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

# accessing the query editor
# cursor = connection.cursor()
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

# defining the query
query = "SELECT * FROM actors"

# running the query
cursor.execute(query)

# fetching the results
results = cursor.fetchall()

# closing the connection
connection.close()

"""Confirmed cases"""
url_confirmed = 'https://api.covid19api.com/dayone/country/mauritius/status/confirmed/live'
data_confirmed = (requests.get(url_confirmed)).json()
for i in range(10): 
    case_confirmed = data_confirmed[i]["Cases"]
    date = data_confirmed[i]["Date"]
    print (case_confirmed, date)
next
    



# ------------------------------------------





#--------------------------------------------------------------

# """Deaths cases"""
# url_deaths = 'https://api.covid19api.com/dayone/country/mauritius/status/deaths/live'
# data_deaths = (requests.get(url_deaths)).json()

# case_deaths = data_deaths[0]["Cases"]

# """Recovered cases"""
# url_recovered = 'https://api.covid19api.com/dayone/country/mauritius/status/recovered/live'
# data_recovered = (requests.get(url_recovered)).json()

# case_recovered = data_recovered[0]["Cases"]




