import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk

my_connect = mysql.connector.connect(
    host="localhost",
    user="lifechoices",
    passwd="@Lifechoices1234",
    database="lifechoicesonline"
)
my_cursor = my_connect.cursor()
####### end of connection ####

recep = tk.Tk()
recep.geometry("400x200")

# add one Label
l1 = tk.Label(recep,  text='Enter Student ID: ', width=25 )
l1.grid(row=1,column=1)

# add one text box
t1 = tk.Text(recep,  height=1, width=4,bg='yellow')
t1.grid(row=1,column=2)

b1 = tk.Button(recep, text='Show Details', width=15,bg='red',
    command=lambda: my_details(t1.get('1.0',END)))
b1.grid(row=1,column=4)

my_str = tk.StringVar()
# add one Label
l2 = tk.Label(recep,  textvariable=my_str, width=30,fg='red' )
l2.grid(row=3,column=1,columnspan=2)

my_str.set("Output")

def my_details(id):
    try:
        val = int(id) # check input is integer or not
        try:
            my_cursor.execute("SELECT * FROM users WHERE id, ="+id)
            student = my_cursor.fetchall()
            #print(student)
            my_str.set(student)

        except :
             my_str.set("Database error")
    except:
        my_str.set("Check input")

recep.mainloop()
