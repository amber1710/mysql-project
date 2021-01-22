#BUTTONS FOR OPTIONS
import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk

root=tk.Tk()
root.title('Life Choices Online')
root.geometry('600x400')
root.config(background="light blue")




button1 = Button(root, text="REGISTER").grid(row=1,column=1,sticky=W)
button2 = Button(root, text="STUDENTS").grid(row=1,column=6,sticky=E)
button3 = Button(root, text="ADMIN").grid(row=3,column=4,sticky=W)
button4 = Button(root, text="STAFF").grid(row=6,column=6,sticky=E)

root.mainloop()
