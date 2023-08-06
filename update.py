# import all the modules
from tkinter import *
import sqlite3
import tkinter.messagebox


conn = sqlite3.connect("D:\Store Management Softwere\Database\store.db")
c = conn.cursor()

result = c.execute("Select Max(id) from inventory")
for r in result:
    id = r[0]


class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Update the database", font='arial 40 bold', fg='steelblue')
        self.heading.place(x=400, y=0)

        # label and entry for id
        self.id_1 = Label(master, text="Enter id", font='arial 18 bold')
        self.id_1.place(x=0, y=70)

        self.id_1e = Entry(master, font='arial 15 bold', width=10)
        self.id_1e.place(x=380, y=70)

        self.btn_search  = Button(master, text="Search", width=15, height=2, bg="orange", command=self.Search)
        self.btn_search.place(x=570, y=70)
        
        # label for the window
        self.name = Label(master, text="Enter Product Name", font='arial 18 bold')
        self.name.place(x=0, y=120)

        self.stock = Label(master, text="Enter Stocks", font='arial 18 bold')
        self.stock.place(x=0, y=170)

        self.cp = Label(master, text="Enter Cost Price", font='arial 18 bold')
        self.cp.place(x=0, y=220)

        self.sp = Label(master, text="Enter Selling Price", font='arial 18 bold')
        self.sp.place(x=0, y=270)

        self.totalcp = Label(master, text="Enter total cost Price", font='arial 18 bold')
        self.totalcp.place(x=0, y=320)

        self.totalsp = Label(master, text="Enter total Selling Price", font='arial 18 bold')
        self.totalsp.place(x=0, y=370)

        self.vendor = Label(master, text="Enter Vendor Name", font='arial 18 bold')
        self.vendor.place(x=0, y=420)

        self.vendor_phonenumber = Label(master, text="Enter Vendor Phone Number", font='arial 18 bold')
        self.vendor_phonenumber.place(x=0, y=470)
        
        # entries for the labels
        self.name_e = Entry(master, width=25, font='arial 15 bold')
        self.name_e.place(x=360, y=120)

        self.stock_e = Entry(master, width=25, font='arial 15 bold')
        self.stock_e.place(x=360, y=170)

        self.cp_e = Entry(master, width=25, font='arial 15 bold')
        self.cp_e.place(x=360, y=220)

        self.sp_e = Entry(master, width=25, font='arial 15 bold')
        self.sp_e.place(x=360, y=270)

        self.totalcp_e = Entry(master, width=25, font='arial 15 bold')
        self.totalcp_e.place(x=360, y=320)

        self.totalsp_e = Entry(master, width=25, font='arial 15 bold')
        self.totalsp_e.place(x=360, y=370)

        self.vendor_e = Entry(master, width=25, font='arial 15 bold')
        self.vendor_e.place(x=360, y=420)

        self.vendor_phonenumber_e = Entry(master, width=25, font='arial 15 bold')
        self.vendor_phonenumber_e.place(x=360, y=470)
        
        # button to add to the database
        self.btn_add = Button(master, text="Update Database", width=20, height=1, bg='steelblue',
                              fg='white', command=self.update)
        self.btn_add.place(x=490, y=520)
        
        # text box for the logs
        self.tBox = Text(master, width=60, height=17)
        self.tBox.place(x=750, y=70)
        
        self.tBox.insert(END, "ID has reached upto: " + str(id))

    def Search(self, *args, **kwargs):
        sql = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(sql, (self.id_1e.get(), ))

        for r in result:
            self.n1 = r[1]  # name
            self.n2 = r[2]  # stock
            self.n3 = r[3]  # cp
            self.n4 = r[4]  # sp
            self.n5 = r[5]  # totalcp
            self.n6 = r[6]  # totalsp
            self.n7 = r[7]  # assumed_profit
            self.n8 = r[8]  # vendor
            self.n9 = r[9]  # vendor_phonenumber

        conn.commit()
        
        # delete the last entry and update
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendor_phonenumber_e.delete(0, END)
        self.totalcp_e.delete(0, END)
        self.totalsp_e.delete(0, END)

        # insert into the entry to update
        self.name_e.insert(0, self.n1)
        self.stock_e.insert(0, self.n2)
        self.cp_e.insert(0, self.n3)
        self.sp_e.insert(0, self.n4)
        self.totalcp_e.insert(0, self.n5)
        self.totalsp_e.insert(0, self.n6)
        self.vendor_e.insert(0, self.n8)
        self.vendor_phonenumber_e.insert(0, self.n9)

    def update(self, *args, **kwargs):
        # get all the updated values
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.totalcp = self.totalcp_e.get()
        self.totalsp = self.totalsp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phonenumber = self.vendor_phonenumber_e.get()

        query = "UPDATE inventory SET name=?, stock=?, cp=?, sp=?, totalcp=?, totalsp=?, vendor=?, vendor_phonenumber=? WHERE id=?"
        c.execute(query, (self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.vendor, self.vendor_phonenumber, self.id_1e.get(), ))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Update database successfully")


root = Tk()
b = Database(root)

root.geometry("1366x768+0+0")
root.title("Update the database")
root.mainloop()
