from tkinter import*
root = Tk()

frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side='bottom')

redbtn = Button(root,text='submit',bg='red')
redbtn.pack(side='left')
bluebtn = Button(root,text='submit',bg='blue')
bluebtn.pack(side='right')
greenbtn = Button(root,text='submit',bg='green')
greenbtn.pack(side='bottom')
root.mainloop()