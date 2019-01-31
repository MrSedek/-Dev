import mysql.connector


connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="root")

try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()