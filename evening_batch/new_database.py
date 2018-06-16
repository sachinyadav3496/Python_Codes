import pymysql as sql
import getpass

try:
    con = sql.connect("localhost","sachin","redhat","paper")
    c = con.cursor()
except Exception as e:
    print("There is an error !!",e)

def create_user():
    name = input("Enter User Name - ")
    password = getpass.getpass("Enter Your password : ")
    dbname = input("Enter Database Name - ")
    cmd1 = "create user '{0}'@'localhost' identified by '{1}' ".format(name,password)
    cmd2 = "create database {0}".format(dbname)
    cmd3 = "grant all privileges on {0}.* to '{1}'@'localhost'".format(dbname,name)
    try :
        c.execute(cmd1)
        c.execute(cmd2)
        c.execute(cmd3)
    except Exception as e :
        print("Error!!! ",e)
        con.rollback()

def create_table():
    tb_name = input("Enter Table name - ")
    l = []
    print("\nEnter table filed and values seprated by space eg: name varchar(50) - \n")
    while True:
        tag = input().strip()
        temp = tag.split()
        l.append(temp)
        ch = input("\nDo want to add more fields - y/n\n\t\t : ")
        if ch.lower() == 'y' :
            pass
        else :
            break
    cmd1 = "create table {0} (".format(tb_name)

    for field,tp in l:
       cmd1 =  cmd1+field+" "+tp+","

    cmd1=cmd1[:len(cmd1)-1]
    cmd1 = cmd1 + ")"
    try :

        c.execute(cmd1)
    except Exception as e:
        print("Error!!!",e)
        con.rollback

    

if __name__ == "__main__" :
    ch = int(input("Enter your choice - \n1.Create Database and User\n2.Create table\n\t\t: "))
    if ch == 1 :
        create_user()
    elif ch == 2 :
        create_table()
    else : 
        print("Wrong choice ")
    con.close()

