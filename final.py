from msilib.schema import Font
import tkinter as tk
from tkinter import Frame, Label, ttk
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
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
from tkinter.tix import X_REGION
from turtle import bgcolor
import mysql.connector


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# from PIL import Image, ImageTK
class loginpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Label = tk.Label(self, text="Welcome To My OMS", font=(FONT_NAME,30,"bold"))
        # Label.place(x=275, y=50)

        Dataframe = Frame(self, bd=15, relief= RIDGE)
        Dataframe.place(x=380,y=100,width=650, height=600)
        L0 = tk.Label(self, text="Login Page", font=(FONT_NAME, 25 ,"bold"))
        L0.place(x=600, y=200)

        lbltitle = tk.Label(self, bd=20, relief=RIDGE, text="ORDER MANAGEMENT SYSTEM", fg="black", bg="white",
                            font=("Courier", 50, "bold"))
        lbltitle.place(x=227,y=0)
        L1 = tk.Label(self, text="Username", font=(FONT_NAME, 12,"bold"))
        L1.place(x=525, y=300)
        T1 = tk.Entry(self, width=30, bd=5)
        T1.place(x=625, y=300)
        L2 = tk.Label(self, text="Password", font=(FONT_NAME, 12, "bold"))
        L2.place(x=525, y=400)
        T2 =tk.Entry(self, show="*", width=30, bd=5)
        T2.place(x=625, y=400)
        # name_list=["Jahnavi", "Oscin"]
        # pass_list=["123",""]
        def verify():
            if T1.get() == "Jahnavi" and T2.get()=="123":
                controller.show_frame(homepage)
                messagebox.showinfo("Login Successfull","Login Successfull")
            elif T1.get() == "Oscin" and T2.get()=="123":
                controller.show_frame(homepage)
                messagebox.showinfo("Login Successfull","Login Successfull")
            elif T1.get() == "Khalid Mirza" and T2.get()=="12345":
                controller.show_frame(homepage)
                messagebox.showinfo("Login Successfull","Login Successfull")
            elif T1.get() == "xyz" and T2.get()=="123":
                controller.show_frame(homepage)
                messagebox.showinfo("Login Successfull","Login Successfull")
            else:
                messagebox.showinfo("Error", "Invalid Username or Password")

        Button = tk.Button(self, text="Login", font=(FONT_NAME, 15),
                           command= verify)
        Button.place(x=675, y=500)
        def add_new_user():
            name = T1.get()
            password = T2.get() 
            messagebox.showinfo("Added","New User Added")
        # Button = tk.Button(self, text="Add New User", font=(FONT_NAME, 15),
        #                    command= add_new_user)
        # Button.place(x=625, y=550)



class homepage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbltitle = tk.Label(self, bd=20, relief=RIDGE, text="ORDER MANAGEMENT SYSTEM", fg="black", bg="white",
                            font=("Courier", 50, "bold"))
        lbltitle.place(x=227,y=0)

        Label2 = tk.Label(self, text="What data would you like to access?", font=(FONT_NAME, 15, "bold"))
        Label2.place(x=500, y=200)
        Button = tk.Button(self, text="Customer Details", font=(FONT_NAME, 15), command=lambda: controller.show_frame(Customer))
        Button.place(x=600, y=250)
        Button = tk.Button(self, text="Order Details", font=(FONT_NAME, 15), command=lambda: controller.show_frame(Order))
        Button.place(x=600, y=300)
        Button = tk.Button(self, text="Product Details", font=(FONT_NAME, 15), command=lambda: controller.show_frame(Product))
        Button.place(x=600, y=350)
        Button = tk.Button(self, text="Store Details", font=(FONT_NAME, 15), command=lambda: controller.show_frame(Store))
        Button.place(x=600, y=400)

        Dataframe = Frame(self, bd=15, relief= RIDGE)
        Dataframe.place(x=2,y=115,width=1350, height=55)
        def selected(event):
            if clicked.get() == 'User':
                controller.show_frame(User)
            elif clicked.get() == 'Employee':
                controller.show_frame(Employee)
            elif clicked.get()== 'Exit':
                iexit=tkinter.messagebox.askyesno("Order Manangement System", "Do you want to exit?")
                if iexit>0:
                    self.destroy()
                    return

        options = [ "Menu Bar","User", "Employee", "Exit"]
        clicked = StringVar()
        clicked.set(options[0])
        drop = OptionMenu(self, clicked,*options, command= selected)
        drop.place(x=18,y=127,width=100)

