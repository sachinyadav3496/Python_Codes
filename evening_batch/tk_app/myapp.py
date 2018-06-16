from tkinter import *

root = Tk()
var = StringVar()
var.set('hello')

e = Entry(root)
e.pack()

def new_window(var):
    
    root1 = Tk()
    l = Label(root1,text=var).pack()
    mainloop()


def set_value():
    var.set(e.get())
    k = var.get()
    print(k)
    new_window(k)
b = Button(root,text="Submit",command=set_value)

b.pack()
root.wm_minsize(400,400)
root.wm_maxsize(400,400)

mainloop()
