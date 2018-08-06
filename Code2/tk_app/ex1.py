import tkinter as tk

root = tk.Tk()

def hello():
    root2 = tk.Tk()

    l = tk.Label(root2,text="Hello how are you ",bg="#666666",fg="#FFFFFF")
    l.grid()
    b = tk.Button(root2,text="Bye!!",command=quit)
    b.grid()
    tk.mainloop()

b1 = tk.Button(root,command=quit,text="Quit")
b2 = tk.Button(root,command=hello,text="hello")


b1.grid(row=1,column=0)
b2.grid(row=0,column=0)


tk.mainloop()
