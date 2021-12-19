# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 19:32:42 2021

@author: Yasaar Mauthoor
"""

# import requests

# requests.get ("https://api.covid19api.com/dayone/country/south-africa/status/confirmed")

# response = requests.get("http://api.open-notify.org/iss-now.json")

import requests
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




"""Confirmed cases"""
url_confirmed = 'https://api.covid19api.com/dayone/country/mauritius/status/confirmed/live'
data_confirmed = (requests.get(url_confirmed)).json()
# for i in data_confirmed:
case_confirmed = data_confirmed[0]["Cases"]
    


"""Deaths cases"""
url_deaths = 'https://api.covid19api.com/dayone/country/mauritius/status/deaths/live'
data_deaths = (requests.get(url_deaths)).json()

case_deaths = data_deaths[0]["Cases"]

"""Recovered cases"""
url_recovered = 'https://api.covid19api.com/dayone/country/mauritius/status/recovered/live'
data_recovered = (requests.get(url_recovered)).json()

case_recovered = data_recovered[0]["Cases"]


#function retrive data




# """
# GETLive By Country And Status
# GETLive By Country All Status
# GETive By Country And Status After Dat"""
