from tkinter import * 
import pymysql as sql

name = ''
price = 0

root = Tk()
var1 = StringVar()
var1.set('')

var2 = StringVar()
var2.set('')


var3 = StringVar()



try :

    db = sql.connect('localhost','root','','home_stuff')
    print("Got Connected to the databases")
    c = db.cursor()
    c.execute("select sum(price) from daily_expenses")
    var3.set(c.fetchone())

except Exception as e:

    print("Connection Failed to databases due to, ",e)

def exp():

    c.execute("select sum(price) from daily_expenses")
    var3.set(c.fetchone())

def submit():
    name = e1.get()
    price = e2.get()
    if str(name) and int(price):

        cmd = "insert into daily_expenses(name,price) values('%s',%d)"%(str(name),int(price))
        var1.set('')
        var2.set('')
    else:
        print("Error!!!!")
        var1.set("Error")
        var2.set("Error")

    c.execute(cmd)
    db.commit()
    exp()


def show():

    root2 = Tk()
    scrollbar = Scrollbar(root2)
    scrollbar.pack( side = RIGHT,fill= 'y' )
    mylist = Listbox(root,yscrollcommand = scrollbar.set)


    print("Welcome to show program")
    c.execute("select * from daily_expenses")
    data = c.fetchall()
    s = ''
    for id,date,name,price in data:
       s+=str(id)+'\t'+str(date)+'\t'+str(price)+'\t'+str(name) #+'\n'
       mylist.insert(END,s)
        #s+= "{:2s}{:5s}{:30s}{:5s}\n".format(str(id),str(price),str(date),str(name))
    print(s)
    #f = Label(root2,text=s,justify=LEFT,bg='#606060',fg='#FFFFFF')
    #f.pack()
    mylist.pack( side = LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)
    #b = Button(root2,text="!QUIT!",command=root2.destroy,bg='#808080',fg='#FFFFFF',height=1,width=10)
    #b.pack()
    root2.title("Details")
    root2.title("MY_DAILY_EXPENSES")
    root2.config(bg="#606060")
    root2.wm_minsize(height=200,width=400)
    root2.mainloop

def exit_tk():

    db.commit()
    db.close()
    root.destroy()
    



l1 = Label(root,text='Name of Items = ',bg="#ABCDEF")
e1 = Entry(root,textvariable=var1,bg='#CCCCCC',fg="#880005",width=45)


l1.grid(row=0,column=0,columnspan=4,rowspan=3)
e1.grid(row=0,column=5,columnspan=4,rowspan=3)

l2 = Label(root,text='Price = ',bg="#ABCDEF")
e2 = Entry(root,textvariable=var2,bg="#CCCCCC",fg="#880005",width=50)


l2.grid(row=4,column=0,columnspan=4,rowspan=3)
e2.grid(row=4,column=5,columnspan=4,rowspan=3)

b1=Button(root,text="Quit",width=6,height=1,bg="#FF0000",command=lambda:exit_tk())
b1.grid(row=12,column=5,columnspan=4,rowspan=3)

b2 = Button(root,text="!!!Save!!!",bg="#808080",width=10,height=1,command=lambda:submit())
b2.grid(row=8,column=5,columnspan=4,rowspan=3)


b3 = Button(root,text='Show Details',height=1,width=20,command=lambda:show(),bg="#808080")
b3.grid(row=25,column=6)

l3 = Label(root,text='total Expenses till now =',bg="#ABCDEF")
l3.grid(row=20,column=0,columnspan=4,rowspan=3)

e3 = Entry(root,textvariable=var3,width=25,bg="#CCCCCC")
e3.grid(row=20,column=5,columnspan=3,rowspan=3)


b4 = Button(root,text='Refresh',height=1,width=10,command=lambda:exp(),bg="#808080")
b4.grid(row=20,column=8)


root.title("MY_DAILY_EXPENSES")
root.config(bg="#606060")
root.wm_minsize(height=200,width=400)
root.mainloop()
