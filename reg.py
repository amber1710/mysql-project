
from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox
import datetime

root = tk.Tk()

root.title("REGISTRATION")
root.geometry("700x780")
root.configure(background="light green")



mydb= mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", database="lifechoicesonline", host="127.0.0.1", auth_plugin="mysql_native_password")
#connect database
mycursor=mydb.cursor()

x = datetime.datetime.now()


def insert():

    fullname= fullname1.get()
    username1= username.get()
    password1= password.get()
    status1= tkvar.get()
    mobile1 =mobile.get()

    sql = "INSERT INTO users (full_name, user_name, password, mobile_number, status, date_joined) VALUES (%s, %s, %s, %s,%s,%s)"
    val = (fullname, username1,password1,mobile1,str(status1),x)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    messagebox.showinfo("Registration Complete","Please log in.")
    root.withdraw()
    import main



lbluser=tk.Label(root, text="Welcome to LIfe Choices Online", bg="beige", font="22")
lbluser.pack(pady=20)

lbluser=tk.Label(root, text="Please complete the form below.", bg="white", font="20")
lbluser.pack()

lbluser=tk.Label(root, text="Enter Fullname",bg='white')
lbluser.pack(pady=20)

fullname1= tk.Entry(root, width=30)
fullname1.pack(pady=20)

lblpasswd=tk.Label(root,text="Enter Username",bg='white')
lblpasswd.pack(pady=20)

username = tk.Entry(root,width=30)
username.pack(pady=20)

lblpasswd=tk.Label(root,text="Enter Password",bg='white')
lblpasswd.pack(pady=20)

password = tk.Entry(root,width=30)
password.pack(pady=20)

lblmobile=tk.Label(root,text="Mobile Number",bg='white')
lblmobile.pack(pady=20)

mobile = tk.Entry(root,width=30)
mobile.pack(pady=20)

lblstatus =Label(root, text="Registering as a:",bg='white')
lblstatus.pack(pady=20)

#Dropdown
# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
choices = {'Visitor','Student','Employee'}
tkvar.set('Student') # set the default option

popupMenu = OptionMenu(root, tkvar, *choices)
popupMenu.place(x=240, y=640,width=200)

logbuttn=tk.Button(root,text="Submit", command=insert,bg='blue',fg='white')
logbuttn.place(x=230, y=700)

root.mainloop()
