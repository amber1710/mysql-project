from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime


mydb= mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", database="lifechoicesonline", host="127.0.0.1", auth_plugin="mysql_native_password")
#connect database

cursor=mydb.cursor()

x = datetime.datetime.now()
#function to display the data
def display():
        cursor.execute("SELECT ID FROM users")

        id = cursor.fetchall()

        for x in id:
            listbox_id.insert(END, x)

        listbox_id.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT full_name FROM users")

        name = cursor.fetchall()

        for x in name:
            listbox_fullname.insert(END, x)

        listbox_fullname.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT user_name FROM users")

        uName = cursor.fetchall()
        for x in uName:
            listbox_uname.insert(END, x)
        listbox_uname.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT password FROM users")

        pas = cursor.fetchall()
        for x in pas:
            listbox_pass.insert(END, x)
        listbox_pass.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT mobile_number FROM users")

        mobileno = cursor.fetchall()
        for x in mobileno:
            listbox_mobile.insert(END, x)
        listbox_mobile.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT status FROM users")

        cat = cursor.fetchall()
        for x in cat:
            listbox_status.insert(END, x)
        listbox_status.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT date_joined FROM users")

        date = cursor.fetchall()
        for x in date:
            listbox_date.insert(END, x)
        listbox_date.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT user_name FROM logged")

        Unamelogged = cursor.fetchall()
        for x in Unamelogged:
            listbox_user.insert(END, x)
        listbox_user.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT time_in FROM logged")

        timeIn = cursor.fetchall()
        for x in timeIn:
            listbox_timein.insert(END, x)
        listbox_timein.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT time_out FROM logged")

        timeOut = cursor.fetchall()
        for x in timeOut:
            listbox_timeout.insert(END, x)
        listbox_timeout.insert(END, str(cursor.rowcount) + " rows")




def add():
        comm3 = "INSERT INTO users (full_name, user_name, password, mobile_number, status, date_joined) VALUES (%s, %s, %s,%s, %s, %s)"
        user_info1 = str(full_name.get()), str(user_name.get()), password.get(),mobile.get(),str(tkvar.get()),x
        cursor.execute(comm3, user_info1)
        mydb.commit()
        messagebox.showinfo("Confirmation", "User created successfully")

def clear():
    listbox_timeout.delete(0,END)
    listbox_timein.delete(0,END)
    listbox_uname.delete(0,END)
    listbox_date.delete(0,END)
    listbox_status.delete(0, END)
    listbox_mobile.delete(0,END)
    listbox_pass.delete(0, END)
    listbox_fullname.delete(0,END)
    listbox_id.delete(0,END)
    listbox_user.delete(0,END)

#to delete data from database
def delete():

        fullname=full_name.get()

        Delete="delete from users where full_name='%s'" %(fullname)
        cursor.execute(Delete)
        mydb.commit()
        messagebox.showinfo("Information","Record Deleted")

#create admin user
def makeAdmin():
    def make_admin_action():
        mydb= mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", database="lifechoicesonline", host="127.0.0.1", auth_plugin="mysql_native_password")

        mycursor = mydb.cursor()
        try:
            user_id=int(admin_id.get())

        except:
            messagebox.showerror("Error","Only enter a number for the ID")

        sql= "INSERT INTO admin (username, password) select user_name, password from users where id=%s"
        try:
            mycursor.execute(sql,[(id)])
            mydb.commit()
            messagebox.showinfo("Success", "Successfully made  user id="+str(id)+"an admin")
        except:
            messagebox.showerror("Error", "Error in my sql connection")

    newWindow = Tk()
    newWindow.title("Make user admin")
    newWindow.geometry("650x450")


    lbl_id=Label(newWindow,text="Enter ID of user to add as Admin")
    lbl_id.place(x=5,y=5)

    admin_id=Entry(newWindow,width=10)
    admin_id.place(x=230,y=5)

    adminBtn=Button(newWindow, text="Make Admin",command=make_admin_action)
    adminBtn.place(x=220,y=30)

    newWindow.mainloop()

def  back():
    master.destroy()
    import main

def sign_out():
    x = datetime.datetime.now()
    y = x.strftime("%H:%M")
    MsgBox = tk.messagebox.askquestion ('Sign Out','Are you sure you want to sign out?',icon = 'warning')
    if MsgBox == 'yes':

       x = datetime.datetime.now()
       y = x.strftime("%H:%M")
       myuser=simpledialog.askstring("Input", "Please re-enter username ", parent=master)
       exe = "UPDATE login SET time_out = curtime()where user_name=%s"
       cursor.execute(exe, [myuser])
       mydb.commit()

       master.destroy()
       import main


master = tk.Tk()

master.title('Administration')
master.geometry("1000x1000")
master.configure(background="beige")

lbluser=tk.Label(master, text="Administration Portal", bg="white")
lbluser.pack(pady=10)

