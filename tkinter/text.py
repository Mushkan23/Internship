from tkinter import *
win = Tk()
win.geometry('300x200')

text = Text(win,height=5,width=20)
text.pack()

l = Label(win,text='Write the quote here....')
l.config(font=('courier',14))
l.pack()

b1 = Button(win,text='Next')
b2 = Button(win,text='Exit',command=win.destroy)
b1.pack()
b2.pack()

win.mainloop()