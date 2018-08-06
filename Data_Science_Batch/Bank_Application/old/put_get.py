import sqlite3 as sql 
import time
db = ''
c = ''

def main():
    print("\nSelect Service \n1.Get infromation \n2.Put Information\n")
    ch = int(input("Choice : "))
    if ch == 1 :
        acc_no = int(input("Enter account number : "))
        get_data(acc_no)
    elif ch == 2 :
        put_data()
    else :
        print("Thanks ")

def connect():
    """connect()-> Use to established connection with your database"""
    global db,c
    
    try : 
        
        db = sql.connect('pybank.db')
        c = db.cursor()
    
    except Exception as e :
        
        print("Error : data base connectivity errors ")
        print("Error : {}".format(e))

def get_data(acc_no):
    """get_data(acc_no)-> used to show all details of custmor based on account number. """
    
    try : 
        cmd = "select * from bank where acc_no = {}".format(acc_no)
        c.execute(cmd)
        d = c.fetchone()
        print("Name = {}\nAcc_no = {}\nBal = {}\nPassword = {}".format(d[0],d[1],d[2],d[3]))
        main()
    
    except Exception as e :
        
        print("Error : No entry found with this account number")
        print("Error : {} ".format(e))
        main()

def put_data():
    "put_data()->used to create new data entry into database "
    
    try  :
        cmd = "select acc_no from bank"
        c.execute(cmd)
        data =  c.fetchall()
        acc_no = data[-1][0] + 1
        name = input("Enter Your Name : ")
        bal = input("Enter Opening Amount : ")
        from getpass import getpass
        password = getpass()
        
        cmd = "insert into bank(name,acc_no,bal,password) values('{}',{},'{}','{}')".format(name,acc_no,bal,password)
        c.execute(cmd)
        db.commit()
        print("User Created Sucessfully ")
        print("Note down your account no {}.".format(acc_no))
        main()
    
    except Exception as e :
        
        print("Error : {}",e)
        main()

if __name__ == "__main__" :
    print("\n\nWelcome to database services ")
    print("\nTrying to connect to database ..... ")
    time.sleep(2)
    connect()
    print("Got connected to database ")
    main()

