from tkinter import *

def donothing():
    filewin = Toplevel()
    button = Button(filewin,text="Do nothing button")
    button.pack()

root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='New',command=donothing)
filemenu.add_command(label='Edit',command=donothing)
filemenu.add_command(label='Open',command=donothing)
filemenu.add_command(label='Save',command=donothing)
filemenu.add_command(label='Save As...',command=donothing)

filemenu.add_separator()

filemenu.add_command(label='Edit',command=root.quit)
menubar.add_cascade(label='File',command=donothing)


filemenu.add_command(label='Cut',command=donothing)
filemenu.add_command(label='Copy',command=donothing)
filemenu.add_command(label='Paste',command=donothing)
filemenu.add_command(label='Delete',command=donothing)

filemenu.add_separator()




root.mainloop()