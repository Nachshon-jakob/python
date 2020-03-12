
import tkinter as tk
from tkinter import *
import os
import webbrowser
import pyodbc
import pymysql
import sqlite3


def onClick(event):
    return lambda *args, **kwargs: webbrowser.open(url="youtube.com")

def submit():

    conn = pymysql.connect(host="db4free.net",
                                port=3306,
                                user="nachshonyj",
                                password="Nachshony1",
                                charset="utf8mb4",
                                db="formdata12",
                                cursorclass=pymysql.cursors.DictCursor
                                )
    cursor = conn.cursor()


    print("oooo")
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_31.delete(0, END)

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="FullName:",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root, text="username")
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email: ",width=20,font=("bold", 10))
label_2.place(x=58,y=240)

entry_2 = Entry(root, text="email")
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Phone number:",width=20,font=("bold", 10))
label_3.place(x=69,y=180)

entry_31 = Entry(root, text="phone")
entry_31.place(x=200,y=240)

label_3 = Label(root, text="Gender:",width=20,font=("bold", 10))
label_3.place(x=70,y=280)
var = IntVar()
entry_3 = Radiobutton(root, text="Male",padx = 5, variable=var, value=1)
entry_3.place(x=205,y=280)
entry_3 = Radiobutton(root, text="Female",padx = 20, variable=var, value=2)
entry_3.place(x=280,y=280)



label_4 = Label(root, text="Programming:",width=20,font=("bold", 10))
label_4.place(x=85,y=330)
var1 = IntVar()
entry_4 = tk.Checkbutton(root, text="java", variable=var1)
entry_4.place(x=235,y=330)
var2 = IntVar()
entry_4 = tk.Checkbutton(root, text="python", variable=var2)
entry_4.place(x=290,y=330)

butt1 = Button(root, text='Submit', width=20,bg='brown',fg='white', command=submit)
butt1.place(x=180, y=380)



openfile = tk.Button(root, text="Youtube.com", padx=90, pady=5, bg="#263D42", fg="red")
openfile.bind("<Button-1>", onClick(event=""))
openfile.pack()
root.mainloop()

conn = pymysql.connect(host="db4free.net",
                            port=3306,
                            user="nachshonyj",
                            password="Nachshony1",
                            db="formdata12",
                            charset="utf8mb4",
                            cursorclass=pymysql.cursors.DictCursor
                            )

cursor = conn.cursor()

cursor.execute("INSERT INTO Formdata (`username`, `phone`, `email`) VALUES ('kiuygthrs', 'houseersi_900knvmk', 9008907896)")
