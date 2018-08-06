__author__ = 'sachin yadav'
from tkinter import *

root = Tk()
def hide():
    fr.grid_forget()
fr = Frame(root)
label1 = Label(fr,text="Welcome to Tkinter")
label1.pack()
def show():
    fr.grid()
b1 = Button(root,text="Show",command=show)
b2 = Button(root,text="Hide",command=hide)
b2.grid(row=0,column=1)
b1.grid(row=0)

root.mainloop()