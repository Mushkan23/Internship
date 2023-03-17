from tkinter import *
win = Tk()
win.geometry('300x200')

lbl = Label(win,text="Languages",font=20)
lbl.pack()

msg = Message(win,text="Hello!!! we are here...",padx=15,pady=20,relief=SUNKEN)
msg.pack()

win.mainloop()