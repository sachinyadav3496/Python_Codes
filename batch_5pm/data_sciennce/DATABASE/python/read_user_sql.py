import pymysql as sql 


def query():
    db = sql.connect(user='student',password='student',database='student')
    c = db.cursor()
    sid = int(input("Enter sid : "))
    cmd = f"select * from student where sid='{sid}'"
    c.execute(cmd)
    data = c.fetchone()
    data  = f"""
        Name        =  {data[1]}
        Student ID  =  {data[0]}
        Phone No    =  {data[2]}
        Email       =  {data[3]}

        """

    print(data)

    if input("\n\nFor Quires Press Any key else press enter") : 
        query()



if __name__ == "__main__" : 

    try : 
        query()
    except TypeError as e : 
        print("No such Student Available")
        query()
    except Exception as e : 
        print("Something Went wrong ",e)
        query()
