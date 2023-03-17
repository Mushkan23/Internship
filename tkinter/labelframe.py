from tkinter import *
win = Tk()
win.geometry('300x200')

labeframe1 = LabelFrame(win,text='here is the first frsme')
labeframe1.pack(fill=BOTH,expand=YES)

label1 = Label(labeframe1,text='hey!!')
label1.pack()

labeframe2 = LabelFrame(win,text='here is the second frame')
labeframe2.pack(fill=BOTH,expand=YES)

label2 = Label(labeframe2,text='hello...')
label2.pack()

win.mainloop()