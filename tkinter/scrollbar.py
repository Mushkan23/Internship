from tkinter import *
win = Tk()
scr = Scrollbar(win)
scr.pack(side=RIGHT,fill=BOTH)

listbox = Listbox(win,yscrollcommand=scr.set)

for list in range(45):
    listbox.insert(END,'value' + str(list))

listbox.pack(side=LEFT)

win.mainloop()