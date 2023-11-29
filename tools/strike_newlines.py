#import curses
#from curses import wrapper
#from curses.textpad import Textbox, rectangle
import pyperclip

#stdscr = curses.initscr()
#curses.start_color()

def text_box(stdscr):
    stdscr.addstr(0, 0, "ctrl+G to strip out newlines")
    b_nlines = 20
    #should be adjustable between ssh from terminal and phone view from u0_a299, option for this should be added 
    b_ncols = 150
    editwin = curses.newwin(b_nlines,b_ncols, 2,1)
    rectangle(stdscr, 1,0, 1+b_nlines+1, 1+b_ncols+1)
    stdscr.refresh()

    #box = Textbox(editwin)

    # Let the user edit until Ctrl-G is struck.
    #box.edit()

    # Get resulting contents
    #message = box.gather()
    message = pyperclip.paste()
    print("TESTING\n", message)
    stdscr.refresh()
    #Pause before ending program
    mod_message = message.replace("\n", "")
    stdscr.clear()
    stdscr.addstr(mod_message)
    pyperclip.copy(message.replace("\n", ""))
    stdscr.refresh()
    #wait
    curses.napms(2000)

#wrapper(text_box)
message = pyperclip.paste()
mod_message = message.replace("\n", "")
pyperclip.copy(message.replace("\n", ""))

