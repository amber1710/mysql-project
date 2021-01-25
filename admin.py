from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

mydb= mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", database="lifechoicesonline", host="127.0.0.1", auth_plugin="mysql_native_password")
#connect database

cursor = mydb.cursor()

# to login into admin with data from mysql
def verify():
    user_verification= username.get()
    pass_verification = password.get()
    sql = "select * from admin where username = %s and password = %s"
    cursor.execute(sql,[(user_verification), (pass_verification)])
    results = cursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
            failed()

#to display a messagebox
def failed():
    messagebox.showerror("Login failed", "Please check your username and password.")

def logged():
    x = datetime.now()
    y = x.strftime("%H:%M")
    user=simpledialog.askstring("Input", "Please re-enter username ", parent=root)
    wap = "INSERT INTO login VALUES (%s, curtime(), NULL)"
    cursor.execute(wap, [user])
    mydb.commit()
    messagebox.showinfo("Successful", "You have successfully logged in")

    root.withdraw()
    import adlog

def back():
    root.destroy()
    import main

root = tk.Tk()

root.title('Login: Admin')

root.geometry("650x650")
root.configure(background="light blue")

lbluser=tk.Label(root, text="Life Choices Online: Admin Log in", bg="pink")
lbluser.pack(pady=10)

lbluser=tk.Label(root, text="Enter Username",bg="orange")
lbluser.pack(pady=20)

username= tk.Entry(root, width=30)
username.pack(pady=20)

lblpasswd=tk.Label(root,text="Enter Password",bg="orange")
lblpasswd.pack(pady=20)

password = tk.Entry(root,width=30)
password.pack(pady=20)

logbuttn=tk.Button(root,text="Sign In", command=verify)
logbuttn.pack(pady=20)

logbuttn=tk.Button(root,text="Back", command=back)
logbuttn.pack(pady=20)

lbluser=tk.Label(root, text="Admin login details:\n\nusername: admin\n\npassword: 1234")
lbluser.pack(pady=20)

root.mainloop()
