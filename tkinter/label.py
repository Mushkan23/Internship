from tkinter import *
root = Tk()

var = StringVar()
label = Label(root,textvariable=var)
var.set('hello!!!')
label.pack(side='left')
root.mainloop()