import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from CustomDateEntry import CustomDateEntry
from teacher import Teacher
from user import User


class TeacherTab2:
    def __init__(self, Page, user_id='100'):


        self.page = Page
        self.user_id = user_id

            
        select_date = Label(self.page, text="Select Date of Attendance",font=("Arial",10,"bold"))
        select_date.grid(row=3, column=0, columnspan=2, ipadx=20, ipady=10)


        date_box = CustomDateEntry(self.page, width=20, background='darkblue',foreground='white', borderwidth=2)
        date_box._set_text(date_box._date.strftime('%m/%d/%Y'))
        date_box.grid(row=3, column=2, pady=5, padx=5)

        heading_label_1= Label(self.page, text="User ID", bg="lightblue", font=("arial",12,"bold"))
        heading_label_1.grid(row=4, column=0, ipadx=20)

        heading_label_2= Label(self.page, text="User Name", bg="lightblue", font=("arial",12,"bold"))
        heading_label_2.grid(row=4, column=1)

        heading_label_3= Label(self.page, text="ATTENDENCE", bg="lightblue", font=("arial",12,"bold"))
        heading_label_3.grid(row=4, column=2)

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

                find_attendance = ('SELECT user_id AND date FROM attendanceTable WHERE user_id=? AND date=?')
                my_cursor.execute(find_attendance,[(x[0]),(date_box.get())])
                attendance_result_find = my_cursor.fetchall()


                if attendance_result_find:
                    messagebox.showerror("Eroor","Attendance already marked")
                    break

                else:
                        conn.commit()
                        conn.close()
                        
                        conn = sqlite3.connect('collegeEasyApp.db')
                        my_cursor = conn.cursor()

                        my_cursor.execute("INSERT INTO attendanceTable VALUES(?,?,?)",[x[0],date_box.get(),entries[index].get()])
                    
                        conn.commit()
                        conn.close()
            

            conn = sqlite3.connect('collegeEasyApp.db')
            my_cursor = conn.cursor()

            my_cursor.execute("SELECT COUNT(*) FROM attendanceTable WHERE date=? AND attendance=?",[date_box.get(),"P"])
            present = my_cursor.fetchall()
            present_label = Label(self.page,text=present, bg="lightblue", font=("arial",12,"bold"))
            present_label.grid(row=6, column=4, ipadx=20, ipady=5)

            my_cursor.execute("SELECT COUNT(*) FROM attendanceTable WHERE date=? AND attendance=?",[date_box.get(),"L"])
            present = my_cursor.fetchall()
            present_label = Label(self.page,text=present, bg="lightblue", font=("arial",12,"bold"))
            present_label.grid(row=7, column=4, ipadx=20, ipady=5)

            my_cursor.execute("SELECT COUNT(*) FROM attendanceTable WHERE date=? AND attendance=?",[date_box.get(),"A"])
            present = my_cursor.fetchall()
            present_label = Label(self.page,text=present, bg="lightblue", font=("arial",12,"bold"))
            present_label.grid(row=8, column=4, ipadx=20, ipady=5)

        entries = []
       
        for index, x in enumerate(result):
        
            index = index+6
            
            variable = str(x[0])

            lookup_label = Label(self.page, text=x[0], bg="lightblue", font=("arial",12,"bold"))
            lookup_label.grid(row=index, column=0, ipadx=10, ipady=5, sticky=W)
            

            lookup_label = Label(self.page, text=x[1], bg="lightblue", font=("arial",12,"bold"))
            lookup_label.grid(row=index, column=1, ipadx=10, ipady=5,sticky=W)

            mark_box = Entry(self.page, width=10, font=("arial",10,"bold"), justify="center")
            mark_box.grid(row=index, column=2, ipadx=20, ipady=2,sticky=W)
            entries.append(mark_box)
        
        save_attendance = Button (self.page, text="Save Attendance", command=saveAttendance)
        save_attendance.grid(row=5, column=3, ipadx=0, ipady=5)

        total_present_label = Label(self.page, text="Total Present: ", bg="lightblue", font=("arial",12,"bold"))
        total_present_label.grid(row=6, column=3, ipadx=0, ipady=5)

        total_leave_label = Label(self.page, text="Total Leave: ", bg="lightblue", font=("arial",12,"bold"))
        total_leave_label.grid(row=7, column=3, ipadx=0, ipady=5)

        total_absent_label = Label(self.page, text="Total Leave: ", bg="lightblue", font=("arial",12,"bold"))
        total_absent_label.grid(row=8, column=3, ipadx=0, ipady=5)
