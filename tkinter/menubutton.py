from tkinter import *
root = Tk()
import tkinter.messagebox

mn = Menubutton(root,text='languages',bg='red')
mn.grid()
mn.menu = Menu(mn)
mn['menu'] = mn.menu

mn.checkbox = Checkbutton(text='python',bg='yellow')
mn.checkbox = Checkbutton(text='Java',bg='yellow')
mn.menu.add_checkbutton(label="java")
mn.menu.add_checkbutton(label="Python")
mn.pack()

root.mainloop()