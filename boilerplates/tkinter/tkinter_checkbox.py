from tkinter import *
from tkinter.ttk import *


window = Tk()
window.title("Hello, World!")
window.geometry('250x250')

check_state = BooleanVar()
check_state.set(True) #set check state

check = Checkbutton(window, text='Make a choice!', var=check_state)
check.grid(column=0, row=0)

window.mainloop()