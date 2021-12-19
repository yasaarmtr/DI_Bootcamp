# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 11:42:11 2021

@author: Yasaar Mauthoor
"""

from tabulate import tabulate
import psycopg2
def order():
    choice = None
    while choice != "X":
        print("Moti's Fruit Shake Stand with questionable hygiene")
        inv = get_inv()
        print(tabulate(inv, headers=['Fruit', 'Amount']))
        choice = input("What do you want to add to your shake?")
        update_inv(choice)
    else:
        print("Bye")
def update_inv(choice):
    query = f"UPDATE fruit SET fruit_quantity=fruit_quantity-1 WHERE fruit_name = '{choice}';"
    return run_query(query)
def get_inv():
    query = "SELECT fruit_name, fruit_quantity FROM fruit ORDER BY fruit_name ASC;"
    return run_query(query)
def run_query(query):
    conn_string = "host='localhost' dbname='shakes' user='postgres' password='yasaar'"
    connection = psycopg2.connect(conn_string)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    try:
        results = cursor.fetchall()
        connection.close()
        return results
    except:
        connection.close()
# HOSTNAME = 'localhost'
# USERNAME = 'yussiroz'
# PASSWORD = 'letmein'
# DATABASE = 'dvdrental'
# fruits = [('apple', 4),('lemon', 5)]
# # THERE’S NO GOOD REASON TO REPEAT YOURSELF IF YOU CAN CREATE A GENERAL FUNCTION
# # I.E run_query(query)
# conn_string = "host='localhost' dbname='shakes' user='postgres' password='yasaar'"
# connection = psycopg2.connect(conn_string)
# cursor = connection.cursor()
# query = "CREATE TABLE fruit (name varchar (255), quantity int);"
# cursor.execute(query)
# query = f"INSERT INTO fruit (name, quantity) values {fruits[0]}, {fruits[1]};"
# cursor.execute(query)
# connection.commit()
# connection.close()
# connection = psycopg2.connect(conn_string)
# cursor = connection.cursor()
# fruits = [('apple', 4),('lemon', 5)]
# query = f"INSERT INTO fruit (name, quantity) values {fruits[0]}, {fruits[1]};"
# cursor.execute(query)
# connection.commit()
# connection.close()
# inventory = get_inv()
# update_inv('apple')
# inventory = get_inv()


fruit = [('apple',6),('banana',10)]


def add_fruit(fruit_name, fruit_quantity):
    query = f"insert into fruit(fruit_name,fruit_quantity) values ('{fruit_name}',{fruit_quantity});"
    return run_query(query)

# add_fruit('mango', 5)






