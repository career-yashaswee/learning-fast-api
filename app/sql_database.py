import sqlite3

connection = sqlite3.connect("sqlite.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS book (id INTEGER, context TEXT, weight REAL, status TEXT)""")
cursor.execute("""INSERT INTO book VALUES (12701, 'plam_trees', 90.32, 'placed')""")
cursor.execute("""INSERT INTO book VALUES (12702, 'screws', 23.32, 'in_transit')""")
cursor.execute("""
SELECT status FROM book
WHERE id=12702
""")
result = cursor.fetchone()
print(result)
connection.commit()
connection.close()