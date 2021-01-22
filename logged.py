import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk

logged=tk.Tk()
logged.title('Life Choices Online')
logged.geometry('900x700')
logged.config(background="light blue")



label=Label(logged, text="Salesian Life Choices is a small yet powerful NPO based in Cape Town.\n \n "
                      "Since 2005, we have impacted over 200 000 people with choices, not charity.\n "
                      "We invest in youth because they are 37% of the South African population… but 100% of its future.\n "
                      "We work with youth from the Cape Flats communities to make choices that can change the world. \n"
                      "We believe that inequality is a matter of the heart and that it can be eradicated if youth are provided with a solid foundation.\n"
                      "We provide this foundation through our services in five key areas: Family Stability, Health, Education, Leadership and Employment.\n "
                      "Salesian Life Choices interventions are holistic by addressing the social, physical and the mental well-being of our beneficiaries.\n "
                      "This ensures our impact is sustainable and that our beneficiaries go on to have a positive impact in their communities.\n",
                      bg="white")
label.place(x=5,y=70,width=900,height=500)


exit=Button(logged , text="EXIT" , command=exit)
exit.place(x=10,y=10)



logged.mainloop()
