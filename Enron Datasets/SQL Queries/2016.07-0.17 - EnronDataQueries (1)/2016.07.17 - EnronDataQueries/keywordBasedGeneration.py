# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 10:48:09 2016

@author: sbbk529
"""


import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root',host='127.0.0.1',database='enrondb')

cursor = cnx.cursor()

firstNames = ["kenneth", "jeffrey", "andrew", "richard", "micheal", "lea", "ben", "dave", "mark"]

lastNames = ["lay", "skilling", "fastow", "causay", "kapper", "fastow", "glisan", "delainey", "koenig"]

keywords = ["FERC", "Affair", "Devastating", "Investigation", "Disclosure", "Bonus", "Meeting", "Plan", "Services", "Report"]

for i in range(0,len(firstNames)):
    
    queryText = "SELECT  Email_id FROM employeelist WHERE LOWER(firstName) LIKE \"%"
    queryText +=  firstNames[i] + "%\" AND LOWER(lastName) LIKE \"%" 
    queryText +=  lastNames[i] + "%\""
    query = (queryText)
    
    queryText = "SELECT  COUNT(sender) FROM message WHERE LOWER(sender) LIKE \"%"
    queryText +=  firstNames[i] + "%\" AND LOWER(sender) LIKE \"%"
    queryText +=  lastNames[i] + "%\""
    query = (queryText)
    
    
    queryText = " select count(*) from message where LOWER(body) LIKE \"%"
    queryText +=  keywords[i] + "%\""
    query = (queryText)
    
#    queryText = "SELECT  COUNT(rvalue) FROM recipientinfo WHERE LOWER(rvalue) LIKE \"%"
#    queryText +=  firstNames[i] + "%\" AND LOWER(rvalue) LIKE \"%" 
#    queryText +=  lastNames[i] + "%\""
#    query = (queryText)

    cursor.execute(query)
    
    
    for emailCount in cursor:
      print(str(i) +" " +keywords[i] + str(emailCount))

cursor.close()
cnx.close()


