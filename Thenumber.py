import tkinter as tk
from tkinter import ttk

def btn_Clicked(Button):
    strShow.set(entLogin.get() + str(Button))

def Clear_entry():
    strShow.set("")


root = tk.Tk()
root.title("TheNumber")
root.geometry('500x300+100+200')



strShow=tk.StringVar()
entLogin=ttk.Entry(root,font=("tahoma",12),textvariable=strShow)
entLogin.place(x=300,y=100)
entLogin.focus()

btn1=ttk.Button(root,text='1',command=lambda:btn_Clicked(1)).place(x=10,y=50) 
btn2=ttk.Button(root,text='2',command=lambda:btn_Clicked(2)).place(x=110,y=50)
btn3=ttk.Button(root,text='3',command=lambda:btn_Clicked(3)).place(x=210,y=50)
btn4=ttk.Button(root,text='4',command=lambda:btn_Clicked(4)).place(x=10,y=110)
btn5=ttk.Button(root,text='5',command=lambda:btn_Clicked(5)).place(x=110,y=110)
btn6=ttk.Button(root,text='6',command=lambda:btn_Clicked(6)).place(x=210,y=110)
btn7=ttk.Button(root,text='7',command=lambda:btn_Clicked(7)).place(x=10,y=170)
btn8=ttk.Button(root,text='8',command=lambda:btn_Clicked(8)).place(x=110,y=170)
btn9=ttk.Button(root,text='9',command=lambda:btn_Clicked(9)).place(x=210,y=170)
btn0=ttk.Button(root,text='0',command=lambda:btn_Clicked(0)).place(x=210,y=230)
btnClear=ttk.Button(root,text='Clear',command=lambda:Clear_entry()).place(x=10,y=200)

   
root.mainloop()

