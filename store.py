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


class Store:

    def __init__(self,root):
        self.root= root
        self.root.title("Order Management System")
        self.root.geometry ("1540x800+0+0")

        self.StoreID_var = StringVar()
        self.Address_var = StringVar()
        
        lbltitle =Label(self.root,bd=20, relief= RIDGE, text="ORDER MANAGEMENT SYSTEM", fg="red", bg="white", font=("Times new roman", 50, "bold"))
        lbltitle.pack(side=TOP)

        Dataframe = Frame(self.root, bd=15, relief= RIDGE)
        Dataframe.place(x=0,y=130,width=1330, height=300)
        DataframeCenter = LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,
                                        font=("times new roman", 12, "bold"), text="Store Information")
        DataframeCenter.place(x=0,y=5, width=1280, height=250)

        lblid1 = Label(DataframeCenter, bg = "powder blue",text= "Store ID", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblid1.grid(row=0, column=0, sticky= W)
        textid1 = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable=self.StoreID_var, width= 27)
        textid1.grid(row=0, column=1)

        lblid = Label(DataframeCenter, bg = "powder blue", text= "Address", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblid.grid(row=1, column=0, sticky= W)
        textid = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.Address_var, width= 27)
        textid.grid(row=1, column=1)


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

        yscroll = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.store_table = ttk.Treeview(Detailsframe, column=("Store ID", "Address"))

        self.store_table.heading("Store ID", text= "Store ID")
        self.store_table.heading("Address", text= "Address")
        self.store_table["show"] = "headings"
        self.store_table.pack(fill = BOTH, expand = 1)

        self.fetchdata()
        self.store_table.bind("<ButtonRelease-1>",self.get_cursor)

    def adddata(self):
        conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
        my_cursor= conn.cursor()
        my_cursor.execute("INSERT INTO db1.store VALUES (%s,%s)",(self.StoreID_var.get(),self.Address_var.get()))        
        conn.commit()
        self.fetchdata()
        conn.close()
        messagebox.showinfo("Success","Member has been inserted successfully")

    def fetchdata(self):
        conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
        my_cursor= conn.cursor()
        my_cursor.execute("select * from db1.store")
        rows = my_cursor.fetchall()
        if len(rows) !=0:
            self.store_table.delete(*self.store_table.get_children())
            for i in rows:
                self.store_table.insert("", END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self, event= ""):
        cursor_row = self.store_table.focus()
        content = self.store_table.item(cursor_row)
        row = content['values']

        self.StoreID_var.set(row[0]),
        self.Address_var.set(row[1]),
        
    def update(self):
        conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
        my_cursor= conn.cursor()
        my_cursor.execute("update db1.store set `Address`= %s where `Store ID`= %s",(self.Address_var.get(),self.StoreID_var.get(), ))
        conn.commit()
        self.fetchdata()
        conn.close()
        messagebox.showinfo("Success","Changes have been made successfully")

    
    def delete(self):
        val = (self.StoreID_var.get(),)
        if self.StoreID_var.get()== "" or self.Address_var== "":
            messagebox.showerror("Error","Select any Member to delete")
        else:
            conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
            my_cursor= conn.cursor()
            query = "DELETE from db1.store WHERE `Store ID`= %s; "
            val = (self.StoreID_var.get(),)
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
    ob= Store(root)
    root.mainloop()