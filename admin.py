import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk

mydb = mysql.connector.connect(user='lifechoices',password='@Lifechoices1234', database='lifechoicesonline',
                             host='127.0.0.1',auth_plugin='mysql_native_password')

mycursor=mydb.cursor()

def logs():


admin=tk.Tk()
admin.title('Logins')
admin.geometry('600x400')
admin.config(background="light blue")


labeluser=tk.Label(admin,text="Username")
labeluser.place(x=50,y=20)


def logs():
	admin.withdraw()
	import recep


username=tk.Entry(admin,width=45)
username.place(x=250,y=20,width=100)

lbl_pword=tk.Label(admin,text="Password")
lbl_pword.place(x=50,y=50)

password=tk.Entry(admin,width=35 )
password.config(width=20,show="*")
password.place(x=250 , y=50 , width=100)

loginbtn=tk.Button(admin,text="Login" , command="logs")
loginbtn.place(x=150,y=135,width=55)



admin.mainloop()





