from tkinter import *
win = Tk()
win.geometry('300x200')

def addition():
    x = int(e1.get())
    y = int(e2.get())
    leftdata = str(x+y)
    leftinput.input(1, leftdata)

w1 = PanedWindow()
w1.pack(fill=BOTH,expand=1)

leftinput = Entry(w1,bd=5)
w1.add(leftinput)

w2 = PanedWindow()
w1.add(w2)

e1 = Entry(w2)
e2 = Entry(w2)

w2.add(e1)
w2.add(e2)

btn = Button(w2,text='Addition',command=addition)
w2.add(btn)

win.mainloop()