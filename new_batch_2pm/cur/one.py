from curses import wrapper

def main(stdscr):

    stdscr.clear()
    for i in range(1,9) :
        v = i-10
        stdscr.addstr(i,0,'10 divided by {} is {}'.format(v,10/v))
    stdscr.refresh()
    stdscr.getkey()
wrapper(main)
