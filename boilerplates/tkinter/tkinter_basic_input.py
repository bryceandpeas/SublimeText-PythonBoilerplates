from tkinter import *

window = Tk()
window.title("Hello, World!")
window.geometry('250x250')

lbl = Label(window, text="Hello, World!")
lbl.grid(column=0, row=0)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)

def clicked():

    input_text = txt.get()
    lbl.configure(text=input_text)

btn = Button(window, text="Click Me!", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()