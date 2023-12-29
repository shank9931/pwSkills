import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("INSERT INTO users_table VALUES ('Rishab', '12345', 13)")
cursor.execute("INSERT INTO users_table VALUES ('James', 'pass@12345', 14)")
cursor.execute("INSERT INTO users_table VALUES ('Homer', 'Pass_12345', 15)")

connection.commit()