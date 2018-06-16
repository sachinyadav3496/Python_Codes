from tkinter import *
x = ''
root = Tk()
var = StringVar()

l = Label(root,text="Expression = ",)
l.grid(row=0,column=0)
e = Entry(root,textvariable=var)
e.grid(row=0,column=1)

def var_set(v):
    global x 
    x += v
    var.set(x)

def clr_func():

    var.set('')

def eval_func():
    global x 
    x = ''
    r = e.get()
    var.set(eval(r))
    
bp = Button(root,text="+",command=lambda:var_set('+'),width=16,height=2)
bp.grid(row=1,column=3)
bs = Button(root,text="-",command=lambda:var_set('-'),width=16,height=2)
bs.grid(row=2,column=3)
bm = Button(root,text="*",command=lambda:var_set('*'),width=16,height=2)
bm.grid(row=3,column=3)
bd = Button(root,text="/",command=lambda:var_set('/'),width=16,height=2)
bd.grid(row=4,column=3)

b9 = Button(root,text="9",command=lambda:var_set('9'),width=16,height=2)
b8 = Button(root,text="8",command=lambda:var_set('8'),width=16,height=2)
b7 = Button(root,text="7",command=lambda:var_set('7'),width=16,height=2)
b6 = Button(root,text="6",command=lambda:var_set('6'),width=16,height=2)
b5 = Button(root,text="5",command=lambda:var_set('5'),width=16,height=2)
b4 = Button(root,text="4",command=lambda:var_set('4'),width=16,height=2)
b3 = Button(root,text="3",command=lambda:var_set('3'),width=16,height=2)
b2 = Button(root,text="2",command=lambda:var_set('2'),width=16,height=2)
b1 = Button(root,text="1",command=lambda:var_set('1'),width=16,height=2)
b0 = Button(root,text="0",command=lambda:var_set('0'),width=16,height=2)


b10 = Button(root,text=".",command=lambda:var_set('.'),width=16,height=2)
b11 = Button(root,text="=",command=lambda:eval_func(),width=16,height=2)


clr = Button(root,text="CLR",command=lambda:clr_func(),width=16,height=2)
clr.grid(row=5,column=1)

b9.grid(row=1,column=0)
b8.grid(row=1,column=1)
b7.grid(row=1,column=2)
b6.grid(row=2,column=0)
b5.grid(row=2,column=1)
b4.grid(row=2,column=2)
b3.grid(row=3,column=0)
b2.grid(row=3,column=1)
b1.grid(row=3,column=2)
b0.grid(row=4,column=1)

b10.grid(row=4,column=0)
b11.grid(row=4,column=2)


root.wm_minsize(500,250)
root.wm_maxsize(500,250)
mainloop()
