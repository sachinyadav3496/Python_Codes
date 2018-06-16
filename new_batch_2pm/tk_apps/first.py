from tkinter import * 

root = Tk()

frame = Frame(root)

l = Label(frame,text="Hello World IN Tkinter")

b = Button(frame,text="Quit", command=frame.destroy)

b1 = Button(root,text="Quit",command=root.destroy)

l.pack()
b.pack()
frame.pack()
b1.pack()
root.mainloop()

