import tkinter as tk 
from tkinter import * 

root = tk.Tk()
helv36 = tkFont.Font(family='Helvetica',
size=36, weight='bold')
def bye():
    w.grid_remove()
def hello():
    w.grid()
b = tk.Button(root,text='Click Me',command=hello)
b.grid(row=0)
k = tk.Button(root,text='BYE',command=bye)
k.grid(row=0,column=1)
w = tk.Label(root,text='hello world',)
w.columnconfigure(0,weight=3)
root.mainloop()

