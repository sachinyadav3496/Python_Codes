import tkinter as tk

r = tk.Tk()

f = tk.Frame(r)
f1 = tk.Frame(r)

l1 = tk.Label(r,text="Just For Fun",fg='red')
l2 = tk.Label(f,text='I am a frame1')
l3 = tk.Label(f1,text='I am a frame2')

b2 = tk.Button(f,text='Hide ME1',command=f.grid_forget)
b1 = tk.Button(r,text='!!EXIT!!',command=r.destroy)
b1.grid(row=9,column=0,columnspan=3,ipadx=20,ipady=20,padx=20,pady=20)
b11 = tk.Button(r,text='Show1',command=f.grid)
b11.grid(row=8,column=0,columnspan=3,ipadx=20,ipady=20,padx=20,pady=20)
b12 = tk.Button(r,text='Show2',command=f1.grid)
b12.grid(row=7,column=0,columnspan=3,ipadx=20,ipady=20,padx=20,pady=20)

l3.pack()
l2.pack()
b2.pack()


b3 = tk.Button(f1,text='Hide Me2',command=f1.grid_forget)
b3.pack()

f.grid(row=0,rowspan=3,column=0,columnspan=3)
f1.grid(row=3,rowspan=3,column=0,columnspan=3,ipadx=20,ipady=20,padx=20,pady=20)


r.mainloop()


