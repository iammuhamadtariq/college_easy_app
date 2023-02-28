import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Admin:
    def __init__(self,root):
        self.root=root
        self.root.title("College Management System")
        self.root.geometry("1350x650+5+5")

        title_label = Label(self.root, text="College Management System", bg="Yellow", fg="Blue", font=("arial",30,"bold"))
        title_label.pack(side=TOP,fill=X)


        self.roll_number = StringVar()
        self.name = StringVar()
        self.email= StringVar()
        self.gender = StringVar()
        
        self.search_by = StringVar()
        self.search_text = StringVar()
        


        ######   MANAGE FRAME

        manage_frame = Frame(self.root, bd=10, relief=RIDGE, bg="light green")
        manage_frame.place(x=20, y=60, height=550, width=550)

        manage_frame_title = Label(manage_frame, text="Manage Student ", bg="light green", fg="white", font=("arial",25,"bold"))
        manage_frame_title.grid(row=0, column=0, columnspan=2, pady=20)

        roll_label = Label(manage_frame, text="Roll Number", bg="light green", fg="blue", font=("arial",15,"bold"))
        roll_label.grid(row=1, column=0, pady=10, padx=20, sticky=W)


        name_label = Label(manage_frame, text="Name", bg="light green", fg="blue", font=("arial",15,"bold"))
        name_label.grid(row=2, column=0, pady=10, padx=20, sticky=W)

        email_label = Label(manage_frame, text="Email", bg="light green", fg="blue", font=("arial",15,"bold"))
        email_label.grid(row=3, column=0, pady=10, padx=20, sticky=W)

        address_label = Label(manage_frame, text="Address", bg="light green", fg="blue", font=("arial",15,"bold"))
        address_label.grid(row=4, column=0, pady=10, padx=20, sticky=W)

        gender_label = Label(manage_frame, text="Gender", bg="light green", fg="blue", font=("arial",15,"bold"))
        gender_label.grid(row=5, column=0, pady=10, padx=20, sticky=W)


        roll_text = Entry(manage_frame, textvariable=self.roll_number, bd=5, font=("times new roman",20,"bold"),relief=GROOVE)
        roll_text.grid(row=1, column=1, padx=10, sticky=W)

        name_text = Entry(manage_frame, textvariable=self.name, bd=5, font=("times new roman",20,"bold"),relief=GROOVE)
        name_text.grid(row=2, column=1, padx=10, sticky=W)


        email_text = Entry(manage_frame,textvariable=self.email, bd=5, font=("times new roman",20,"bold"),relief=GROOVE)
        email_text.grid(row=3, column=1, padx=10, sticky=W)

        self.address_text = Text(manage_frame, width=20, height=2, bd=5, font=("times new roman",20,"bold"),relief=GROOVE)
        self.address_text.grid(row=4, column=1, padx=10, sticky=W)

        combo_gender = ttk.Combobox(manage_frame, textvariable=self.gender, font=("times new roman",20,"bold"), state='readonly')
        combo_gender['values']=('male','female','other')
        combo_gender.grid(row=5, column=1, padx=10, sticky=W)

        button_frame = Frame(manage_frame, height=20, width=550, bg="red")
        button_frame.place(x=25, y=400)

        button_add = Button(button_frame,command=self.add_student, text="ADD")
        button_add.grid(row=0, column=0, padx=10, pady=7, ipadx=30)

        button_add7 = Button(button_frame, text="UPDATE", command=self.update_student)
        button_add7.grid(row=0, column=1, padx=10, pady=7, ipadx=25)

        button_add8 = Button(button_frame, text="DELETE", command=self.delete_student)
        button_add8.grid(row=0, column=2, padx=10, pady=7, ipadx=25)

        button_add9 = Button(button_frame, text="CLEAR", command=self.clear_entries)
        button_add9.grid(row=0, column=3, padx=10, pady=7, ipadx=25)

        ########## DETAIL FRAME


        display_frame = Frame(self.root, bd=10, relief=RIDGE, bg="light green")
        display_frame.place(x=580, y=60, height=550, width=750)

        search_label = Label(display_frame, text="Search By", font=("times new roman",15,"bold"))
        search_label.grid(row=0, column=0,ipady=6, ipadx=50)

        combo_search = ttk.Combobox(display_frame, textvariable=self.search_by, width=13, font=("times new roman",15,"bold"), state='readonly')
        combo_search['values']=('roll_number','name','email')
        combo_search.grid(row=0, column=1, pady=6, padx=10, sticky=W)

        search_text = Entry(display_frame,bd=5, textvariable=self.search_text, width=15, font=("times new roman",15,"bold"),relief=GROOVE)
        search_text.grid(row=0, column=2, pady=2, padx=10, sticky=W)

        search_button = Button(display_frame, text="Search", command=self.search_data)
        search_button.grid(row=0, column=3, pady=6, padx=2, ipadx=15)

        all_button = Button(display_frame, text="Show All", command=self.fetch_data)
        all_button.grid(row=0, column=4, pady=6, padx=2, ipadx=10)

        ###### table frame 

        table_frame = Frame(display_frame, bd=2, relief=GROOVE, bg="light pink")
        table_frame.place(x=10, y=70, width=700, height=400)
        

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=("Roll","Name","Email","Address","Gender"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table['show']='headings'

        self.student_table.heading("Roll", text="Roll Number")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Gender",text="Gender")

        self.student_table.column("Roll", width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Gender",width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_student(self):
        
        if self.roll_number.get()=="" or self.name.get()=="" or self.gender.get()=="" or self.email.get()=="":
            messagebox.showerror("Error","All fields are required")
    
        else:

            conn =sqlite3.connect("mydatabase.db")
            cur = conn.cursor()
        
            cur.execute("INSERT INTO studentTable VALUES(?,?,?,?,?)",(
                                                                        self.roll_number.get(),
                                                                        self.name.get(),
                                                                        self.email.get(),
                                                                        self.gender.get(),
                                                                        self.address_text.get('1.0',END)
            ))

            conn.commit()
            conn.close()
            self.fetch_data()
            self.clear_entries()

    def clear_entries(self):
        self.roll_number.set("")
        self.name.set("")
        self.email.set("")
        self.gender.set("")
        self.address_text.delete("1.0",END)



    def fetch_data(self):

        conn =sqlite3.connect("mydatabase.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM studentTable")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
        conn.commit()
        conn.close()
    
    def get_cursor(self, ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
       
        self.clear_entries()
        self.roll_number.set(row[0])
        self.name.set(row[1])
        self.email.set(row[2])
        self.gender.set(row[3])
        self.address_text.insert("1.0",row[4])

    def update_student(self):


        conn =sqlite3.connect("mydatabase.db")
        cur2 = conn.cursor()
        cur2.execute("UPDATE studentTable SET roll_number=?, name=?, email=?, gender=?, address=? WHERE roll_number=?",(
                                                                    self.roll_number.get(),
                                                                    self.name.get(),
                                                                    self.email.get(),
                                                                    self.gender.get(),
                                                                    self.address_text.get('1.0',END),
                                                                    self.roll_number.get()
        ))

        conn.commit()
        self.clear_entries()
        self.fetch_data()
        conn.close()
    
    def delete_student(self):
        
        conn =sqlite3.connect("mydatabase.db")
        cur2 = conn.cursor()
        cur2.execute("DELETE from studentTable WHERE roll_number=?",(
                                                                    self.roll_number.get(),
        ))

        conn.commit()
        self.clear_entries()
        self.fetch_data()
        conn.close()

    def search_data(self):
    
        conn =sqlite3.connect("mydatabase.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM studentTable WHERE "+str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
        conn.commit()
        conn.close()

root = Tk()
obj = Admin(root)
root.mainloop()
