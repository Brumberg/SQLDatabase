#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 13:22:09 2021

@author: samuel
"""
import mysql
import mysql.connector as dbcon



def main():
    mydb = dbcon.connect(
    host="localhost",
    user="samuel",
    passwd="root",
    database="ACCOUNTS")
    
    # prepare a cursor object using cursor() method
    cursor = mydb.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")
     

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print('Database version : {version}'.format(version=data))

    sqlstatement = 'SELECT * FROM Accounts'
    cursor.execute(sqlstatement)  
    results = cursor.fetchall()
    for i in results:
        print('User= {usrname} Password= {password}, Type=({t0},{t1})'.
              format(usrname=i[0],password=i[1],t0=type(i[0]),t1=type(i[1])))
        
    # disconnect from server
    mydb.close()

if __name__ == "__main__":
    main()