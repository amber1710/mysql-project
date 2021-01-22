import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk

stu=tk.Tk()
stu.title('Logins')
stu.geometry('600x400')
stu.config(background="black")

def login():
    stu.withdraw()
    import logged


#label for id
labeluser=tk.Label(stu,text="Student ID")
labeluser.place(x=50,y=20)
username=tk.Entry(stu,width=45)
username.place(x=250,y=20,width=100)

labeluser=tk.Label(stu,text="Full Name ")
labeluser.place(x=50,y=50)
username=tk.Entry(stu,width=45)
username.place(x=250,y=50,width=100)

labeluser=tk.Label(stu,text="Username")
labeluser.place(x=50,y=80)
username=tk.Entry(stu,width=45)
username.place(x=250,y=80,width=100)

lbl_pword=tk.Label(stu,text="Password")
lbl_pword.place(x=50,y=120)

password=tk.Entry(stu,width=35 )
password.config(width=20,show="*")
password.place(x=250 , y=120 , width=100)

loginbtn=tk.Button(stu,text="Login" , command="login")
loginbtn.place(x=150,y=170,width=55)

stu.mainloop()
