import sqlite3

connection = sqlite3.connect("users.db")

cursor = connection.cursor()

cursor.execute("UPDATE users_table SET age = 20")

connection.commit()