from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("Hello, World!")
window.geometry('200x250')

def clicked():

    messagebox.showinfo('Messagebox title', 'Message appears here')

btn = Button(window,text='Click for message!', command=clicked)
btn.grid(column=0, row=0)

window.mainloop()