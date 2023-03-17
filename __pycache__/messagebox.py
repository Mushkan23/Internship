from tkinter import*
from tkinter import messagebox

win = Tk()
win.geometry('300x200')

#msg = messagebox.showwarning('Warning','Something wrong')
#msg = messagebox.showerror('Error','Error occur')
#msg = messagebox.showinfo('Important','password sholud contain 12 characters')
#msg = messagebox.askretrycancel('try or wait','retry or close the app')
msg = messagebox.askquestion('confirm',"Are you sure")

msg.pack()
win.mainloop()