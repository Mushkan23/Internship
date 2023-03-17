from tkinter import *
from tkinter import ttk
win = Tk()
win.geometry('300x200')

bar = ttk.Progressbar(win,orient=HORIZONTAL,mode ='indeterminate')
bar.pack()

win.mainloop()