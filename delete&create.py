import mysql.connector
import admin
import datetime
import admin as ad
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.config(background="light blue")
root.title("Data Control")

mydb= mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", database="lifechoicesonline", host="127.0.0.1", auth_plugin="mysql_native_password")

mycursor=mydb.cursor()

current_date = datetime.datetime.now()

def studentData():
   mydb= mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", database="lifechoicesonline", host="127.0.0.1", auth_plugin="mysql_native_password")

   mycursor=mydb.cursor()

   exe = "CREATE TABLE IF NOT EXISTS  users VALUES(ID int(35) NOT NULL AUTO_INCREMENT, full_name varchar(60) default null, user_name varchar(50) default null, password varchar(20) default null, mobile_number int(10) default null, status varchar(30) default not null, date_joined date, PRIMARY KEY(ID))"
   mycursor.execute(exe)
   mydb.commit()


fullname= ad.full_name.get()
username1= ad.username.get()
password1= ad.password.get()
status1= ad.tkvar.get()
mobile1 =ad.mobile.get()

def addRec(full_name, user_name, password, mobile_number, status):
    mydb= mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", database="lifechoicesonline", host="127.0.0.1", auth_plugin="mysql_native_password")

    mycursor=mydb.cursor()

    sql = "INSERT INTO users (full_name, user_name, password, mobile_number, status, date_joined) VALUES (%s, %s, %s, %s,%s,%s)"
    val = (fullname, username1,password1,mobile1,str(status1),current_date)

    mycursor.execute(sql, val)

    mydb.commit()


def viewData():
    con = con = mysql.connector.connect(host="127.0.0.1", user="lifechoices", passwd="@Lifechoices1234")
    cur = con.cursor()
    cur.execute("use lifechoicesonline")
    cur.execute("select * from users")
    row = cur.fetchall()
    con.close()
    return row

def deleteRec(id):
    con = con = mysql.connector.connect(host="127.0.0.1", user="lifechoices", passwd="@Lifechoices1234")
    cur = con.cursor()
    cur.execute("use lifechoicesonline")
    cur.execute("DELETE FROM users WHERE ID=%s", (id,))
    con.commit()
    con.close()


root.mainloop()
