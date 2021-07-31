from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime



class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1366x768+0+0")

        # =================================Variable===============================
        
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue=StringVar()
        self.finallprice=StringVar()


        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green",bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE,padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1360, height=360)

        # ============================Data Frame Left ====================================
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue",fg="green", bd=12, relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=800, height=350)

        lblMember = Label(DataFrameLeft,font=("arial", 12, "bold"),text="Member Type",padx=2, pady=6,bg="powder blue")
        lblMember.grid(row=0, column=0, sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,state="readonly",font=("arial", 12, "bold"), width=27)
        comMember["value"] = ("Admin Staf", "Lecturer","Student", )
        comMember.current(0)
        comMember.grid(row=0, column=1)

        lblref = Label(DataFrameLeft, bg="powder blue", text="PRN  No", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.prn_var, width=29)
        txtref.grid(row=1, column=1)
       
        lblTitle = Label(DataFrameLeft, bg="powder blue", text="ID  No", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.id_var, width=29)
        txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, bg="powder blue", text="First Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.firstname_var, width=29)
        txtFirstName.grid(row=3, column=1)


        lblLastName = Label(DataFrameLeft, bg="powder blue", text="Last Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.lastname_var, width=29)
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, bg="powder blue", text="Address1", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.address1_var, width=29)
        txtAddress1.grid(row=5, column=1)


        lblAddress2 = Label(DataFrameLeft, bg="powder blue", text="Address2", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.address2_var, width=29)
        txtAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, bg="powder blue", text="Post Code", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.postcode_var, width=29)
        txtPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, bg="powder blue", text="Mobile", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.mobile_var, width=29)
        txtMobile.grid(row=8, column=1)

        lblBookId = Label(DataFrameLeft, bg="powder blue", text="Book Id", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.bookid_var, width=29)
        txtBookId.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, bg="powder blue", text="Book Title", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.booktitle_var, width=29)
        txtBookTitle.grid(row=1, column=3)

        lblAuther = Label(DataFrameLeft, bg="powder blue", text="Auther Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblAuther.grid(row=2, column=2, sticky=W)
        txtAuther = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.auther_var, width=29)
        txtAuther.grid(row=2, column=3)

        lblDateBorrowed = Label(DataFrameLeft, bg="powder blue", text="Date Borrowed", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.dateborrowed_var, width=29)
        txtDateBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, bg="powder blue", text="Date Due", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.datedue_var, width=29)
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(DataFrameLeft, bg="powder blue", text="Days On Book", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.daysonbook, width=29)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, bg="powder blue", text="Late Return Fine", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.lateratefine_var, width=29)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverDate = Label(DataFrameLeft, bg="powder blue", text="Date Over Due", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblDateOverDate.grid(row=7, column=2, sticky=W)
        txtDateOverDate = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.dateoverdue, width=29)
        txtDateOverDate.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, bg="powder blue", text="Actual Price", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.finallprice, width=29)
        txtActualPrice.grid(row=8, column=3)


        # ========================Data Frame Right============================


        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue",fg="green", bd=12, relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameRight.place(x=810, y=5, width=500, height=350)


        self.txtBox=Text(DataFrameRight, font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Head First Book', 'Learn Python The Hard Way','Python Programming','Python CookBook','Intro to Machine Learning','Machine tecno','My Python','My python','Elite Jungle Python','Machine Python','Advanced Python','Inton Python','RedChilli Python','Head First Book', 'Learn Python The Hard Way','Python Programming','Python CookBook','Intro to Machine Learning','Machine tecno','My Python','My python','Elite Jungle Python','Machine Python','Advanced Python','Inton Python','RedChilli Python'
        ]


        # All Books details added here 


        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Head First Book"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("bdt.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("bdt.788")



                
            elif (x=="Learn Python The Hard Way"):
                self.bookid_var.set("BKID123")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Charls Dicken")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("bdt.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("bdt.900")



                
            elif (x=="Python Programming"):
                self.bookid_var.set("BKID124")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("jane austin")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("bdt.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("bdt.1208")



                
            elif (x=="Python CookBook"):
                self.bookid_var.set("BKID125")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("james joyse")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("bdt.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("bdt.1000")



                
            elif (x=="Intro to Machine Learning"):
                self.bookid_var.set("BKID126")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Leo tolstoy")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("bdt.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("bdt.300")



                
            elif (x=="Machine tecno"):
                self.bookid_var.set("BKID127")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Mark Twain")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("bdt.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("bdt.150")



                
            elif (x=="My Python"):
                self.bookid_var.set("BKID128")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("C.S Lewis")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("bdt.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("bdt.277")



                
            elif (x=="Elite Jungle Python"):
                self.bookid_var.set("BKID129")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Roald Dahl")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("bdt.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("bdt.548")



                
            elif (x=="Machine Python"):
                self.bookid_var.set("BKID130")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("John Milton")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("bdt.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("bdt.320")



                
            elif (x=="Head First Book"):
                self.bookid_var.set("BKID131")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Henry j")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("bdt.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("bdt.558")



                

        listBox=Listbox(DataFrameRight,font=("arial",12),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)


        # =========================Buttons Frame==============================
        Framebutton = Frame(self.root, bd=12, relief=RIDGE,
                            padx=20, bg="powder blue")
        Framebutton.place(x=0, y=490, width=1300, height=70)


        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,text="Show Data",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,text="Update",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,text="Delete",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,text="Reset",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,text="Exit",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)


        # =========================Information Frame==============================
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE,padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=560, width=1360, height=150)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0, y=2, width=1300, height=130)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","adress1","address2","postid","mobile","bookid","booktitle","auther","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)



        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("adress1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date of Borrow")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="DaysOnBooks")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")


        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)


        self.library_table.column("prnno",width=100)
        self.library_table.column("membertype",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("adress1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fatch_data()


    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="mdriyadmr968",database="mydata")
        my_cursor=conn.cursor()

        
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.auther_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook.get(),
                                                                                                                self.lateratefine_var.get(),
                                                                                                                self.dateoverdue.get(),
                                                                                                                self.finallprice.get()
                                                                                                                ))
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success","Member Has been inserted successfully")


    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="mdriyadmr968",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()




        



if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()



