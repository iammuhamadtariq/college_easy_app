from tkinter import *

from datetime import datetime, date, timedelta
import sqlite3
from user import User

class AccountantTab1:
    def __init__(self, Page, user_id):
        self.main_page = Page       
        self.page = Frame(self.main_page, width=1325, height=680, bg="lightgreen")
        self.page.place(x=0,y=0)


        self.user_id = user_id
        
        shared_variable = user_id

        conn =sqlite3.connect("CollegeEasyApp.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM accountantTable WHERE user_id=" + str(shared_variable))

        profileRecord = cur.fetchall()



        profile_name = Label(self.page, text="Your Profile ", bg="lightblue", font=("arial",17,"bold"))
        profile_name.grid(row=6, column=2, columnspan=2, pady=10, ipadx=50, sticky=W)

        profile_name = Label(self.page, text="Your User ID is : ", bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=7, column=2, pady=10, ipadx=10, sticky=W)
        profile_id = Label(self.page, text=shared_variable, bg="lightgreen", font=("arial",12,"bold"))
        profile_id.grid(row=7, column=3, pady=10, ipadx=10, sticky=W)


        profile_name = Label(self.page, text="Your Name is : ", bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=8, column=2, pady=10, ipadx=10, sticky=W)
        profile_name = Label(self.page, text=profileRecord[0][1], bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=8, column=3, pady=10, ipadx=10, sticky=W)



        profile_name = Label(self.page, text="Your Designation : ", bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=9, column=2, pady=10, ipadx=10, sticky=W)
        user_object_type = User(self.user_id)
        designation = user_object_type.getter_user_type()
        profile_name = Label(self.page, text=designation, bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=9, column=3, pady=10, ipadx=10, sticky=W)


        profile_name = Label(self.page, text="Date of Birth is : ", bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=10, column=2, pady=10, ipadx=10, sticky=W)
        profile_name = Label(self.page, text=profileRecord[0][4], bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=10, column=3, pady=10, ipadx=10, sticky=W)





        profile_name = Label(self.page, text="Your Address is : ", bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=11, column=2, pady=10, ipadx=10, sticky=W)
        profile_name = Label(self.page, text=profileRecord[0][7], bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=11, column=3, pady=10, ipadx=10, sticky=W)




        profile_name = Label(self.page, text="Your Email is : ", bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=12, column=2, pady=10, ipadx=10, sticky=W)
        profile_name = Label(self.page, text=profileRecord[0][6], bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=12, column=3, pady=10, ipadx=10, sticky=W)


        profile_name = Label(self.page, text="Your Phone Number : ", bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=13, column=2, pady=10, ipadx=10, sticky=W)
        profile_name = Label(self.page, text=profileRecord[0][7], bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=13, column=3, pady=10, ipadx=10, sticky=W)


        profile_name = Label(self.page, text="Your Scale is :", bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=14, column=2, pady=10, ipadx=10, sticky=W)
        profile_name = Label(self.page, text=profileRecord[0][8], bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=14, column=3, pady=10, ipadx=10, sticky=W)



        profile_name = Label(self.page, text="Your Salary is :", bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=15, column=2, pady=10, ipadx=10, sticky=W)
        profile_name = Label(self.page, text=profileRecord[0][9], bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=15, column=3, pady=10, ipadx=10, sticky=W)




        profile_name = Label(self.page, text="Your Attendance : ", bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=16, column=2, pady=10, ipadx=10, sticky=W)

        total_leave = self.previouseMonthAttendance()
        
        profile_name = Label(self.page, text=str(total_leave), bg="lightgreen", font=("arial",12,"bold"))
        profile_name.grid(row=16, column=3, pady=10, ipadx=10, sticky=W)



        profile_Label = Label(self.page, text=shared_variable, bg="lightgreen", font=("arial",12,"bold"))
        profile_Label.grid(row=7, column=3, pady=10, ipadx=10, sticky=W)


        
    def previouseMonthAttendance(self):

        conn = sqlite3.connect('collegeEasyApp.db')
        my_cursor = conn.cursor()

        last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
        start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)

        last_day = last_day_of_prev_month.strftime('%m/%d/%Y')
        first_day = start_day_of_prev_month.strftime('%m/%d/%Y')
    
        attendance = "P"

        my_cursor.execute("SELECT COUNT(*) FROM attendanceTable WHERE user_id = ? and attendance = ? and date BETWEEN ? and ? ",[self.user_id,attendance,first_day,last_day])
        present = my_cursor.fetchall()

        return present[0][0]
