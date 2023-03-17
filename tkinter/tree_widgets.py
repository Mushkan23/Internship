import tkinter as t
from tkinter import ttk
from tkinter.messagebox import showinfo
root_window = t.Tk()
root_window.geometry(600,520)
root_window.title("Treeview widget")
description = ("Sr.no","Name","Phone Number")
tree = ttk.Treeview