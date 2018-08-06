__author__ = 'sachin yadav'
import pymysql as sql
try :
    db = sql.connect('localhost','root','','bank')
    c = db.cursor()
except Exception as e:
    print("Error:!!",e)

from tkinter import *
root = Tk()
uname = StringVar()
upasswd = StringVar()
root.title("Bank App")
root.geometry("400x400")
root.wm_maxsize(400,400)
root.wm_minsize(400,400)

fr = Frame(root)
lb1 = Label(fr,text="Python Bank",bg='green')
lb1.grid(row=5,column=5)

lb2 = Label(fr,text="UserName:",bg='green')
lb2.grid(row=5,column=5)
lb3 = Label(fr,text="Password:",bg='green')
lb3.grid(row=6,column=5)

e1 = Entry(fr,textvar=uname,bg='green')
e2 = Entry(fr,textvar=upasswd,bg='green')

e1.grid(row=5,column=6)
e2.grid(row=6,column=6)

def Login():
    name = uname.get()
    passwd = upasswd.get()
    uname.set('')
    upasswd.set('')
    if name and passwd :
        cmd  = 'select * from  data where name="%s"'%(name)
        c.execute(cmd)
        v_data = c.fetchone()
        if v_data :
            if passwd == v_data[2] :
                r = Tk()
                r.maxsize(400,400)
                r.minsize(400,400)
                fr = Frame(r)
                lable = Label(fr,text="Welcome Back %s "%(v_data[0].upper()),bg='green')
                lable.grid(row=0,column=5,columnspan=5)
                def Credit():
                    pass
                nb1 = Button(fr,text="CREDIT",bg='green',command=Credit)
                def Debit():
                    pass
                nb2 = Button(fr,text="Debit",bg='green',command=Debit)

                nb1.grid(row=1,column=5,columnspan=5)
                nb2.grid(row=2,column=5,columnspan=5)



                fr.pack()
                b1 = Button(r,text="Quit",bg='green',command=r.destroy)
                b1.pack()
                r.mainloop()
            else :
                lable = Label(fr,text="Incorrect Password Try again ",bg='green')
                lable.grid(row=9,column=5,columnspan=8)


        else :
            lable = Label(fr,text="No Such User Exist in Our System Try Again ",bg='green')
            lable.grid(row=9,column=5)
    else :
        lable = Label(fr,text="Please input UserName and Password Both ",bg='green')
        lable.grid(row=9,column=5)

def SignUp():
    pass

b1 = Button(fr,text='Login',bg='green',command=Login)
b2 = Button(fr,text='Quit',bg='green',command=root.destroy)
b3 = Button(fr,text='Open New Account',bg='green',command=SignUp)

b1.grid(row=7,column=5)
b2.grid(row=7,column=7)
b3.grid(row=7,column=6)
fr.pack()
root.mainloop()