class Customer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lbltitle = tk.Label(self, bd=20, relief=RIDGE, text="Customer Details", fg="black", bg="white",
                            font=("Courier", 50, "bold"))
        lbltitle.place(x=350,y=0)

        self.CustomerID_var = StringVar()
        self.CustomerName_var = StringVar()
        self.ContactNo_var = StringVar()
        self.Address_var = StringVar()
        self.OrderID_var = StringVar()
        self.ProductID_var = StringVar()
        self.Amount_var = StringVar()


        # lbltitle =Label(self,bd=20, relief= RIDGE, text="ORDER MANAGEMENT SYSTEM", fg="red", bg="white", font=("Times new roman", 50, "bold"))
        # lbltitle.pack(side=TOP)

        Dataframe = Frame(self, bd=15, relief= RIDGE)
        Dataframe.place(x=0,y=130,width=1330, height=300)
        DataframeCenter = LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,
                                        font=("times new roman", 12, "bold"), text="Customer Information")
        DataframeCenter.place(x=0,y=5, width=1280, height=250)

        lblmember = Label(DataframeCenter, bg = "powder blue",text= "Customer Name", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblmember.grid(row=0, column=0, sticky= W)
        textmember = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable=self.CustomerName_var, width= 27)
        textmember.grid(row=0, column=1)

        lblid = Label(DataframeCenter, bg = "powder blue", text= "Customer ID", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblid.grid(row=1, column=0, sticky= W)
        textid = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.CustomerID_var, width= 27)
        textid.grid(row=1, column=1)

        lblno = Label(DataframeCenter, bg = "powder blue", text= "Contact No", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblno.grid(row=2, column=0, sticky= W)
        textno = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.ContactNo_var, width= 27)
        textno.grid(row=2, column=1)

        lbladd = Label(DataframeCenter, bg = "powder blue", text= "Address", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lbladd.grid(row=3, column=0, sticky= W)
        textadd = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.Address_var, width= 27)
        textadd.grid(row=3, column=1)

        lblorder = Label(DataframeCenter, bg = "powder blue", text= "OrderID", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblorder.grid(row=4, column=0, sticky= W)
        textorder = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.OrderID_var, width= 27)
        textorder.grid(row=4, column=1)

        lblproduct = Label(DataframeCenter, bg = "powder blue", text= "ProductID", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblproduct.grid(row=5, column=0, sticky= W)
        textproduct = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.ProductID_var, width= 27)
        textproduct.grid(row=5, column=1)

        lblamount = Label(DataframeCenter, bg = "powder blue", text= "Amount", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblamount.grid(row=6, column=0, sticky= W)
        textamount = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.Amount_var, width= 27)
        textamount.grid(row=6, column=1)

        Buttonframe = Frame(self, bd=10, relief= RIDGE)
        Buttonframe.place(x=20, y=440, width=1256, height=50)

        btnadddata = Button(Buttonframe,command=self.adddata, text="Add", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=0)

        btnadddata = Button(Buttonframe,command= self.delete, text="Delete", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=1)

        btnadddata = Button(Buttonframe,command= self.update, text="Update", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=2)

        btnadddata = Button(Buttonframe,command= self.iexit, text="Exit", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=3)

        Detailsframe = Frame(self, bd=10, relief= RIDGE)
        Detailsframe.place(x=0, y=500, width=1330, height=180)

        self.customer_table = ttk.Treeview(Detailsframe, column=("Customer ID", "Customer Name", "Contact No", "Address", "OrderID","ProductID","Amount"))

        self.customer_table.heading("Customer ID", text= "Customer ID")
        self.customer_table.heading("Customer Name", text= "Customer Name")
        self.customer_table.heading("Contact No", text= "Contact No")
        self.customer_table.heading("Address", text= "Address")
        self.customer_table.heading("OrderID", text= "OrderID")
        self.customer_table.heading("ProductID", text= "ProductID")
        self.customer_table.heading("Amount", text= "Amount")
        self.customer_table["show"] = "headings"
        self.customer_table.pack(fill = BOTH, expand = 1)

        self.fetchdata()
        self.customer_table.bind("<ButtonRelease-1>",self.get_cursor)

    def adddata(self):
        conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
        my_cursor= conn.cursor()
        my_cursor.execute("INSERT INTO customer VALUES(%s,%s,%s,%s,%s,%s,%s)",(self.CustomerID_var.get(),self.CustomerName_var.get(),self.ContactNo_var.get(),self.Address_var.get(),self.OrderID_var.get(),self.ProductID_var.get(),self.Amount_var.get()))
        conn.commit()
        self.fetchdata()
        conn.close()
        messagebox.showinfo("Success","Member has been inserted successfully")
    
    def fetchdata(self):
        conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
        my_cursor= conn.cursor()
        my_cursor.execute("select * from customer ")
        rows = my_cursor.fetchall()
        if len(rows) !=0:
            self.customer_table.delete(*self.customer_table.get_children())
            for i in rows:
                self.customer_table.insert("", END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event= ""):
        cursor_row = self.customer_table.focus()
        content = self.customer_table.item(cursor_row)
        row = content['values']

        self.CustomerID_var.set(row[0]),
        self.CustomerName_var.set(row[1]),
        self.ContactNo_var.set(row[2]),
        self.Address_var.set(row[3]),
        self.OrderID_var.set(row[4]),
        self.ProductID_var.set(row[5]),
        self.Amount_var.set(row[6])

    def delete(self):
        
        if self.CustomerID_var.get()== "" or self.CustomerName_var== "":
            messagebox.showerror("Error","Select any Member to delete")
        else:
            conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
            my_cursor= conn.cursor()
            query = "DELETE from db1.customer WHERE `Customer ID`= %s "
            val = (self.CustomerID_var.get(),)
            my_cursor.execute(query,val)
            conn.commit()
            self.fetchdata()
            conn.close()
            messagebox.showinfo("Success", "Member has been deleted")

    def update(self):
        conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
        my_cursor= conn.cursor()
        my_cursor.execute("update db1.customer set `Customer Name`= %s, `Contact No`= %s, `Address`= %s, `Order ID`= %s, `Product ID`= %s, `Amount`= %s where `Customer ID`= %s",(self.CustomerName_var.get(),self.ContactNo_var.get(),self.Address_var.get(),self.OrderID_var.get(),self.ProductID_var.get(),self.Amount_var.get(),self.CustomerID_var.get(), ))
        conn.commit()
        self.fetchdata()
        conn.close()
        messagebox.showinfo("Success","Changes have been made successfully")

    def iexit(self):
        iexit=tkinter.messagebox.askyesno("Order Manangement System", "Do you want to exit?")
        if iexit>0:
            self.destroy()
            return

