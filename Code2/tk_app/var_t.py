from tkinter import *

root = Tk()
root.maxsize(400,400)
var = StringVar()
var.set('hello')

l = Label(root,textvariable=var,anchor=NW,justify=LEFT)

l.pack()

t = Entry(root,textvariable = var)

t.pack()

root.mainloop()
