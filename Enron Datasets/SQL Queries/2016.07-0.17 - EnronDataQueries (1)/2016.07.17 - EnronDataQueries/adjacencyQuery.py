# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 20:34:08 2016

@author: sbbk529
"""

import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root',host='127.0.0.1',database='enrondb')

cursor = cnx.cursor()

firstNames = ["kenneth", "jeffrey", "andrew", "richard", "micheal", "lea", "ben", "dave", "mark"]

lastNames = ["lay", "skilling", "fastow", "causay", "kapper", "fastow", "glisan", "delainey", "koenig"]

keywords = ["FERC", "Affair", "Devastating", "Investigation", "Disclosure", "Bonus", "Meeting", "Plan", "Services", "Report"]

emails = ["jeff.dasovich@enron.com","james.d.steffes@enron.com","j.kaminski@enron.com","kay.mann@enron.com","steven.j.kean@enron.com","sara.shackleton@enron.com","lynn.blair@enron.com","sally.beck@enron.com","richard.b.sanders@enron.com","matthew.lenhart@enron.com"]

    
for i in range(0,len(emails)):
    for j in range(0,len(emails)):
        queryText = "SELECT  COUNT(*) FROM message m, recipientinfo r WHERE m.mid = r.mid  AND LOWER(m.sender) LIKE \"%"
        queryText += emails[i] + "%\"  AND r.rvalue LIKE \"%"
        queryText += emails[j] + "%\""
        #print (queryText)
        query = (queryText)

        cursor.execute(query)
    
    
        for (countValue) in cursor:
          print(emails[i] + "," + emails[j] + "," + str(countValue[0]))

cursor.close()
cnx.close()