class Order(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lbltitle = tk.Label(self, bd=20, relief=RIDGE, text="Order Details", fg="black", bg="white",
                            font=("Courier", 50, "bold"))
        lbltitle.place(x=370,y=0)

        self.OrderID_var = StringVar()
        self.ProductID_var = StringVar()
        self.Date_var = StringVar()
        self.Amount_var = StringVar()
        self.Quantity_var = StringVar()


        # lbltitle =Label(self,bd=20, relief= RIDGE, text="ORDER MANAGEMENT SYSTEM", fg="red", bg="white", font=("Times new roman", 50, "bold"))
        # lbltitle.pack(side=TOP)

        Dataframe = Frame(self, bd=15, relief= RIDGE)
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

        lblamount = Label(DataframeCenter, bg = "powder blue", text= "Amount", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblamount.grid(row=3, column=0, sticky= W)
        textamount = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.Amount_var, width= 27)
        textamount.grid(row=3, column=1)

        lblqua = Label(DataframeCenter, bg = "powder blue", text= "Quantity", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblqua.grid(row=4, column=0, sticky= W)
        textqua = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.Quantity_var, width= 27)
        textqua.grid(row=4, column=1)


        Buttonframe = Frame(self, bd=10, relief= RIDGE)
        Buttonframe.place(x=20, y=440, width=1256, height=50)

        btnadddata = Button(Buttonframe,command=self.adddata, text="Add", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=0)

        btnadddata = Button(Buttonframe,command= self.delete, text="Delete", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=1)

        btnadddata = Button(Buttonframe,command= self.update, text="Update", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=2)

        btnadddata = Button(Buttonframe,command= self.iexit, text="Exit", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=3)

        Detailsframe = Frame(self, bd=10, relief= RIDGE)
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
        iexit=tkinter.messagebox.askyesno("Order Manangement System", "Do you want to exit?")
        if iexit>0:
            self.destroy()
            return

class Employee(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lbltitle = tk.Label(self, bd=20, relief=RIDGE, text="Employee Details", fg="black", bg="white",
                            font=("Courier", 50, "bold"))
        lbltitle.pack(side=TOP)
    
        self.EmployeeID_var = StringVar()
        self.EmployeeName_var = StringVar()
        self.ContactNo_var = StringVar()
        self.Address_var = StringVar()
        self.Branch_var = StringVar()


        # lbltitle =Label(self,bd=20, relief= RIDGE, text="ORDER MANAGEMENT SYSTEM", fg="red", bg="white", font=("Times new roman", 50, "bold"))
        # lbltitle.pack(side=TOP)

        Dataframe = Frame(self, bd=15, relief= RIDGE)
        Dataframe.place(x=0,y=130,width=1330, height=300)
        DataframeCenter = LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,
                                        font=("times new roman", 12, "bold"), text="Employee Information")
        DataframeCenter.place(x=0,y=5, width=1280, height=250)

        lblmember = Label(DataframeCenter, bg = "powder blue",text= "Employee Name", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblmember.grid(row=0, column=0, sticky= W)
        textmember = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable=self.EmployeeName_var, width= 27)
        textmember.grid(row=0, column=1)

        lblid = Label(DataframeCenter, bg = "powder blue", text= "Employee ID", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblid.grid(row=1, column=0, sticky= W)
        textid = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.EmployeeID_var, width= 27)
        textid.grid(row=1, column=1)

        lblno = Label(DataframeCenter, bg = "powder blue", text= "Contact No", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblno.grid(row=2, column=0, sticky= W)
        textno = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.ContactNo_var, width= 27)
        textno.grid(row=2, column=1)

        lbladd = Label(DataframeCenter, bg = "powder blue", text= "Address", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lbladd.grid(row=3, column=0, sticky= W)
        textadd = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.Address_var, width= 27)
        textadd.grid(row=3, column=1)

        lblbranch = Label(DataframeCenter, bg = "powder blue", text= "Branch", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblbranch.grid(row=4, column=0, sticky= W)
        textbranch = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.Branch_var, width= 27)
        textbranch.grid(row=4, column=1)


        Buttonframe = Frame(self, bd=10, relief= RIDGE)
        Buttonframe.place(x=20, y=440, width=1350, height=50)

        btnadddata = Button(Buttonframe,command=self.adddata, text="Add", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=0)

        btnadddata = Button(Buttonframe,command= self.delete, text="Delete", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=1)

        btnadddata = Button(Buttonframe,command=self.update, text="Update", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=2)

        btnadddata = Button(Buttonframe,command= self.iexit, text="Exit", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=3)

        Detailsframe = Frame(self, bd=10, relief= RIDGE)
        Detailsframe.place(x=0, y=500, width=1330, height=180)

        yscroll = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.employee_table = ttk.Treeview(Detailsframe, column=("Employee ID", "Employee Name", "Contact No", "Address", "Branch"))

        self.employee_table.heading("Employee ID", text= "Employee ID")
        self.employee_table.heading("Employee Name", text= "Employee Name")
        self.employee_table.heading("Contact No", text= "Contact No")
        self.employee_table.heading("Address", text= "Address")
        self.employee_table.heading("Branch", text= "Branch")
        self.employee_table["show"] = "headings"
        self.employee_table.pack(fill = BOTH, expand = 1)

        self.fetchdata()
        self.employee_table.bind("<ButtonRelease-1>",self.get_cursor)

    def adddata(self):
        conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
        my_cursor= conn.cursor()
        my_cursor.execute("INSERT INTO employee VALUES(%s,%s,%s,%s,%s)",(self.EmployeeID_var.get(),self.EmployeeName_var.get(),self.ContactNo_var.get(),self.Address_var.get(),self.Branch_var.get()))
        conn.commit()
        self.fetchdata()
        conn.close()
        messagebox.showinfo("Success","Member has been inserted successfully")
    
    def update(self):
        conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
        my_cursor= conn.cursor()
        my_cursor.execute("update db1.employee set `Employee Name`= %s, `Contact No`= %s, `Address`= %s, `Branch`= %s where `Employee ID`= %s",(self.EmployeeName_var.get(),self.ContactNo_var.get(),self.Address_var.get(),self.Branch_var.get(),self.EmployeeID_var.get(), ))
        conn.commit()
        self.fetchdata()
        conn.close()
        messagebox.showinfo("Success","Changes have been made successfully")

    def fetchdata(self):
        conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
        my_cursor= conn.cursor()
        my_cursor.execute("select * from employee ")
        rows = my_cursor.fetchall()
        if len(rows) !=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in rows:
                self.employee_table.insert("", END,values=i)
            conn.commit()
        conn.close()
    
    def delete(self):
        val = (self.EmployeeID_var.get(),)
        if self.EmployeeID_var.get()== "" or self.EmployeeName_var== "":
            messagebox.showerror("Error","Select any Member to delete")
        else:
            conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
            my_cursor= conn.cursor()
            query = "DELETE from db1.employee WHERE `Employee ID`= %s; "
            val = (self.EmployeeID_var.get(),)
            my_cursor.execute(query,val)
            conn.commit()
            self.fetchdata()
            conn.close()
            messagebox.showinfo("Success", "Member has been deleted")


    
    def get_cursor(self, event= ""):
        cursor_row = self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        row = content['values']

        self.EmployeeID_var.set(row[0]),
        self.EmployeeName_var.set(row[1]),
        self.ContactNo_var.set(row[2]),
        self.Address_var.set(row[3]),
        self.Branch_var.set(row[4])

    def iexit(self):
        iexit=tkinter.messagebox.askyesno("Order Manangement System", "Do you want to exit?")
        if iexit>0:
            self.destroy()
            return

class Product(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lbltitle = tk.Label(self, bd=20, relief=RIDGE, text="Product Details", fg="black", bg="white",
                            font=("Courier", 50, "bold"))
        lbltitle.place(x=350, y=0)
        self.ProductID_var = StringVar()
        self.ProductName_var = StringVar()
        self.StoreID_var = StringVar()
        self.Amount_var = StringVar()
        self.Quantity_var = StringVar()


        # lbltitle =Label(self,bd=20, relief= RIDGE, text="ORDER MANAGEMENT SYSTEM", fg="red", bg="white", font=("Times new roman", 50, "bold"))
        # lbltitle.pack(side=TOP)

        Dataframe = Frame(self, bd=15, relief= RIDGE)
        Dataframe.place(x=0,y=130,width=1330, height=300)
        DataframeCenter = LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,
                                        font=("times new roman", 12, "bold"), text="Product Information")
        DataframeCenter.place(x=0,y=5, width=1280, height=250)

        lblid1 = Label(DataframeCenter, bg = "powder blue",text= "Product ID", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblid1.grid(row=0, column=0, sticky= W)
        textid1 = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable=self.ProductID_var, width= 27)
        textid1.grid(row=0, column=1)

        lblid = Label(DataframeCenter, bg = "powder blue", text= "Product Name", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblid.grid(row=1, column=0, sticky= W)
        textid = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.ProductName_var, width= 27)
        textid.grid(row=1, column=1)

        lblsid = Label(DataframeCenter, bg = "powder blue", text= "Store ID", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblsid.grid(row=2, column=0, sticky= W)
        textsid = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.StoreID_var, width= 27)
        textsid.grid(row=2, column=1)

        lblamount = Label(DataframeCenter, bg = "powder blue", text= "Amount", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblamount.grid(row=3, column=0, sticky= W)
        textamount = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.Amount_var, width= 27)
        textamount.grid(row=3, column=1)

        lblqua = Label(DataframeCenter, bg = "powder blue", text= "Quantity", font=("times new roman", 15, "bold"), padx=2,pady=2)
        lblqua.grid(row=4, column=0, sticky= W)
        textqua = Entry(DataframeCenter, font=("arial", 12,"bold"),textvariable= self.Quantity_var, width= 27)
        textqua.grid(row=4, column=1)


        Buttonframe = Frame(self, bd=10, relief= RIDGE)
        Buttonframe.place(x=20, y=440, width=1256, height=50)

        btnadddata = Button(Buttonframe,command=self.adddata, text="Add", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=0)

        btnadddata = Button(Buttonframe,command= self.delete, text="Delete", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=1)

        btnadddata = Button(Buttonframe,command= self.update, text="Update", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=2)

        btnadddata = Button(Buttonframe,command= self.iexit, text="Exit", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=3)

        Detailsframe = Frame(self, bd=10, relief= RIDGE)
        Detailsframe.place(x=0, y=500, width=1330, height=180)

        yscroll = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.product_table = ttk.Treeview(Detailsframe, column=("Product ID", "Product Name", "Store ID", "Amount", "Quantity"))

        self.product_table.heading("Product ID", text= "Product ID")
        self.product_table.heading("Product Name", text= "Product Name")
        self.product_table.heading("Store ID", text= "Store ID")
        self.product_table.heading("Amount", text= "Amount")
        self.product_table.heading("Quantity", text= "Quantity")
        self.product_table["show"] = "headings"
        self.product_table.pack(fill = BOTH, expand = 1)

        self.fetchdata()
        self.product_table.bind("<ButtonRelease-1>",self.get_cursor)

    def adddata(self):
        conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
        my_cursor= conn.cursor()
        my_cursor.execute("INSERT INTO db1.product VALUES (%s,%s,%s,%s,%s)",(self.ProductID_var.get(),self.ProductName_var.get(),self.StoreID_var.get(),self.Amount_var.get(),self.Quantity_var.get()))
        conn.commit()
        self.fetchdata()
        conn.close()
        messagebox.showinfo("Success","Member has been inserted successfully")

    def fetchdata(self):
        conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
        my_cursor= conn.cursor()
        my_cursor.execute("select * from db1.product")
        rows = my_cursor.fetchall()
        if len(rows) !=0:
            self.product_table.delete(*self.product_table.get_children())
            for i in rows:
                self.product_table.insert("", END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self, event= ""):
        cursor_row = self.product_table.focus()
        content = self.product_table.item(cursor_row)
        row = content['values']

        self.ProductID_var.set(row[0]),
        self.ProductName_var.set(row[1]),
        self.StoreID_var.set(row[2]),
        self.Amount_var.set(row[3]),
        self.Quantity_var.set(row[4])

    def update(self):
        conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
        my_cursor= conn.cursor()
        my_cursor.execute("update db1.product set `Product Name`= %s, `Store ID`= %s, `Amount`= %s, `Quantity`= %s where `Product ID`= %s",(self.ProductName_var.get(),self.StoreID_var.get(),self.Amount_var.get(),self.Quantity_var.get(),self.ProductID_var.get(), ))
        conn.commit()
        self.fetchdata()
        conn.close()
        messagebox.showinfo("Success","Changes have been made successfully")

    
    def delete(self):
        val = (self.ProductID_var.get(),)
        if self.ProductID_var.get()== "" or self.ProductName_var== "":
            messagebox.showerror("Error","Select any Member to delete")
        else:
            conn = mysql.connector.connect(host="localhost",username = "root", password = "oscin12345", database = "db1")
            my_cursor= conn.cursor()
            query = "DELETE from db1.product WHERE `Product ID`= %s; "
            val = (self.ProductID_var.get(),)
            my_cursor.execute(query,val)
            conn.commit()
            self.fetchdata()
            conn.close()
            messagebox.showinfo("Success", "Member has been deleted")

    def iexit(self):
        iexit=tkinter.messagebox.askyesno("Order Manangement System", "Do you want to exit?")
        if iexit>0:
            self.destroy()
            return

class Store(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lbltitle = tk.Label(self, bd=20, relief=RIDGE, text="Store Details", fg="black", bg="white",
                            font=("Courier", 50, "bold"))
        lbltitle.pack(side=TOP)
        self.StoreID_var = StringVar()
        self.Address_var = StringVar()
        
        # lbltitle =Label(self,bd=20, relief= RIDGE, text="ORDER MANAGEMENT SYSTEM", fg="red", bg="white", font=("Times new roman", 50, "bold"))
        # lbltitle.pack(side=TOP)

        Dataframe = Frame(self, bd=15, relief= RIDGE)
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


        Buttonframe = Frame(self, bd=10, relief= RIDGE)
        Buttonframe.place(x=20, y=440, width=1350, height=50)

        btnadddata = Button(Buttonframe,command=self.adddata, text="Add", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=0)

        btnadddata = Button(Buttonframe,command= self.delete, text="Delete", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=1)

        btnadddata = Button(Buttonframe,command= self.update, text="Update", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=2)

        btnadddata = Button(Buttonframe,command= self.iexit, text="Exit", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=3)

        Detailsframe = Frame(self, bd=10, relief= RIDGE)
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
        iexit=tkinter.messagebox.askyesno("Order Manangement System", "Do you want to exit?")
        if iexit>0:
            self.destroy()
            return

class User(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lbltitle = tk.Label(self, bd=20, relief=RIDGE, text="User Details", fg="black", bg="white",
                            font=("Courier", 50, "bold"))
        lbltitle.place(x=350,y=0)
        self.UserID_var = StringVar()
        self.FN_var = StringVar()
        self.LN_var = StringVar()
        self.UN_var = StringVar()
        self.PSD_var = StringVar()

        # lbltitle =Label(self,bd=20, relief= RIDGE, text="ORDER MANAGEMENT SYSTEM", fg="red", bg="white", font=("Times new roman", 50, "bold"))
        # lbltitle.pack(side=TOP)

        Dataframe = Frame(self, bd=15, relief= RIDGE)
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


        Buttonframe = Frame(self, bd=10, relief= RIDGE)
        Buttonframe.place(x=20, y=440, width=1256, height=50)

        btnadddata = Button(Buttonframe,command=self.adddata, text="Add", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=0)

        btnadddata = Button(Buttonframe,command= self.delete, text="Delete", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=1)

        btnadddata = Button(Buttonframe,command= self.update, text="Update", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=2)

        btnadddata = Button(Buttonframe,command= self.iexit, text="Exit", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=3)

        Detailsframe = Frame(self, bd=10, relief= RIDGE)
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
        iexit=tkinter.messagebox.askyesno("Order Manangement System", "Do you want to exit?")
        if iexit>0:
            self.destroy()
            return

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize=1000)
        window.grid_columnconfigure(0, minsize=1500)
        self.frames = {}
        for F in (loginpage, homepage, User, Employee, Customer,Order ,Store, Product):
            Frame = F(window, self)
            self.frames[F] = Frame
            Frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(loginpage)

    def show_frame(self, page):
        Frame = self.frames[page]
        Frame.tkraise()

if __name__ == "__main__":
    app = Application()
    app.title("Order Management System")

    app.mainloop()
