import sqlite3
conn = sqlite3.connect("test.db")
c = conn.cursor()
c.execute("select * from user")
k = c.fetchall()
print(k)

