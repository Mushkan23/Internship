from tkinter import *
win = Tk()
win.geometry('200x100')

label = Label(win,text='select here..',fg='lightgreen',font=50)
label.pack()

spin = Spinbox(win,from_=0,to_=10)
spin.pack()

win.mainloop()