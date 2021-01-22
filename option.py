from tkinter import *
import tkinter.messagebox
import mysql.connector
import tkinter as tk

option=tk.Tk()
option.geometry("500x400")
option.config(background="yellow")
option.title("Select Login")


def opt():
	option.withdraw()
	import staff

def admin():
	option.withdraw()
	import admin

def students():
	option.withdraw()
	import students

def register():
	option.withdraw()
	import reg



button1 = Button(option, text="REGISTER",command=register).grid(row=3,column=1,sticky=W,ipadx=20,ipady=20)
button2 = Button(option, text="STUDENTS",command=students).grid(row=4,column=6,sticky=E,ipadx=20,ipady=20)
button3 = Button(option, text="ADMIN",command=admin).grid(row=5,column=4,sticky=W,ipadx=20,ipady=20)
button4 = Button(option, text="STAFF",command=opt).grid(row=6,column=7,sticky=E,ipadx=20,ipady=20)

option.mainloop()
