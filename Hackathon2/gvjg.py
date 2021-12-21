# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 20:27:39 2021

@author: Yasaar Mauthoor
"""
import requests
import psycopg2   # importing a module to connect to postgres
import psycopg2.extras

# """Confirmed cases"""
# url_confirmed = 'https://api.covid19api.com/dayone/country/mauritius/status/confirmed/live'
# data_confirmed = (requests.get(url_confirmed)).json()
# case_confirmed = []
# for i in range(len(data_confirmed)): 
#     case_confirmed.append(data_confirmed[i]["Cases"])
#     # case_confirmed = data_confirmed[i]["Cases"]
#     # date = data_confirmed[i]["Date"]
#     # print (case_confirmed, date)
# next
   

# def run_query(query):
#     conn_string = "host='localhost' dbname='covid' user= 'yasaar' password='Mypg12'"
#     connection = psycopg2.connect(conn_string)
#     cursor = connection.cursor()
#     cursor.execute(query)
#     connection.commit()
#     try:
#         results = cursor.fetchall()
#         connection.close()
#         return results
#     except:
#         connection.close()






def update(self,case_confirmed):
    """Confirmed cases"""
    url_confirmed = 'https://api.covid19api.com/dayone/country/mauritius/status/confirmed/live'
    data_confirmed = (requests.get(url_confirmed)).json()
    case_confirmed = []
    for i in range(len(data_confirmed)): 
        case_confirmed.append(data_confirmed[i]["Cases"])
        # case_confirmed = data_confirmed[i]["Cases"]
        # date = data_confirmed[i]["Date"]
        # print (case_confirmed, date)
    next
        
    self.case_confirmed = case_confirmed
    query = f"UPDATE covid_cases SET confirmed = '{self.case_confirmed}';"
update()