from tkinter import *
top = Tk()

#use to create a arc in canvas
"""C = Canvas(top,bg='white',height=250, width=300)
coord = 10,50, 240, 210
arc = C.create_arc(coord,start=0,extent = 150,fill='blue')
C.pack()"""

C = Canvas(top,bg="white",height=250,width=300)
line = C.create_line(12,4,3,2,9,bg='green')
line.pack()
top.mainloop()