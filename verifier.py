"""
A verifier that checks if every row has at least one item is a specific column.
"""

import mysql.connector
from database import login_info

db = mysql.connector.Connect(**login_info)
cursor = db.cursor()
cursor.execute("""SELECT id, name, family  FROM animal""")
data = cursor.fetchall()
count = 0
for _id, name, family in data:
    cursor.execute("SELECT feed FROM food WHERE anid={0}".format(_id))
    items = cursor.fetchall()
    diet = len(items)
    if diet > 0:
        count += 1
cursor.execute("SELECT COUNT(*) FROM animal")
animals = int((cursor.fetchone()[0]))
if animals==count:
    print("Every animal can eat.")
else:
    print("At least one animal can't eat")
