#dynamic content in Label
from tkinter import *
c = 0
def c_label(label):
    c = 0
    def count():
        global c
        c += 1
        label.config(text=str(c))
        label.after(1000,count)
    count()
root = Tk()
root.title("Counting Seconds ")
label=Label(root,bg='black',fg='dark green')
label.pack()
c_label(label)
button=Button(root,text="Stop",width=25,command=root.destroy)
button.pack()
root.mainloop()