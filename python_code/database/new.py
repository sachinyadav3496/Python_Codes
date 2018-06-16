import pymysql as sql
try:
    db = sql.connect('localhost','testuser','redhat','testdb')
    cursor = sql.Cursor(db)
except Exception as e:
    print("Error!!",e)

