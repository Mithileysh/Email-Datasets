# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 10:45:33 2016

@author: sbbk529
"""

keywords = ["ferc", "affair", "devastating", "investigation", "disclosure", "bonus", "meeting", "plan", "services", "report"]
queryText = "SELECT  m.sender, e.firstName, e.lastName, COUNT(*) AS emailCounts FROM message m, employeelist e WHERE m.sender = e.Email_id AND YEAR(m.date) = 2001 AND m.mid IN ( SELECT mid FROM message"
if len(keywords) > 0:
     
    for i in range(0,len(keywords)):
        if i == 0:
            queryText += "  WHERE "
        else:
            queryText += " OR "
        queryText += "LOWER(message.body) LIKE \"%"
        queryText +=  keywords[i] + "%\""
    
queryText += ") GROUP BY m.sender ORDER BY emailCounts DESC"