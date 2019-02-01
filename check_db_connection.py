import mysql.connector
from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="root")


try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()

"""
connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="root")

try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
"""