import sqlite3
from tkinter import *
from tkinter import ttk
from CustomDateEntry import CustomDateEntry
from teacher import Teacher
from user import User


class AdminTab3:
    def __init__(self, Page):
        self.page = Page
        
        # Variables

        self.user_id = StringVar()
        self.name = StringVar()
        self.password = StringVar()
        self.gender = StringVar()
        self.date_of_birth = StringVar()
        self.email = StringVar()
        self.address = StringVar()
        self.phone_number = StringVar()
        self.scale = StringVar()
        self.salary = IntVar()
       



        # Page Contents

        self.title_label = Label (self.page, text=" Manage Teacher Record ", font=("times new roman",20,"bold"))
        self.title_label.place(x=0, y=0, width=1325)

        self.left_frame = Frame(self.page, bg="lightgreen")
        self.left_frame.place(x=25, y=50, height=600, width=500)


        # Buttons 

        self.left_frame_bottom = Frame(self.left_frame, bg="light pink")
        self.left_frame_bottom.place(x=25, y=535, width=450, height=45)

        self.save_record_button = Button(self.left_frame_bottom, text="Save", bg="red", fg="white", command=self.save_record)
        self.save_record_button.grid(row=0, column=0, pady=6, padx=6, ipadx=30, ipady=3)

        self.delete_record_button = Button(self.left_frame_bottom, text="Delete", bg="red", fg="white", command=self.delete_record)
        self.delete_record_button.grid(row=0, column=1, pady=6, padx=6, ipadx=27, ipady=3)

        self.update_record_button = Button(self.left_frame_bottom, text="Update", bg="red", fg="white",command=self.update_record)
        self.update_record_button.grid(row=0, column=3, pady=6, padx=6, ipadx=27, ipady=3)

        self.clear_record_button = Button(self.left_frame_bottom, text="Clear", bg="red", fg="white", command=self.clear_entries)
        self.clear_record_button.grid(row=0, column=4, pady=6, padx=6, ipadx=28, ipady=3)



        # Left Frame Contents

        # Labels
        self.enter_record_label = Label(self.left_frame, text="Enter Teacher Record",bg="lightgreen" , font=("arial",18,"bold"), fg="Red")
        self.enter_record_label.grid(row=1, column=0, ipadx=5, ipady=5, pady=10, padx=10, sticky=W)

        self.user_id_label = Label(self.left_frame, text="Teacher ID",bg="lightgreen" , font=("arial",12,"bold"))
        self.user_id_label.grid(row=2, column=0, ipadx=5, ipady=5, pady=5, padx=10, sticky=W)

        self.name_label = Label(self.left_frame, text="Name",bg="lightgreen" , font=("arial",12,"bold"))
        self.name_label.grid(row=3, column=0, ipadx=5, ipady=5, pady=5, padx=10, sticky=W)

        self.password_label = Label(self.left_frame, text="Password",bg="lightgreen" , font=("arial",12,"bold"))
        self.password_label.grid(row=4, column=0, ipadx=5, ipady=5, pady=5, padx=10, sticky=W)

        self.gender_label = Label(self.left_frame, text="Gender",bg="lightgreen" , font=("arial",12,"bold"))
        self.gender_label.grid(row=5, column=0, ipadx=5, ipady=5, pady=5, padx=10, sticky=W)

        self.date_of_birth_label = Label(self.left_frame, text="Date of Birth",bg="lightgreen" , font=("arial",12,"bold"))
        self.date_of_birth_label.grid(row=6, column=0, ipadx=5, ipady=5, pady=5, padx=10, sticky=W)
   
        self.email_label = Label(self.left_frame, text="Email",bg="lightgreen" , font=("arial",12,"bold"))
        self.email_label.grid(row=7, column=0, ipadx=5, ipady=5, pady=5, padx=10, sticky=W)

        self.address_label = Label(self.left_frame, text="Address",bg="lightgreen" , font=("arial",12,"bold"))
        self.address_label.grid(row=8, column=0, ipadx=5, ipady=5, pady=5, padx=10, sticky=W)

        self.phone_number_label = Label(self.left_frame, text="Phone Number",bg="lightgreen" , font=("arial",12,"bold"))
        self.phone_number_label.grid(row=9, column=0, ipadx=5, ipady=5, pady=5, padx=10, sticky=W)

        self.phone_number_label = Label(self.left_frame, text="Course",bg="lightgreen" , font=("arial",12,"bold"))
        self.phone_number_label.grid(row=10, column=0, ipadx=5, ipady=5, pady=5, padx=10, sticky=W)

        self.fee_label = Label(self.left_frame, text="Salary",bg="lightgreen" , font=("arial",12,"bold"))
        self.fee_label.grid(row=11, column=0, ipadx=5, ipady=5, pady=5, padx=10, sticky=W)

        # Entry Boxes

        self.user_id_entry = Entry(self.left_frame, textvariable=self.user_id , font=("arial",12,"bold"))
        self.user_id_entry.grid(row=2, column=1, ipadx=5, ipady=5, pady=5, padx=1, sticky=W)

        self.name_entry = Entry(self.left_frame, textvariable=self.name, font=("arial",12,"bold"))
        self.name_entry.grid(row=3, column=1, ipadx=5, ipady=5, pady=5, padx=1, sticky=W)

        self.password_entry = Entry(self.left_frame, textvariable=self.password, font=("arial",12,"bold"))
        self.password_entry.grid(row=4, column=1, ipadx=5, ipady=5, pady=5, padx=1, sticky=W)

        self.gender_entry = ttk.Combobox(self.left_frame, textvariable=self.gender, font=("arial",12,"bold"),state='readonly', width=18)
        self.gender_entry['values']=('Male','Female')
        self.gender_entry.grid(row=5, column=1, ipadx=5, pady=5, padx=1, sticky=W)

        self.date_of_birth_entry = CustomDateEntry(self.left_frame, textvariable=self.date_of_birth, font=("arial",12,"bold"))
        self.date_of_birth_entry.grid(row=6, column=1, ipadx=5, ipady=5, pady=5, padx=1, sticky=W)

        self.email_entry = Entry(self.left_frame, textvariable=self.email,font=("arial",12,"bold"))
        self.email_entry.grid(row=7, column=1, ipadx=5, ipady=5, pady=5, padx=1, sticky=W)

        self.address_entry = Entry(self.left_frame, textvariable=self.address, font=("arial",12,"bold"))
        self.address_entry.grid(row=8, column=1, ipadx=5, ipady=5, pady=5, padx=1, sticky=W)

        self.phone_number_entry = Entry(self.left_frame, textvariable=self.phone_number, font=("arial",12,"bold"))
        self.phone_number_entry.grid(row=9, column=1, ipadx=5, ipady=5, pady=5, padx=1, sticky=W)

        self.scale_entry = ttk.Combobox(self.left_frame, textvariable=self.scale, font=("arial",12,"bold"),state='readonly', width=18)
        self.scale_entry['values']=('Python','Java','C#','PHP','C++')
        self.scale_entry.grid(row=10, column=1, ipadx=5, pady=5, padx=1, sticky=W)


        self.salary_entry = Entry(self.left_frame, textvariable=self.salary,font=("arial",12,"bold"))
        self.salary_entry.grid(row=11, column=1, ipadx=5, ipady=5, pady=5, padx=1, sticky=W)


        # Right Frame

        self.table_view = Frame(self.page, bg="lightgreen")
        self.table_view.place(x=550, y=50, height=600, width=750)

        self.top_frame_table_view = Frame(self.table_view, bg="light blue")
        self.top_frame_table_view.place(x=0,y=0, width=750, height=50)

        self.search_by_label = Label(self.top_frame_table_view, text="Search By",bg="cyan", font=("arial",13,"bold"))
        self.search_by_label.grid(row=0, column=0, pady=15, padx=5, ipadx=20)

        self.combo_search = ttk.Combobox(self.top_frame_table_view, width=13, font=("arial",13,"bold"), state="readonly")
        self.combo_search['values']=('user_id','name','gender','email','address','phone_number','salary')
        self.combo_search.grid(row=0, column=1, pady=15, padx=5, ipadx=1)

        self.search_by_entry = Entry(self.top_frame_table_view, font=("arial",13,"bold"))
        self.search_by_entry.grid(row=0, column=2, pady=15, padx=5, ipadx=1)

        self.search_by_button = Button(self.top_frame_table_view, text="Search", font=("arial",13,"bold"), command=self.search_data)
        self.search_by_button.grid(row=0, column=3, pady=15, padx=5, ipadx=10)

        self.search_by_all = Button(self.top_frame_table_view, text="Show All", font=("arial",13,"bold"), command=self.fetch_data)
        self.search_by_all.grid(row=0, column=4, pady=15, padx=5, ipadx=10)

        ###### Table Frame

        table_frame = Frame(self.table_view, bd=2, relief=GROOVE, bg="light pink")
        table_frame.place(x=10, y=70, width=720, height=500)
        

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.teacher_table = ttk.Treeview(table_frame, columns=("user_id","name","password","gender","DOB","email","address","phone_number","scale","salary"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.teacher_table.xview)
        scroll_y.config(command=self.teacher_table.yview)

        self.teacher_table['show']='headings'

        self.teacher_table.heading("user_id", text="ID")
        self.teacher_table.heading("name",text="Name")
        self.teacher_table.heading("password", text="Password")
        self.teacher_table.heading("gender", text="Gender")
        self.teacher_table.heading("DOB", text="DOB")
        self.teacher_table.heading("email",text="Email")
        self.teacher_table.heading("address",text="Address")
        self.teacher_table.heading("phone_number",text="Phone No.")
        self.teacher_table.heading("scale",text="Course")
        self.teacher_table.heading("salary",text="salary")

        self.teacher_table.column("user_id", width=50)
        self.teacher_table.column("name",width=75)
        self.teacher_table.column("password", width=75)
        self.teacher_table.column("gender", width=50)
        self.teacher_table.column("DOB", width=75)
        self.teacher_table.column("email",width=75)
        self.teacher_table.column("address",width=75)
        self.teacher_table.column("phone_number",width=75)
        self.teacher_table.column("scale",width=75)
        self.teacher_table.column("salary",width=75)


        self.teacher_table.pack(fill=BOTH, expand=1)
        self.teacher_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def update_record(self):
        teacher_object = Teacher(self.user_id_entry.get(), 
        self.name_entry.get(), 
        self.password_entry.get(), 
        self.gender_entry.get(),
        self.date_of_birth_entry.get(), 
        self.email_entry.get(), 
        self.address_entry.get(), 
        self.phone_number_entry.get(), 
        self.scale_entry.get(),
        self.salary_entry.get())
    
        teacher_object.update()

        self.clear_entries()
        self.fetch_data()
        del teacher_object


    def save_record(self):
        teacher_object = Teacher(self.user_id_entry.get(), 
        self.name_entry.get(), 
        self.password_entry.get(), 
        self.gender_entry.get(),
        self.date_of_birth_entry.get(), 
        self.email_entry.get(), 
        self.address_entry.get(), 
        self.phone_number_entry.get(), 
        self.scale_entry.get(),
        self.salary_entry.get())
    
        teacher_object.setter()

        user_object = User(self.user_id_entry.get(),'teacher')
        user_object.setter()

        self.clear_entries()
        self.fetch_data()
        del teacher_object
        del user_object

    def clear_entries(self):
        self.user_id_entry.delete(0,END)
        self.name_entry.delete(0,END)
        self.password_entry.delete(0,END)
        self.gender_entry.delete(0,END)
        self.date_of_birth_entry.delete(0,END)
        self.email_entry.delete(0,END)
        self.address_entry.delete(0,END)
        self.phone_number_entry.delete(0,END)
        self.scale_entry.delete(0,END)
        self.salary_entry.delete(0,END)

    def fetch_data(self):
    
        conn =sqlite3.connect("collegeEasyApp.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM teacherTable")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.teacher_table.delete(*self.teacher_table.get_children())
            for row in rows:
                self.teacher_table.insert('',END,values=row)
        conn.commit()
        conn.close()


    def get_cursor(self, ev):
        cursor_row = self.teacher_table.focus()
        contents = self.teacher_table.item(cursor_row)
        row = contents['values']
       
        self.clear_entries()

        self.user_id.set(row[0])
        self.name.set(row[1])
        self.password.set(row[2])
        self.gender.set(row[3])
        self.date_of_birth.set(row[4])
        self.email.set(row[5])
        self.address.set(row[6])
        self.phone_number.set(row[7])
        self.scale .set(row[8])
        self.salary.set(row[9])

    def delete_record(self):
        
        teacher_object = Teacher(self.user_id_entry.get())
        teacher_object.remove()

        user_object = User(self.user_id_entry.get())
        user_object.remove()

        del teacher_object
        self.clear_entries()
        self.fetch_data()
    
    def search_data(self):
    
        conn =sqlite3.connect("collegeEasyApp.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM teacherTable WHERE "+str(self.combo_search.get())+" LIKE '%"+str(self.search_by_entry.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.teacher_table.delete(*self.teacher_table.get_children())
            for row in rows:
                self.teacher_table.insert('',END,values=row)
                
        conn.commit()
        conn.close()
