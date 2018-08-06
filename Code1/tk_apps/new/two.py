from tkinter import * 

root = Tk()

var = StringVar()

w = Label(root,text="Messege")
w.grid(row=0)
e1 = Entry(root,textvariable=var)
e1.grid(row=0,column=1)

def show():
 
b = Button(root,text='show messege',command=show)
