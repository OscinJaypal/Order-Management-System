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


class Order:

    def __init__(self,root):
        self.root= root
        self.root.title("Order Management System")
        self.root.geometry ("1540x800+0+0")

        self.OrderID_var = StringVar()
        self.ProductID_var = StringVar()
        self.Date_var = StringVar()
        self.Amount_var = StringVar()
        self.Quantity_var = StringVar()


        lbltitle =Label(self.root,bd=20, relief= RIDGE, text="ORDER MANAGEMENT SYSTEM", fg="red", bg="white", font=("Times new roman", 50, "bold"))
        lbltitle.pack(side=TOP)

        Dataframe = Frame(self.root, bd=15, relief= RIDGE)
        Dataframe.place(x=0,y=130,width=1330, height=300)
        DataframeCenter = LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,
                                        font=("times new roman", 12, "bold"), text="Order Information")
        DataframeCenter.place(x=0,y=5, width=1280, height=250)

        lblid1 = Label(DataframeCenter, bg = "powder blue",text= "Order ID", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblid1.grid(row=0, column=0, sticky= W)
        textid1 = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable=self.OrderID_var, width= 27)
        textid1.grid(row=0, column=1)

        lblid = Label(DataframeCenter, bg = "powder blue", text= "Product ID", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblid.grid(row=1, column=0, sticky= W)
        textid = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.ProductID_var, width= 27)
        textid.grid(row=1, column=1)

        lbldate = Label(DataframeCenter, bg = "powder blue", text= "Date", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lbldate.grid(row=2, column=0, sticky= W)
        textdate = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.Date_var, width= 27)
        textdate.grid(row=2, column=1)

        lblamount = Label(DataframeCenter, bg = "powder blue", text= "Address", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblamount.grid(row=3, column=0, sticky= W)
        textamount = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.Amount_var, width= 27)
        textamount.grid(row=3, column=1)

        lblqua = Label(DataframeCenter, bg = "powder blue", text= "Quantity", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblqua.grid(row=4, column=0, sticky= W)
        textqua = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.Quantity_var, width= 27)
        textqua.grid(row=4, column=1)


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

        self.order_table = ttk.Treeview(Detailsframe, column=("Order ID", "Product ID", "Date", "Amount", "Quantity"))

        self.order_table.heading("Order ID", text= "Order ID")
        self.order_table.heading("Product ID", text= "Product ID")
        self.order_table.heading("Date", text= "Date")
        self.order_table.heading("Amount", text= "Amount")
        self.order_table.heading("Quantity", text= "Quantity")
        self.order_table["show"] = "headings"
        self.order_table.pack(fill = BOTH, expand = 1)

        self.fetchdata()
        self.order_table.bind("<ButtonRelease-1>",self.get_cursor)

    def adddata(self):
        conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
        my_cursor= conn.cursor()
        my_cursor.execute("INSERT INTO db1.order VALUES (%s,%s,%s,%s,%s)",(self.OrderID_var.get(),self.ProductID_var.get(),self.Date_var.get(),self.Amount_var.get(),self.Quantity_var.get()))
        conn.commit()
        self.fetchdata()
        conn.close()
        messagebox.showinfo("Success","Member has been inserted successfully")

    def fetchdata(self):
        conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
        my_cursor= conn.cursor()
        my_cursor.execute("select * from db1.order")
        rows = my_cursor.fetchall()
        if len(rows) !=0:
            self.order_table.delete(*self.order_table.get_children())
            for i in rows:
                self.order_table.insert("", END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self, event= ""):
        cursor_row = self.order_table.focus()
        content = self.order_table.item(cursor_row)
        row = content['values']

        self.OrderID_var.set(row[0]),
        self.ProductID_var.set(row[1]),
        self.Date_var.set(row[2]),
        self.Amount_var.set(row[3]),
        self.Quantity_var.set(row[4])

    def update(self):
        conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
        my_cursor= conn.cursor()
        my_cursor.execute("update db1.order set `Product ID`= %s, `Date`= %s, `Amount`= %s, `Quantity`= %s where `Order ID`= %s",(self.ProductID_var.get(),self.Date_var.get(),self.Amount_var.get(),self.Quantity_var.get(),self.OrderID_var.get(), ))
        conn.commit()
        self.fetchdata()
        conn.close()
        messagebox.showinfo("Success","Changes have been made successfully")

    
    def delete(self):
        val = (self.OrderID_var.get(),)
        if self.OrderID_var.get()== "" or self.ProductID_var== "":
            messagebox.showerror("Error","Select any Member to delete")
        else:
            conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
            my_cursor= conn.cursor()
            query = "DELETE from db1.order WHERE `Order ID`= %s; "
            val = (self.OrderID_var.get(),)
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
    ob= Order(root)
    root.mainloop()