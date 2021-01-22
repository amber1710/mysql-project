import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk

#First window !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Create window
main=tk.Tk()
main.title('Life Choices Online')
main.geometry('600x700')
main.config(background="light blue")


mydb = mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',host='127.0.0.1',database='lifechoicesonline',auth_plugin='mysql_native_password')

mycursor =mydb.cursor()





#Headlabel to welcome users !!
headlabel=Label(main , text="WELCOME !!!")
headlabel.place(x=250,y=10,width=150)


#Label for Username
label4=Label(main, text="Username")
label4.place(x=68,y=190)
username_login_entry = Entry(main, textvariable="username")
username_login_entry.place(x=240,y=190)

#Label and Entry for Password
label5=Label(main, text="Password")
label5.place(x=70,y=250)
password__login_entry4= Entry(main, textvariable="password", show= '*')
password__login_entry4.place(x=240,y=250)

#Label for Date signed in
label6=Label(main,text="",bg="beige")
label6.place(x=10,y=10)


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

	#next window

	def back():
		reg.withdraw()



	label_7=Label(reg,text="ID",width=20,bg="yellow",font=("bold",10))
	label_7.place(x=80,y=120)
	entry_0=Entry(reg)
	entry_0.place(x=240,y=120)


	#label and entry for fullname
	label_1 = Label(reg, text="FullName",width=20,bg="yellow",font=("bold", 10))
	label_1.place(x=80,y=150)
	entry_1 = Entry(reg)
	entry_1.place(x=240,y=150)

	#label and entry for Username
	label_2 = Label(reg, text="Username",width=20,bg="yellow",font=("bold", 10))
	label_2.place(x=68,y=190)
	entry_2 = Entry(reg)
	entry_2.place(x=240,y=190)

	#label and entry for Password
	label_3 = Label(reg , text="Password" ,width=20 ,bg="yellow", font=("bold",10))
	label_3.place(x=70,y=300)
	entry_4=Entry(reg)
	entry_4.place(x=240,y=300)


	#button and label for Gender
	label_4 = Label(reg, text="Gender",width=20,bg="yellow",font=("bold", 10))
	label_4.place(x=70,y=250)
	var = IntVar()
	Radiobutton(reg, text="Male",padx = 20, variable=var, value=1 , bg="blue").place(x=235,y=250)
	Radiobutton(reg, text="Female",padx = 20, variable=var, value=2 , bg="pink").place(x=340,y=250)


	def submit ():
		mysql = 'INSERT INTO users VALUES (%s,%s,%s,%s,%s) '
		val = ('')
		cursor.execute(mysql, val)

		db.commit()

		print(cursor.rowcount, "record inserted.")
		cursor.execute('Select * from Dentists')
		for i in cursor:
		   print(i)


	label_0 = Label(reg, text="Register ",width=20,font=("bold", 20),)
	label_0.place(x=90,y=53)

	#button for submit
	Button(reg, text='Submit',width=20,bg='brown',fg='white',command=submit).place(x=180,y=450)
	Button(reg,text='<< Back',width=20,bg='white',command=back).place(x=40,y=600)
	Button(reg,text='Exit',width=20,bg='grey',command=exit).place(x=220,y=600)

	reg.mainloop()

Button2=Button(main,text="Register New User",bg="purple",fg="white",width=20,height=1,command=register)
Button2.place(x=220,y=500)






main.mainloop()




