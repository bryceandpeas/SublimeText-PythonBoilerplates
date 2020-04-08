from tkinter import messagebox

message = messagebox.askquestion('Question Title', 'Message Appears Here')
message = messagebox.askyesno('Yes No Title', 'Message Appears Here')
message = messagebox.askyesnocancel('Yes No Cancel Title', 'Message Appears Here')
message = messagebox.askokcancel('Ok To Cancel Title', 'Message Appears Here')
message = messagebox.askretrycancel('Retry Title', 'Message Appears Here')