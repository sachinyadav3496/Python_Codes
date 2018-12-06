#animated graph 
from random import randint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
#style.available?
style.use('seaborn') #use fivethirtyeight for different graph style
fig = plt.figure()
plot1 = fig.add_subplot(1,1,1)

data = [ randint(1,100) for var in range(30)]
x = [ var for var in range(30)]
print(data)
print(x)
def animate(i):
    global data,x
    data.append(randint(1,100))
    x.append(x[-1] + 1)
    plot1.clear()
    plot1.plot(x,data)
    
ani = animation.FuncAnimation(fig,animate,interval=1000)
plt.show()
    