#labels
lblid=Label(master,text="ID", bg="black",fg="white")
lblid.place(x=50,y=40)

lblful=Label(master,text="Fullname", bg="black",fg="white")
lblful.place(x=120,y=40)

lblid=Label(master,text="Username", bg="black",fg="white")
lblid.place(x=200,y=40)

lblid=Label(master,text="Password", bg="black",fg="white")
lblid.place(x=300,y=40)

lblid=Label(master,text="Mobile no.", bg="black",fg="white")
lblid.place(x=385,y=40)

lblid=Label(master,text="Category", bg="black",fg="white")
lblid.place(x=600,y=40)

lblid=Label(master,text="Date Joined", bg="black",fg="white")
lblid.place(x=800,y=40,)

#####################################################################################################
#LOGINDATALABELS
#####################################################################################################
lblid=Label(master,text="Username", bg="black",fg="white")
lblid.place(x=25,y=260)

lblid=Label(master,text="Time In", bg="black",fg="white")
lblid.place(x=160,y=260)

lblid=Label(master,text="Time Out", bg="black",fg="white")
lblid.place(x=330,y=260)






#users

listbox_id = Listbox(master,bg="light blue",width=10, height=10,selectbackground="grey", selectforeground="black")
listbox_id.place(x=20,y=70)

listbox_fullname = Listbox(master,bg="light blue",width=10,selectbackground="grey", selectforeground="black")
listbox_fullname.place(x=110,y=70)

listbox_uname = Listbox(master,bg="light blue",width=10,selectbackground="grey", selectforeground="black")
listbox_uname.place(x=200,y=70)

listbox_pass = Listbox(master,bg="light blue",width=10,selectbackground="grey", selectforeground="black")
listbox_pass.place(x=290,y=70)

listbox_mobile = Listbox(master,bg="light blue",width=10,selectbackground="grey", selectforeground="black")
listbox_mobile.place(x=380,y=70)

listbox_status = Listbox(master,bg="light blue",width=10,selectbackground="grey", selectforeground="black")
listbox_status.place(x=600,y=70,width=150)

listbox_date = Listbox(master,bg="light blue",width=10,selectbackground="grey", selectforeground="black")
listbox_date.place(x=800,y=70,width=150)

#######################################################################################################################
#logindata

listbox_user = Listbox(master,bg="light blue",width=10, height=10,selectbackground="grey", selectforeground="black")
listbox_user.place(x=20,y=290)

listbox_timein = Listbox(master,bg="light blue",width=20, height=10,selectbackground="grey", selectforeground="black")
listbox_timein.place(x=110,y=290)

listbox_timeout = Listbox(master,bg="light blue",width=20, height=10,selectbackground="grey", selectforeground="black")
listbox_timeout.place(x=280,y=290)

################################################################################################################3######

lbluser=tk.Label(master, text="Enter Fullname",bg="white")
lbluser.place(x=200, y=500)

full_name= tk.Entry(master, width=30)
full_name.place(x=400,y=500)

lblpasswd=tk.Label(master,text="Enter Username",bg="white")
lblpasswd.place(x=200, y=540)

user_name = tk.Entry(master,width=30)
user_name.place(x=400, y=540)

labelpass=tk.Label(master,text="Enter Password",bg="white")
labelpass.place(x=200, y=580)

password = tk.Entry(master,width=30)
password.place(x=400, y=580)

labelmob=tk.Label(master,text="Mobile Number",bg="white")
labelmob.place(x=200, y=620)

mobile = tk.Entry(master,width=30)
mobile.place(x=400, y=620)

labelcat=tk.Label(master,text="Category",bg="white")
labelcat.place(x=200, y=660)

tkvar = StringVar(master)

# Dictionary with options
choices = {'Visitor','Student','Employee'}
tkvar.set('Student') # set the default option

popupMenu = OptionMenu(master, tkvar, *choices)
popupMenu.place(x=400, y=660)



logbuttn=tk.Button(master,text="ADD RECORD",command=add,bg="orange")
logbuttn.place(x=40, y=780)

logbuttn=tk.Button(master,text="DELETE RECORD",command=delete,bg="orange")
logbuttn.place(x=40, y=820)




logbuttn=tk.Button(master,text="DISPLAY DATA", command=display,bg="orange")
logbuttn.place(x=500, y=780)

logbuttn=tk.Button(master,text="CLEAR", command=clear,bg="orange")
logbuttn.place(x=570,y=820)


logbuttn=tk.Button(master,text="MAKE ADMIN",command=makeAdmin,bg="orange")
logbuttn.place(x=290, y=780)

logbuttn=tk.Button(master,text="SIGN OUT", command=sign_out,bg="black",fg="white")
logbuttn.place(x=260,y=900,width=200)












master.mainloop()


