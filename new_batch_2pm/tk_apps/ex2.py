import tkinter as tk 

def hello_world():
    f2 = tk.Frame(root)
    label = tk.Label(f2,text="Hello World")
    label.pack()
    f2.pack()

root = tk.Tk()
frame1 = tk.Frame(root)
root.title("Hello World")
lb = tk.Label(frame1,text="Hello World")
b = tk.Button(frame1,text="Say Hello",command=hello_world)


lb.pack(anchor='center')
b.pack(anchor='s')
frame1.pack(anchor='ne')



tk.mainloop()
