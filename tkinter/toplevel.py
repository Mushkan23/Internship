from tkinter import *
win = Tk()
win.geometry('300x200')
def open():
    top = Toplevel(win)
    top.pack()

btn = Button(win,text='open',command=open)
btn.pack()

win.mainloop()