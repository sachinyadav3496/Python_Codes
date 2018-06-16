from tkinter import * 

root = Tk()

l1 = Label(root,text="An eye for an makes whole world blind.\nMahatma Gandhi",bg="#45607c",fg="#000000")
img = PhotoImage(file="../small.gif")
l2 = Label(root,image=img)

l1.grid()
l2.grid()

mainloop()
