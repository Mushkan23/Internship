from tkinter import*
top = Tk()

l1 = Label(top,text="Full Name")
l1.pack(side='left')
e1 = Entry(top,bd=5,relief=FLAT,border=2,borderwidth=5,selectbackground='green',show="*")#selectbackground is used when we are copying some selected text then it will change colour.
e1.pack(side='left')

top.mainloop()