from tkinter import *
import tkinter.messagebox
base = Tk()


choice1 = Checkbutton(base,text='audio',cursor='dot',selectcolor='pink',width=20,onvalue=1,height=5 )
choice2 = Checkbutton(base,text='video',cursor='arrow',selectcolor='pink',width=20,onvalue=1,height=5 )
choice1.pack()
choice2.pack()

base.mainloop()