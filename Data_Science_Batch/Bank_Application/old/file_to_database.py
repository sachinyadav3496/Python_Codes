import sqlite3 as sql
import json

try :
    f = open('bank.db')
    data = json.load(f)
    f.close()

    db = sql.connect('pybank.db')
    c = db.cursor()

    l = len(data['user'])

    for i in range(l) :

        name = data['user'][i]
        bal = data['bal'][i]
        password = data['passwd'][i]
        acc_no = data['acc'][i]

        cmd = "insert into bank(name,acc_no,bal,password) values('{}',{},'{}','{}')".format(name,acc_no,bal,password)
        c.execute(cmd)
        db.commit()
    print("Your data sucessfully updated")
except Exception as e :
    print("Error! : {}".format(e))

    
