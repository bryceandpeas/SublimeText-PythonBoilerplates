from tkinter import *


window = Tk()
window.title("Hello, World!")
window.geometry('250x250')

lbl = Label(window, text="Hello, World!")
lbl.grid(column=0, row=0)

def clicked():

    lbl.configure(text="Goodnight, World!")

btn = Button(window, text="Click Me!", command=clicked)
btn.grid(column=1, row=0)

window.mainloop()