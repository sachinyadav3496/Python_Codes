__author__ = "sachin yadav"

import tkinter as tk

class Application(tk.Frame):

    def __init__(self,master=None):

        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.quitButton = tk.Button(self,text='Quit',command=self.quit)
        self.quitButton.grid()


if __name__ == "__main__" :
    app = Application()
    app.master.title('Sample Application')
    app.mainloop()


