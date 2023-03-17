from tkinter import *
root = Tk()
import tkinter.messagebox

mn = Menubutton(root,text='languages',bg='red')
mn.grid()
mn.menu = Menu(mn)
mn['menu'] = mn.menu

mn.checkbox = Checkbutton(text='python',bg='yellow')
mn.checkbox = Checkbutton(text='Java',bg='yellow')
mn.menu.add_checkbutton(label="Python")
mn.menu.add_checkbutton(label="Python")
mn.pack()


list = Listbox(root,selectmode=MULTIPLE)
l1 = list.insert(1,'python')
l1 = list.insert(2,'Javascipt')
l1 = list.insert(3,'Java')
l1 = list.insert(4,'Kotlin')
l1 = list.insert(5,'C#')

list.pack()
root.mainloop()
