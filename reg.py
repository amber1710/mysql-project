from tkinter import messagebox
from datetime import datetime
import mysql.connector
from tkinter import *
import tkinter as tk

reg=tk.Tk()
reg.title('Life Choices Online')
reg.geometry('600x700')
reg.config(background="light blue")


db = mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',host='127.0.0.1',database='lifechoicesonline',auth_plugin='mysql_native_password')

cursor = db.cursor()

def submit():
    reg_info=(entry_2.get(),entry_6.get(),entry_5.get(),entry_4.get() )
    wap="INSERT INTO register(username , full_name , mobile number , password) VALUES(%s , %s ,%s ,%s)"
    cursor.execute(wap,reg_info)
    db.commit()
    result = cursor

    if result:
        messagebox.showinfo("info","You registered successfully!")

    else:
        failed()


def failed():
    messagebox.showinfo("Error","PLease try again")



def logged():

    d=datetime.now()
    t=d.strftime("%H:%M")
    dt=d.strftime("%d/%m/%y")
    messagebox.showinfo("info","Login Successfully")

    logout = Tk()
    def out():
        d2=datetime.now()
        t2=d2.strftime("%H:%M")
        u=entry_2.get()
        f=entry_6.get()
        p=entry_5.get()

        inU = u,f,t,t2,p,dt

        uCon2="INSERT INTO register(username,full_name,mobile number,time,timeout,date) VALUES (%s , %s , %s , %s , %s , %s)"

        cursor.execute(uCon2,inU)
        db.commit()
        messagebox.showinfo()

    butOut=Button(logout,text="LogOut",command=out)
    butOut.pack()





label_6=Label(reg,text="Fullname",width=20,bg="yellow",font=("bold",10))
label_6.place(x=70,y=220)
entry_6=Entry(reg)
entry_6.place(x=240,y=220)


#label  and entry for Mobile number
label_6=Label(reg,text="Mobile Number:",width=20,bg="yellow",font=("bold",10))
label_6.place(x=70,y=280)
entry_5=Entry(reg)
entry_5.place(x=240,y=280)

#label and entry for Username
label_2 = Label(reg, text="Username",width=20,bg="yellow",font=("bold", 10))
label_2.place(x=68,y=190)
entry_2 = Entry(reg)
entry_2.place(x=240,y=190)

#label and entry for Password
label_3 = Label(reg , text="Password" ,width=20 ,bg="yellow", font=("bold",10))
label_3.place(x=70,y=330)
entry_4=Entry(reg)
entry_4.place(x=240,y=330)





label_0 = Label(reg, text="Register ",width=20,font=("bold", 20),)
label_0.place(x=90,y=53)

#button for submit
Button(reg, text='Submit',width=20,bg='brown',fg='white',command=submit).place(x=180,y=450)

Button(reg,text='<< Back',width=20,bg='white').place(x=40,y=600)

Button(reg,text='Exit',width=20,bg='grey',command=exit).place(x=220,y=600)

reg.mainloop()
