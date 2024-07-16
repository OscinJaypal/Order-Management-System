from cProfile import label
from distutils.cmd import Command
from pydoc import text
from re import X
from textwrap import fill
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
import random
import datetime
import time
from tkinter import *
from turtle import bgcolor
import tkinter
import mysql.connector


class User:

    def __init__(self,root):
        self.root= root
        self.root.title("Order Management System")
        self.root.geometry ("1540x800+0+0")

        self.UserID_var = StringVar()
        self.FN_var = StringVar()
        self.LN_var = StringVar()
        self.UN_var = StringVar()
        self.PSD_var = StringVar()

        lbltitle =Label(self.root,bd=20, relief= RIDGE, text="ORDER MANAGEMENT SYSTEM", fg="red", bg="white", font=("Times new roman", 50, "bold"))
        lbltitle.pack(side=TOP)

        Dataframe = Frame(self.root, bd=15, relief= RIDGE)
        Dataframe.place(x=0,y=130,width=1330, height=300)
        DataframeCenter = LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,
                                        font=("times new roman", 12, "bold"), text="User Information")
        DataframeCenter.place(x=0,y=5, width=1280, height=250)

        lblid1 = Label(DataframeCenter, bg = "powder blue",text= "User ID", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblid1.grid(row=0, column=0, sticky= W)
        textid1 = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable=self.UserID_var, width= 27)
        textid1.grid(row=0, column=1)

        lblfn = Label(DataframeCenter, bg = "powder blue", text= "First Name", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblfn.grid(row=1, column=0, sticky= W)
        textfn = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.FN_var, width= 27)
        textfn.grid(row=1, column=1)

        lblln = Label(DataframeCenter, bg = "powder blue", text= "Last Name", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblln.grid(row=2, column=0, sticky= W)
        textln = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.LN_var, width= 27)
        textln.grid(row=2, column=1)

        lblun = Label(DataframeCenter, bg = "powder blue", text= "Username", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblun.grid(row=3, column=0, sticky= W)
        textun = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.UN_var, width= 27)
        textun.grid(row=3, column=1)

        lblpsd = Label(DataframeCenter, bg = "powder blue", text= "Password", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblpsd.grid(row=4, column=0, sticky= W)
        textpsd = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.PSD_var, width= 27)
        textpsd.grid(row=4, column=1)


        Buttonframe = Frame(self.root, bd=10, relief= RIDGE)
        Buttonframe.place(x=20, y=440, width=1350, height=50)

        btnadddata = Button(Buttonframe,command=self.adddata, text="Add", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=0)

        btnadddata = Button(Buttonframe,command= self.delete, text="Delete", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=1)

        btnadddata = Button(Buttonframe,command= self.update, text="Update", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=2)

        btnadddata = Button(Buttonframe,command= self.iexit, text="Exit", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=3)

        Detailsframe = Frame(self.root, bd=10, relief= RIDGE)
        Detailsframe.place(x=0, y=500, width=1330, height=180)

        self.user_table = ttk.Treeview(Detailsframe, column=("User ID", "First Name", "Last Name", "Username", "Password"))

        self.user_table.heading("User ID", text= "User ID")
        self.user_table.heading("First Name", text= "First Name")
        self.user_table.heading("Last Name", text= "Last Name")
        self.user_table.heading("Username", text= "Username")
        self.user_table.heading("Password", text= "Password")
        self.user_table["show"] = "headings"
        self.user_table.pack(fill = BOTH, expand = 1)

        self.fetchdata()
        self.user_table.bind("<ButtonRelease-1>",self.get_cursor)

    def adddata(self):
            conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
            my_cursor= conn.cursor()
            my_cursor.execute("INSERT INTO db1.user VALUES (%s,%s,%s,%s,%s)",(self.UserID_var.get(),self.FN_var.get(),self.LN_var.get(),self.UN_var.get(),self.PSD_var.get()))
            conn.commit()
            self.fetchdata()
            conn.close()
            messagebox.showinfo("Success","Member has been inserted successfully")

    def fetchdata(self):
        conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
        my_cursor= conn.cursor()
        my_cursor.execute("select * from db1.user")
        rows = my_cursor.fetchall()
        if len(rows) !=0:
            self.user_table.delete(*self.user_table.get_children())
            for i in rows:
                self.user_table.insert("", END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self, event= ""):
        cursor_row = self.user_table.focus()
        content = self.user_table.item(cursor_row)
        row = content['values']

        self.UserID_var.set(row[0]),
        self.FN_var.set(row[1]),
        self.LN_var.set(row[2]),
        self.UN_var.set(row[3]),
        self.PSD_var.set(row[4])

    def update(self):
        conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
        my_cursor= conn.cursor()
        my_cursor.execute("update db1.user set `First Name`= %s, `Last Name`= %s, `Username`= %s, `Password`= %s where `User ID`= %s",(self.FN_var.get(),self.LN_var.get(),self.UN_var.get(),self.PSD_var.get(),self.UserID_var.get(), ))
        conn.commit()
        self.fetchdata()
        conn.close()
        messagebox.showinfo("Success","Changes have been made successfully")

    
    def delete(self):
        val = (self.UserID_var.get(),)
        if self.UserID_var.get()== "" or self.FN_var== "":
            messagebox.showerror("Error","Select any Member to delete")
        else:
            conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
            my_cursor= conn.cursor()
            query = "DELETE from db1.user WHERE `User ID`= %s; "
            val = (self.UserID_var.get(), )
            my_cursor.execute(query,val)
            conn.commit()
            self.fetchdata()
            conn.close()
            messagebox.showinfo("Success", "Member has been deleted")    

    def iexit(self):
        iexit=tkinter.messagebox.askyesno("Order Manangement System", "Do yoy want to exit?")
        if iexit>0:
            self.root.destroy()
            return

if __name__ == "__main__":
    root = Tk()
    ob= User(root)
    root.mainloop()