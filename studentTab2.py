import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from CustomDateEntry import CustomDateEntry
from student import Student
from user import User
from result import Result

class StudentTab2:
    def __init__(self, Page, user_id, userObject):
        self.main_page = Page       
        self.page = Frame(self.main_page, width=1325, height=680, bg="lightpink")
        self.page.place(x=0,y=0)
        self.user_id = user_id
        self.userObject = userObject
        
        additional_label= Label(self.page, text=" - ")
        additional_label.place(x=1300, y=660)


        # Getting Course
        student_course_object = Student(self.user_id)
        course1 = (student_course_object.getter())[0][8]

        
        conn = sqlite3.connect('collegeEasyApp.db')
        my_cur = conn.cursor()


        my_cur.execute("SELECT * FROM studentTable WHERE course=?",(course1,))
        
        result = my_cur.fetchall()
        conn.commit()
        conn.close()
        resultGetter = Result(userObject.getter())
        result_of_student = resultGetter.getter()


        lookup_label = Label(self.page, text="Name", width=20)
        lookup_label.grid(row=4, column=2, ipadx=10, ipady=5,sticky=W)
        lookup_label = Label(self.page, text=result[0][1])
        lookup_label.grid(row=4, column=3, ipadx=10, ipady=5,sticky=W)




        lookup_label = Label(self.page, text="ID", width=20)
        lookup_label.grid(row=4, column=4, ipadx=10, ipady=5,sticky=W)
        lookup_label = Label(self.page, text=result[0][0], width=20)
        lookup_label.grid(row=4, column=5, ipadx=10, ipady=5,sticky=W)



        lookup_label = Label(self.page, text="Program", width=20)
        lookup_label.grid(row=4, column=6, ipadx=10, ipady=5,sticky=W)
        lookup_label = Label(self.page, text=course1, width=20)
        lookup_label.grid(row=4, column=7, ipadx=10, ipady=5,sticky=W)




        lookup_label = Label(self.page, text="Your Result is : ", width=20, font=("arial",15,"bold"), bg="light green")
        lookup_label.grid(row=6, column=3, columnspan=2, ipadx=5, ipady=20,sticky=W)

        if result_of_student:
                
            lookup_label = Label(self.page, text=result_of_student[0][1], width=20, font=("arial",15,"bold"),fg="red", bg="light green")
            lookup_label.grid(row=6, column=5, ipadx=5, ipady=20,sticky=W)

    
                        