from tkinter import*
win = Tk()
win.geometry('300x200')

def print_text(text):
    Label(win,text=text).pack()

btn1  = Button(win,text='button 1',command=lambda:print_text('button 1'))
btn2  = Button(win,text='button 2',command=lambda:print_text('button 2'))

btn1.pack()
btn2.pack()
win.mainloop()
