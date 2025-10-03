import tkinter as tk 
from tkinter import ttk,messagebox

def btn_Clicked(num):
    #labshow["text"]=f"buttom{num} is Clicked"
    messagebox.showinfo("888",f"button{num} is Cliked")

def showLogin(event):
    #messagebox.showinfo("",f"Text From Entry is {entLogin.get()} ")
    strShow.set(entLogin.get())
root = tk.Tk()
root.title("888")
root.geometry('500x300+100+200')

labshow=ttk.Label(root,text="Hello World")
labshow.pack()



entLogin=ttk.Entry(root)
entLogin.place(x=10,y=100)
entLogin.focus()
entLogin.bind("<Return>",showLogin)

strShow=tk.StringVar()
entshow=ttk.Entry(root,textvariable=strShow)
entshow.place(x=300,y=100)

btn1=ttk.Button(root,text="button1",command=lambda:btn_Clicked(1))
btn1.place(x=10,y=200)

btn2=ttk.Button(root,text="button2",command=lambda:btn_Clicked(2))
btn2.place(x=100,y=200)

#btn3=ttk.Button(root,text="ShowEntry",command=lambda:showLogin())
#btn3.place(x=300,y=200)

root.mainloop()