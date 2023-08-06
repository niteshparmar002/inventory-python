# import all the modules
from tkinter import *
import sqlite3
import tkinter.messagebox


conn = sqlite3.connect("D:\Store Management Softwere\Database\store.db")
c = conn.cursor()

result = c.execute("Select Max(id) from inventory")
for r in result:
    Id = r[0]


class Database:
    def __init__(self, master):
        
        self.master = master
        self.heading = Label(master, text="Add to the database", font='arial 40 bold', fg='steelblue')
        self.heading.place(x=400, y=0)
        
        # label for the window
        self.name = Label(master, text="Enter Product Name", font='arial 18 bold')
        self.name.place(x=0, y=70)

        self.stock = Label(master, text="Enter Stocks", font='arial 18 bold')
        self.stock.place(x=0, y=120)

        self.cp = Label(master, text="Enter Cost Price", font='arial 18 bold')
        self.cp.place(x=0, y=170)

        self.sp = Label(master, text="Enter Selling Price", font='arial 18 bold')
        self.sp.place(x=0, y=220)

        self.vendor = Label(master, text="Enter Vendor Name", font='arial 18 bold')
        self.vendor.place(x=0, y=270)

        self.vendor_phonenumber = Label(master, text="Enter Vendor Phone Number", font='arial 18 bold')
        self.vendor_phonenumber.place(x=0, y=320)

        self.id = Label(master, text="Enter ID", font='arial 18 bold')
        self.id.place(x=0, y=370)
        
        # entries for the labels
        self.name_e = Entry(master, width=25, font='arial 15 bold')
        self.name_e.place(x=360, y=70)

        self.stock_e = Entry(master, width=25, font='arial 15 bold')
        self.stock_e.place(x=360, y=120)

        self.cp_e = Entry(master, width=25, font='arial 15 bold')
        self.cp_e.place(x=360, y=170)

        self.sp_e = Entry(master, width=25, font='arial 15 bold')
        self.sp_e.place(x=360, y=220)

        self.vendor_e = Entry(master, width=25, font='arial 15 bold')
        self.vendor_e.place(x=360, y=270)

        self.vendor_phonenumber_e = Entry(master, width=25, font='arial 15 bold')
        self.vendor_phonenumber_e.place(x=360, y=320)
        
        self.id_e = Entry(master, width=25, font='arial 15 bold')
        self.id_e.place(x=360, y=370)
        
        # button to add to the database
        self.btn_add = Button(master, text="Add To Database", width=20, height=1, bg='steelblue',
                              fg='white', command=self.get_items)
        self.btn_add.place(x=490, y=420)
        
        self.btn_clear = Button(master, text="Clear All Fields", width=18, height=1, bg="lightgreen",
                                fg="white", command=self.clear_all)
        self.btn_clear.place(x=320, y=420)
        
        # text box for the logs
        self.tBox = Text(master, width=60, height=17)
        self.tBox.place(x=750, y=70)
        
        self.tBox.insert(END, "ID has reached upto: " + str(id))
        
    def get_items(self):
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phonenumber = self.vendor_phonenumber_e.get()

        # dynamics entries
        self.assumed_profit = float(self.totalsp - self.totalcp)
        self.totalsp = float(self.sp) * float(self.stock)
        self.totalcp = float(self.cp) * float(self.stock)

        if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '':
            tkinter.messagebox.showinfo("Error", "Please fill all the entries")
        else:
            sql = "Insert into inventory(name, stock, cp, sp, totalcp, totalsp, assume_profit, " \
                  "vendor, vendor_phonenumber) VALUES(?,?,?,?,?,?,?,?,?)"
            c.execute(sql, (self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp,
                            self.assumed_profit, self.vendor, self.vendor_phonenumber))
            conn.commit()
            self.tBox.insert(END, "\n\nInserted" + str(self.name) + "into the database with code" +
                             str(self.id_e.get()))
            
            tkinter.messagebox.showinfo("Success", "Successfully added to the database")
            
    def clear_all(self, *args, **kwargs):
        num = Id + 1
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendor_phonenumber_e.delete(0, END)
        self.id_e.delete(0, END)


root = Tk()
b = Database(root)

root.geometry("1366x768+0+0")
root.title("Add to the database")
root.mainloop()
