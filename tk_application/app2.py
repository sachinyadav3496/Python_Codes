__author__ = 'sachin yadav'

import tkinter as tk

class Application(tk.Frame):

    def __init__(self,master=None):

        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        top = self.winfo_toplevel()
        top.columnconfigure(0,weight=1)
        top.rowconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.quitButton = tk.Button(self,text='Quit',command=self.quit)
        self.quitButton.grid(row=0,column=0,sticky=tk.N+tk.S+tk.E+tk.W)


if __name__ == "__main__" :
    app = Application()
    app.master.title('Sample Application')
    app.mainloop()



