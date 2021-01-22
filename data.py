import mysql.connector
mydb=mysql.connector.connect(user='lifechoices',password='@Lifechoices1234'
                             ,host='127.0.0.1',database='Hospitals'
                             ,auth_plugin='mysql_native_password')

mycursor=mydb.cursor()

sql="UPDATE Dentists SET Dentists_surname='Benjamin' WHERE Dentists_names='Amber'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount,"record updated.")
mycursor.execute("Select * from Dentists")

for i in mycursor:
    print(i)
