from tkinter import *
from tkinter.ttk import *


window = Tk()
window.title("Hello, World!")
window.geometry('500x250')

def clicked():

	lbl.configure(text=str(selected.get()))

selected = IntVar()

radio_1 = Radiobutton(window,text='First Option', value=1, variable=selected)
radio_2 = Radiobutton(window,text='Second Option', value=2, variable=selected)
radio_3 = Radiobutton(window,text='Third Option', value=3, variable=selected)

lbl = Label(window, text="Option Placeholder")

btn = Button(window, text="Click Me!", command=clicked)

radio_1.grid(column=0, row=0)
radio_2.grid(column=1, row=0)
radio_3.grid(column=2, row=0)
btn.grid(column=0, row=1)
lbl.grid(column=0, row=2)

window.mainloop()