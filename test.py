import sqlite3
import csv
from sqlite3 import Error

recruitIDs = []
recruitIDs.append({
            'id' : 22458397,
            'name' : 'Bob Watson',
            'pos': 'QB',
            'height' : "6'3",
            'weight' : '202',
            'rating' : '705',
            'rank' : '5',
            'hometown' : 'Miami, FL',
            'miles' : '75'
        })
temp = []
temp.append({
            'id' : 21123445,
            'name' : 'Jake Broom',
            'pos': 'DB',
            'height' : "6'1",
            'weight' : '189',
            'rating' : '644',
            'rank' : '34',
            'hometown' : 'New York, NY',
            'miles' : '1222'
})


recruitIDs += temp


print(len(recruitIDs))
print(recruitIDs)