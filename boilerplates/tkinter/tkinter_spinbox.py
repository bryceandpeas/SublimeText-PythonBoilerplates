from tkinter import *


window = Tk()
window.title("Hello, World!")
window.geometry('250x250')

spinbox = Spinbox(window, from_=0, to=100, width=5)
spinbox.grid(column=0,row=0)

window.mainloop()