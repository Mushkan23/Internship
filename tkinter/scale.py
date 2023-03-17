from tkinter import*
win = Tk()
win.geometry('300x200')
scale = Scale(win,from_=0,to_=10,orient=HORIZONTAL,troughcolor='darkgreen',tickinterval=5,sliderlength=40)
scale.pack()

btn = Button(win,text='value')
btn.pack()

win.mainloop()