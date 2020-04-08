from tkinter import *
from tkinter import Menu

window = Tk()
window.title("Hello, World!")
window.geometry('250x250')

menu = Menu(window)
new_menu_item = Menu(menu)
new_menu_item.add_command(label='New')
new_menu_item.add_separator()
new_menu_item.add_command(label='Edit')
menu.add_cascade(label='File', menu=new_menu_item)
window.config(menu=menu)

window.mainloop()