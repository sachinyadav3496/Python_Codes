import tkinter as tk   #importing tkinter module 

class Application(tk.Frame): #inherting tkinter's frame class


    def __init__(self,master=None):  

        tk.Frame.__init__(self,master) #calling parent class's constructor
        self.grid()  #function which will grid applictaion on screen
        self.createWidgets() 

    
    def createWidgets(self):

        self.quitButton = tk.Button(self,text='Quit',command=self.quit) #creating button labled with Quit
        self.quitButton.grid() #Placing the button in grid


app = Application()

app.master.title('Sample application') #setting master's name
app.mainloop() #Waiting for mouse of keyboard signal
