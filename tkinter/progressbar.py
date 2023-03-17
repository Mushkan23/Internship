from tkinter import *
from tkinter import ttk
win = Tk()

win.grid()

bar = ttk.Progressbar(win,length=280,mode ='indeterminate')
bar.grid(column=1,row=1,padx=20,pady=20)

start_button = ttk.Button(win,text='Start',command=bar.start)
start_button.grid(column=1,row=1,padx=10,pady=10,sticky=E)

stop_button = ttk.Button(win,text='Stop',command=bar.stop)
stop_button.grid(column=1,row=1,padx=10,pady=10,sticky=W)



win.mainloop()