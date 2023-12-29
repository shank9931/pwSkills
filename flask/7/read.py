import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM users_table")
results = cursor.fetchall()
print(results)
