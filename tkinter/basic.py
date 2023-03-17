import tkinter
from tkinter import Button
top = tkinter.Tk()
btn = Button(top,text='submit',background='red')
btn.pack(side="left",pady=46,padx=56)

#we can simply used the button by defining the sides.
"""btn1 = Button(top,text='submit',background='red')
btn1.pack(side="right")

btn2 = Button(top,text='submit',background='red')
btn2.pack(side="top")

btn3 = Button(top,text='submit',background='red')
btn3.pack(side="bottom")"""

top.mainloop()