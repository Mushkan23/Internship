from tkinter import*
base = Tk()

btn = Button(base,text='submit',activebackground='blue',activeforeground='black',fg='grey',bg='purple',font=45,
             bd=8,highlightcolor='white',relief='sunken',state='active')#state='disabled'
#relief type can be :(raised,groove,sunken,ridge)
btn.pack()

#btn.pack(fill=BOTH,expand=1)

mainloop()