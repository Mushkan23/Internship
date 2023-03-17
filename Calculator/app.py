from tkinter import*
from tkinter import Tk

win = Tk()
win.geometry('750x500')
win.resizable(0,0)
win.title('Calculator')

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = " "
    input_text.set("")

input_text = StringVar()
expression = " "

input_frame = Frame(win,width=312,height=50,bd=0,highlightbackground='black',highlightthickness=2,highlightcolor='black')
input_frame.pack(side=TOP)

input_field = Entry(input_frame,textvariable='input_text',width=50,bd=0,bg='#eee',justify=RIGHT)
input_field.pack(row=0,column=0)

btns_frame = Frame(win,width=312,height=272.5)
btns_frame.pack()



C = Button(win,text='C',bg='#fff',fg='black',height=7,width=32,bd=0,cursor='hand2',command=lambda:btn_click('C').grid(row=0,column=0,padx=1,pady=1))
dot = Button(win,text='.',bg='#eee',fg='black',height=3,width=10,bd=0,cursor='hand2',command=lambda:btn_click('.').grid(row=0,column=1,padx=1,pady=1))

btn7 = Button(win,text=7,fg='black',bg='#fff',height=8,width=10,bd=0,cursor='hand2',command=lambda:btn_click(7).grid(row=1,column=0,padx=1,pady=1))
btn8 = Button(win,text=8,fg='black',bg='#fff',height=8,width=10,bd=0,cursor='hand2',command=lambda:btn_click(8).grid(row=1,column=1,padx=1,pady=1))
btn9 = Button(win,text=9,fg='black',bg='#fff',height=9,width=10,bd=0,cursor='hand2',command=lambda:btn_click(9).grid(row=1,column=2,padx=1,pady=1))
backslash = Button(win,text='/',fg='black',bg='#eee',height=9,width=10,bd=0,cursor='hand2',command=lambda:btn_click('/').grid(row=1,column=3,padx=1,pady=1))

btn4 = Button(win,text=4,fg='black',bg='#fff',height=3,width=10,bd=0,cursor='hand2',command=lambda:btn_click(4).grid(row=2,column=0,padx=1,pady=1))
btn5 = Button(win,text=5,fg='black',bg='#fff',height=3,width=10,bd=0,cursor='hand2',command=lambda:btn_click(5).grid(row=2,column=1,padx=1,pady=1))
btn6 = Button(win,text=6,fg='black',bg='#fff',height=3,width=10,bd=0,cursor='hand2',command=lambda:btn_click(6).grid(row=2,column=2,padx=1,pady=1))
sub = Button(win,text='-',fg='black',bg='#eee',height=3,width=10,bd=0,cursor='hand2',command=lambda:btn_click('-').grid(row=2,column=3,padx=1,pady=1))

btn1 = Button(win,text=1,fg='black',bg='#fff',height=3,width=10,bd=0,cursor='hand2',command=lambda:btn_click(1).grid(row=3,column=0,padx=1,pady=1))
btn2 = Button(win,text=2,fg='black',bg='#fff',height=3,width=10,bd=0,cursor='hand2',command=lambda:btn_click(2).grid(row=3,column=1,padx=1,pady=1))
btn3 = Button(win,text=3,fg='black',bg='#fff',height=3,width=10,bd=0,cursor='hand2',command=lambda:btn_click(3).grid(row=3,column=2,padx=1,pady=1))
add = Button(win,text='+',fg='black',bg='#eee',height=3,width=10,bd=0,cursor='hand2',command=lambda:btn_click('+').grid(row=3,column=3,padx=1,pady=1))

zero = Button(win,text=0,fg='black',bg='#fff',height=3,width=10,bd=0,cursor='hand2',command=lambda:btn_click(0).grid(row=4,column=0,padx=1,pady=1))
mul = Button(win,text='*',fg='black',bg='#eee',height=3,width=10,bd=0,cursor='hand2',command=lambda:btn_click('*').grid(row=4,column=1,padx=1,pady=1))
mode = Button(win,text='%',fg='black',bg='#eee',height=3,width=10,bd=0,cursor='hand2',command=lambda:btn_click('%').grid(row=4,column=2,padx=1,pady=1))



C.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()
btn7.pack()
btn8.pack()
mul.pack()
add.pack()
sub.pack()
mode.pack()
zero.pack()
backslash.pack()

win.mainloop()