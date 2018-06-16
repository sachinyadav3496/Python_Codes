from tkinter import *
root = Tk()
img = PhotoImage(file="../small3.gif")
txt = """
if you love yourself then trust me
Everthing will love you as you do 
enjoy loving everthing in your life
you are a creature which is awesome
so let's do some awesome work out here"""
w = Label(root,compound=CENTER,text=txt,bg='light blue',font='Times 30 bold',fg='red',padx=30,image=img).pack(side='right')
root.mainloop()
