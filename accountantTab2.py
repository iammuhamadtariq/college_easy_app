from tkinter import *
from tkinter import ttk
from datetime import datetime, date, timedelta
import sqlite3
from user import User
from admin import Admin
from teacher import Teacher
from accountant import Accountant


class AccountantTab2:
    def __init__(self, Page, user_id):
        self.main_page = Page       
        self.page = Frame(self.main_page, width=1325, height=680, bg="lightgreen")
        self.page.place(x=0,y=0)


        self.user_id = user_id

        
        ###### Table Frame
        
        self.table_view = Frame(self.page, bg="lightgreen")
        self.table_view.place(x=10, y=20, height=500, width=1300)

        table_frame = Frame(self.table_view, bd=2, relief=GROOVE, bg="light pink")
        table_frame.place(x=10, y=70, width=1200, height=500)
        

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.teacher_table = ttk.Treeview(table_frame, columns=("user_id","name","password","gender","DOB","email","address","phone_number","scale","salary","total_leave","this_salary"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

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
        self.teacher_table.heading("scale",text="scale")
        self.teacher_table.heading("salary",text="salary")
        self.teacher_table.heading("total_leave",text="Total Leave")
        self.teacher_table.heading("this_salary",text="This Month Salary")

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
        self.teacher_table.column("total_leave",width=75)
        self.teacher_table.column("this_salary",width=75)


        self.teacher_table.pack(fill=BOTH, expand=1)
        self.fetch_data()



    def fetch_data(self):
    
        conn =sqlite3.connect("collegeEasyApp.db")
        cur2 = conn.cursor()

        cur2.execute("SELECT * from adminTable UNION ALL SELECT * from teacherTable UNION ALL SELECT * from accountantTable")
        rows = cur2.fetchall()
        conn.commit()
        conn.close()

        ## Adding Leave in Previouse Month and Salary

        rows_with_salary =[]

        for row in rows:
                    
            user_leave = self.previouseMonthLeave(row[0])
            
            this_month_salary = (float(user_leave)) * (float(row[9])) * 12 / 365

            my_list = list(row)
            my_list.append(user_leave)
            my_list.append(int(this_month_salary))

            row = tuple(my_list)
            rows_with_salary.append(row)




        if len(rows_with_salary)!=0:
            self.teacher_table.delete(*self.teacher_table.get_children())
            for row in rows_with_salary:
                self.teacher_table.insert('',END,values=row)

                    
                # getting leave of Employees 
                conn = sqlite3.connect('collegeEasyApp.db')
                my_cursor = conn.cursor()


                my_cursor.execute("SELECT COUNT(*) FROM attendanceTable WHERE date=? AND attendance=?",[row[0],"P"])
                self.teacher_table.item('')





        conn.commit()
        conn.close()

    def previouseMonthLeave(self, id):

        conn = sqlite3.connect('collegeEasyApp.db')
        my_cursor = conn.cursor()

        last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
        start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)

        last_day = last_day_of_prev_month.strftime('%m/%d/%Y')
        first_day = start_day_of_prev_month.strftime('%m/%d/%Y')
    
        attendance = "P"
        
        my_cursor.execute("SELECT COUNT(*) FROM attendanceTable WHERE user_id = ? and attendance = ? and date BETWEEN ? and ? ",[id,attendance,first_day,last_day])
        present = my_cursor.fetchall()
        
        return present[0][0]

        conn.commit()
        conn.close()
