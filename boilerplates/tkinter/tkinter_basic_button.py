from tkinter import *


window = Tk()
window.title("Hello, World!")

btn = Button(window, text="Click Me!")
btn.grid(column=1, row=0)

window.mainloop()