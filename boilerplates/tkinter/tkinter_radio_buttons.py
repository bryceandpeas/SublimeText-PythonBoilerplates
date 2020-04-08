from tkinter import *
from tkinter.ttk import *


window = Tk()
window.title("Hello, World!")
window.geometry('350x250')

radio_1 = Radiobutton(window,text='First Option', value=1)
radio_2 = Radiobutton(window,text='Second Option', value=2)
radio_3 = Radiobutton(window,text='Third Option', value=3)

radio_1.grid(column=0, row=0)
radio_2.grid(column=1, row=0)
radio_3.grid(column=2, row=0)

window.mainloop()