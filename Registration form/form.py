from tkinter import*
from tkinter import ttk
base = Tk()
import re

base.geometry('500x500')
base.title("Registration Form")

labl_0 = Label(base,text="Registration Form",width=20,font=('bold',20))
labl_0.place(x=95,y=52)

labl_1 = Label(base,text='Name',width=20,font=('bold',10))
labl_1.place(x=80,y=130)

entry_1 = Entry(base)
entry_1.place(x=240,y=130)

labl_2 = Label(base,text='Email',width=20,font=('bold',10))
labl_2.place(x=68,y=180)

entry_02 = Entry(base)
entry_02.place(x=240,y=180)

"""def validate_email(entry_02):
    if re.match(r'\b[A-Za-z0-9._]+\.[A-Z|a-z]{2,7}\b',entry_02):
        return True
    return False
if validate_email(entry_02):
    print("valid email")
else:
    print("Invalid email")"""
    
labl_3 = Label(base,text='Gender',width=20,font=('bold',10))
labl_3.place(x=70,y=230)

Radiobutton(base,text="Male",padx=5,value=1).place(x=235,y=230)
Radiobutton(base,text="Female",padx=20,value=2).place(x=290,y=230)

labl_4 = Label(base,text='Age',width=20,font=('bold',10))
labl_4.place(x=70,y=230)

entry_02 = Entry(base)
entry_02.place(x=240,y=180)

btn = Button(base,text='submit',bg='brown',fg='white').place(x=180,y=380)
base.mainloop()
print("Registration form is created successfully.....")

