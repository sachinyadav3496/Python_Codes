import curses
stdscr = curses.initscr()
#begin_x = 20; begin_y = 7
#height=5;width=40
#win = curses.newwin(height,width,begin_y,begin_x)
pad = curses.newpad(100,100)
for y in range(0,99) :
    for x in range(0,99) :
        pad.addch(y,x,ord('a')+(x*x+y*y)%26)

pad.refresh(0,0,5,5,20,75)
