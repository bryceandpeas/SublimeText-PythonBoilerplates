from tkinter import *
from tkinter import scrolledtext


window = Tk()
window.title("Hello, World!")
window.geometry('200x250')

txt = scrolledtext.ScrolledText(window, width=40, height=10)
txt.insert(INSERT,'Keep scrolling, scrolling, scrolling, scrolling...')
txt.grid(column=0, row=0)

window.mainloop()