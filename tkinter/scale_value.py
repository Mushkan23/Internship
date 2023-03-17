from tkinter import *
win = Tk()

#define function
def sel():
    selection = 'selected value is: '+ str(var.get())
    label.config(text=selection)

#create widget for scale
var = StringVar()
scale = Scale(win,from_=0,to_=10)
scale.pack()

#create label widget to print the output
label = Label(win,font='helvetica 12 bold')
label.pack()

#create button widget by click it will call the functionn and then we will get the output
btn = Button(win,text='get value',command=sel)
btn.pack()

win.mainloop()