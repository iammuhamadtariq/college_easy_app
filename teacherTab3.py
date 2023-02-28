import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from CustomDateEntry import CustomDateEntry
from teacher import Teacher
from user import User
from result import Result

class TeacherTab3:
    def __init__(self, Page, user_id, userObject):

        
        self.main_page = Page

        self.page = Frame(self.main_page, width=1325, height=680, bg="lightblue")
        self.page.place(x=0,y=0)


        self.user_id = user_id
        self.userObject = userObject


        additional_label= Label(self.page, text=" - ")
        additional_label.place(x=1300, y=660)

        heading_label_1= Label(self.page, text="User ID", bg="pink")
        heading_label_1.grid(row=4, column=0, ipadx=20)

        heading_label_2= Label(self.page, text="Student Name", bg="pink")
        heading_label_2.grid(row=4, column=1)

        heading_label_3= Label(self.page, text="Result (Pass/Fail)", bg="pink")
        heading_label_3.grid(row=4, column=2)

        
        teacher_course_object = Teacher(self.user_id)
        course1 = (teacher_course_object.getter())[0][8]


        teacher_course_object = Teacher(self.user_id)
        course1 = (teacher_course_object.getter())[0][8]

        conn = sqlite3.connect('collegeEasyApp.db')
        my_cur = conn.cursor()


        my_cur.execute("SELECT * FROM studentTable WHERE course=?",(course1,))
        
        result = my_cur.fetchall()
        conn.commit()
        conn.close()


        def saveAttendance():
            for index, x in enumerate(result):


                conn = sqlite3.connect('collegeEasyApp.db')
                my_cursor = conn.cursor()

                find_attendance = ('SELECT user_id AND result FROM resultTable WHERE user_id=?')
                my_cursor.execute(find_attendance,[(x[0]),])
                student_result_find = my_cursor.fetchall()


                if student_result_find:

                    conn =sqlite3.connect("collegeEasyApp.db")
                    cur2 = conn.cursor()
                    cur2.execute("UPDATE resultTable SET user_id=?, result=? WHERE user_id=?",([x[0],entries[index].get(),x[0]]))
                    conn.commit()
                    conn.close()
                else:
                        conn.commit()
                        conn.close()
                        
                        conn = sqlite3.connect('collegeEasyApp.db')
                        my_cursor = conn.cursor()

                        my_cursor.execute("INSERT INTO resultTable VALUES(?,?)",[x[0],entries[index].get()])
                    
                        conn.commit()
                        conn.close()
            


        entries = []

        for index, x in enumerate(result):
        
            index = index+6
            
            variable = str(x[0])

            lookup_label = Label(self.page, text=x[0])
            lookup_label.grid(row=index, column=0, ipadx=10, ipady=5, sticky=W)
            

            lookup_label = Label(self.page, text=x[1])
            lookup_label.grid(row=index, column=1, ipadx=10, ipady=5,sticky=W)

            mark_box = Entry(self.page, width=10, font=("arial",10,"bold"), justify="center")
            mark_box.grid(row=index, column=2, ipadx=20, ipady=2,sticky=W)
            entries.append(mark_box)
        

        save_attendance = Button (self.page, text="Save Result", bg="red",fg="white", command=saveAttendance)
        save_attendance.grid(row=index+1, column=0, columnspan=3,ipadx=100, pady=100)
