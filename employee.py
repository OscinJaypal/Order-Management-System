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


class Employee:

    def __init__(self,root):
        self.root= root
        self.root.title("Order Management System")
        self.root.geometry ("1540x800+0+0")

        self.EmployeeID_var = StringVar()
        self.EmployeeName_var = StringVar()
        self.ContactNo_var = StringVar()
        self.Address_var = StringVar()
        self.Branch_var = StringVar()


        lbltitle =Label(self.root,bd=20, relief= RIDGE, text="ORDER MANAGEMENT SYSTEM", fg="red", bg="white", font=("Times new roman", 50, "bold"))
        lbltitle.pack(side=TOP)

        Dataframe = Frame(self.root, bd=15, relief= RIDGE)
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


        Buttonframe = Frame(self.root, bd=10, relief= RIDGE)
        Buttonframe.place(x=20, y=440, width=1350, height=50)

        btnadddata = Button(Buttonframe,command=self.adddata, text="Add", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=0)

        btnadddata = Button(Buttonframe,command= self.delete, text="Delete", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=1)

        btnadddata = Button(Buttonframe,command=self.update, text="Update", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=2)

        btnadddata = Button(Buttonframe,command= self.iexit, text="Exit", font=("arial", 12, "bold"), width= 30, bg="blue", fg="white")
        btnadddata.grid(row=0, column=3)

        Detailsframe = Frame(self.root, bd=10, relief= RIDGE)
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
        iexit=tkinter.messagebox.askyesno("Order Manangement System", "Do yoy want to exit?")
        if iexit>0:
            self.root.destroy()
            return

if __name__ == "__main__":
    root = Tk()
    ob= Employee(root)
    root.mainloop()