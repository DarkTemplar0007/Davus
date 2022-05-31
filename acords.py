
from tkinter import *
import random

condition = False
t = int(1000)


def acords():
    acords_list = ["C", "D", "E", "F", "G", "A", "H", "Cmi", "Dmi", "Emi", "Fmi", "Gmi", "Ami", "B", "C7",
                   "D7", "E7", "F7", "G7", "A7", "H7"]
    return random.choice(acords_list)


def display():
    l["text"] = str(acords())
    if condition:
        l.after(t, display)


def start():
    global condition
    condition = True
    display()


def stop():
    global condition
    condition = False


window = Tk()
window.title("Davus")
window.configure(bg='white')
# centering on the middle
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# window size and position
window_width = 250
window_height = 350

xcord = int(screen_width / 2 - window_width / 2)
ycord = int(screen_height / 2 - window_height / 2)

# set the size of window
window.geometry(f'{window_width}x{window_height}+{xcord}+{ycord}')
window.resizable(False, False)

# widgets
l = Label(window, text="0", font='Arial, 40', bg='white')

start_button = Button(window,
                      text='Start',
                      command=lambda: start())

stop_button = Button(window,
                     text='Stop',
                     command=lambda: stop())

exit_button = Button(window,
                     text='Exit',
                     command=lambda: window.quit())
# pause_play_button = Button(window, text=)

# initialise widgets
exit_button.pack(ipadx=5,
                 ipady=0,
                 fill='x',
                 side='top',
                 expand=False
                 )

start_button.pack(ipadx=5,
                  ipady=0,
                  fill='x',
                  expand=False,
                  side='bottom'
                  )

stop_button.pack(ipadx=5,
                 ipady=0,
                 fill='x',
                 expand=False,
                 side='bottom'
                 )

l.pack(ipady=5)

window.mainloop()
