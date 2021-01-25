import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk

#First window !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Create window
from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime






mydb= mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", database="lifechoicesonline", host="127.0.0.1", auth_plugin="mysql_native_password")
#connect database

mycursor=mydb.cursor()

#create function thats pulls all data from Login table in the hospital database
def verify():
    user_verification= username.get()
    pass_verification = password.get()
    sql = "select * from users where user_name = %s and password = %s"
    mycursor.execute(sql,[(user_verification), (pass_verification)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
            failed()

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
x = datetime.now()

def logged():
    x = datetime.now()
    y = x.strftime("%H:%M")
    myuser=simpledialog.askstring("Input", "Please re-enter username ", parent=root)
    exe = "INSERT INTO login VALUES (%s, curtime(), NULL)"
    mycursor.execute(exe, [myuser])
    mydb.commit()
    messagebox.showinfo("Successful", "You have successfully logged in")

    root.withdraw()



    window = tk.Tk()

    window.title('Login Page')

    window.geometry("450x450")
    window.configure(background="black")

    lbluser=tk.Label(window, text="Life Choices Online: Logged in", bg="cadet blue")
    lbluser.pack(pady=10)

    lbluser=tk.Label(window, text="You are currently LOGGED IN as:\n\n"+ username.get(), bg="grey")
    lbluser.pack(pady=10)

    regbuttn=tk.Button(window,text="Sign Out", command=sign_out)
    regbuttn.pack(pady=60)




def failed():
    messagebox.showerror("Login failed", "Please check your username and password.")

def register():
    root.withdraw()
    import reg

def sign_out():
    x = datetime.now()
    y = x.strftime("%H:%M")
    MsgBox = tk.messagebox.askquestion ('Sign Out','Are you sure you want to sign out?',icon = 'warning')
    if MsgBox == 'yes':

       x = datetime.now()
       y = x.strftime("%H:%M")
       myuser=simpledialog.askstring("Input", "Please re-enter username ", parent=root)
       exe = "UPDATE logged SET time_out = curtime()where user_name=%s"
       mycursor.execute(exe, [myuser])
       mydb.commit()

       root.destroy()
       import logged

    else:
        tk.messagebox.showinfo('Return','You will now return to the application screen')



root = tk.Tk()

root.title('Lifechoices Online')

root.geometry("700x680")
root.configure(background="pink")

lbluser=tk.Label(root, text="Sign in", bg="beige")
lbluser.pack(pady=10)


lbluser=tk.Label(root, text="Enter Username",bg='white')
lbluser.pack(pady=20)

username= tk.Entry(root, width=30)
username.pack(pady=20)

lblpasswd=tk.Label(root,text="Enter Password",bg='white')
lblpasswd.pack(pady=20)

password = tk.Entry(root,width=30)
password.pack(pady=20)

logbuttn=tk.Button(root,text="Sign In", command=verify,bg='light blue')
logbuttn.pack(pady=20)

regbuttn=tk.Button(root,text="Register", command=register,bg='red')
regbuttn.pack(pady=20)


import time

time1 = ''
clock = Label(root, font=('times', 18, 'bold'), bg='light blue')
clock.pack(pady=100)

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
    clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()

keyspressed=""
def key():
    global keyspressed
    root.destroy()
    import admin

root.bind("<Control-a>",lambda x: key())





root.mainloop()


