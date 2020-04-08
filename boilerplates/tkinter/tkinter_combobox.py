from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Hello, World!")
window.geometry('250x250')

combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=0, row=0)

window.mainloop()