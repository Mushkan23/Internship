from tkinter import*
from tkinter import Tk

win = Tk()
win.geometry('270x170')
win.title('Calculator')
win.configure(background='white')

expression = ''
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:

        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = " "
    equation.set("")

if __name__ == "__main__":
    equation = StringVar()
    expression_field = Entry(win,textvariable= equation)
    expression_field.grid(columnspan=4,ipadx=70)


    C = Button(win,text='C',bg='#fff',fg='white',height=1,width=7,command=lambda:press('C').grid(row=2,column=0))
    dot = Button(win,text='.',bg='#eee',fg='white',height=3,width=10,command=lambda:press('.').grid(row=0,column=1))

    btn7 = Button(win,text=7,fg='white',bg='black',height=8,width=10,command=lambda:press(7).grid(row=1,column=0))
    btn8 = Button(win,text=8,fg='white',bg='black',height=8,width=10,command=lambda:press(8).grid(row=1,column=1))
    btn9 = Button(win,text=9,fg='white',bg='black',height=9,width=10,command=lambda:press(9).grid(row=1,column=2))
    backslash = Button(win,text='/',fg='white',bg='black',height=9,width=10,command=lambda:press('/').grid(row=1,column=3))

    btn4 = Button(win,text=4,fg='white',bg='black',height=3,width=10,command=lambda:press(4).grid(row=2,column=0))
    btn5 = Button(win,text=5,fg='white',bg='black',height=3,width=10,command=lambda:press(5).grid(row=2,column=1))
    btn6 = Button(win,text=6,fg='white',bg='black',height=3,width=10,command=lambda:press(6).grid(row=2,column=2))
    sub = Button(win,text='-',fg='white',bg='black',height=3,width=10,command=lambda:press('-').grid(row=2,column=3))

    btn1 = Button(win,text=1,fg='white',bg='black',height=3,width=10,command=lambda:press(1).grid(row=3,column=0))
    btn2 = Button(win,text=2,fg='white',bg='black',height=3,width=10,command=lambda:press(2).grid(row=3,column=1))
    btn3 = Button(win,text=3,fg='white',bg='black',height=3,width=10,command=lambda:press(3).grid(row=3,column=2))
    add = Button(win,text='+',fg='white',bg='black',height=3,width=10,command=lambda:press('+').grid(row=3,column=3))

    zero = Button(win,text=0,fg='white',bg='black',height=3,width=10,command=lambda:press(0).grid(row=4,column=0))
    mul = Button(win,text='*',fg='white',bg='black',height=3,width=10,command=lambda:press('*').grid(row=4,column=1))
    mode = Button(win,text='%',fg='white',bg='black',height=3,width=10,command=lambda:press('%').grid(row=4,column=2))


    win.mainloop()