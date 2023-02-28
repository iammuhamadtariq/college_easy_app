import tkinter as tk                
from tkinter import ttk
from tkinter import font  as tkfont 
from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import datetime 
from datetime import date
from tkcalendar import DateEntry
from CustomDateEntry import CustomDateEntry
from course import Course
from user import user
from employee import Employee
from salary import Salary
from userType import userType
from studentResultPage import StudentResultPage
from studentDisplayRecordPage import StudentDisplayResultPage
from studentProfilePage import StudentProfilePage
from studentResultStudentPage import StudentResultStudentPage
from accountantProfile import AccountantProfilePage
from accountantSalaryPage import AccountantSalaryPage
from AttendanceP import previouseMonthAttendance
from adminDisplayRecord import DisplayAllRecordClass




global userObject

userObject = user("","")

root = Tk()
root.title("Programmar Computer College")
root.geometry("1300x650+10+10")

def loginFunction():
    
    # Create objects of classes 
    global userObject
    courseObject = Course(user_id_entry.get())
    userObject.changeUserRecord(user_id_entry.get(),user_password_entry.get())

    if user_id_entry.get()=="" or user_password_entry.get()=="":
        messagebox.showerror("Error","All fields are required")
    elif (user_id_entry.get()!="" and user_password_entry.get()!=""):

        result = userObject.checkUser()

        if result:

            role_type = userObject.getRole()
            if role_type == "Teacher":
                teacherPage()

            elif role_type == "Accountant":
                accountantPage()

            elif role_type == "Admin":
                adminPage()

            elif role_type == "Student":
                studentPage()
            else:
                messagebox.showinfo("Student Type","You are Student")
        else:
            messagebox.showerror("Error","Invalid Username or Password")
    
 ####################################################################################################### 


def hideFrames():
    admin_frame.grid_forget()
    login_frame.grid_forget()
    teacher_frame.grid_forget()
    student_frame.grid_forget()
    accountant_frame.grid_forget()
    

def adminPage():
    hideFrames()
    admin_frame.grid(row=0, column=0)
    displayProfileFunction()
    RegisterEmployeeIntoSystem()


def studentPage():
    hideFrames()
    student_frame.grid(row=0, column=0)
    studentProfilePage()
    studentResultStudentPage()


def accountantPage():
    hideFrames()
    accountant_frame.grid(row=0, column=0, ipadx=600, ipady=500)
    accountantProfilePage()
    accountantSalaryPage()

def teacherPage():
    hideFrames()
    teacher_frame.grid(row=0, column=0)
    profileTeacherDisplay()
    studentAttendance()
    studentResultPage()
    studentRecrodPage()

    
def userLogOut():
    hideFrames()
    login_frame.grid(row=0,column=0)



# Creating Main Login Page ####################################################
login_frame = Frame(root, width=1300, height=625)
login_frame.grid(row=0, column=0)
user_id_label = Label(login_frame, text="LOGIN PAGE",  font=("comic sans roman",15,"bold"))
user_id_label.grid(row=5, column=0, columnspan=4, ipady=50, ipadx=50)
user_id_label = Label(login_frame, text="Enter Your ID ", bg="light blue",font=("arial",10,"bold"))
user_id_label.grid(row=6, column=1, ipadx=74)
user_password_label = Label(login_frame, text="Enter Your Password ", bg="light blue",font=("arial",10,"bold"))
user_password_label.grid(row=7, column=1, ipadx=50)
user_id_entry = Entry(login_frame)
user_id_entry.grid(row=6, column=2, ipadx=50, ipady=2, padx=10)
user_password_entry = Entry(login_frame)
user_password_entry.grid(row=7, column=2, ipadx=50, ipady=2, padx=10)
login_button = Button(login_frame, command=loginFunction, text="Login", bg="red", fg="white", font=("arial",10,"bold"))
login_button.grid(row=8, column=2, padx=10, pady=30, ipadx=50, sticky=E)




def employeeAttendance():
    
    select_date = Label(admin_attendance_of_employe, text="Select Date of Attendance",font=("Arial",10,"bold"))
    select_date.grid(row=3, column=0, columnspan=2, ipadx=20, ipady=10)


    date_box = CustomDateEntry(admin_attendance_of_employe, width=20, background='darkblue',foreground='white', borderwidth=2)
    date_box._set_text(date_box._date.strftime('%m/%d/%Y'))
    date_box.grid(row=3, column=2, pady=5, padx=5)

    heading_label_1= Label(admin_attendance_of_employe, text="User ID", bg="pink")
    heading_label_1.grid(row=4, column=0, ipadx=20)

    heading_label_2= Label(admin_attendance_of_employe, text="User Name", bg="pink")
    heading_label_2.grid(row=4, column=1)

    heading_label_3= Label(admin_attendance_of_employe, text="ATTENDENCE", bg="pink")
    heading_label_3.grid(row=4, column=2)



    conn = sqlite3.connect('collegeEasyApp.db')
    my_cur = conn.cursor()


    userRole="Student"
    sql = ("SELECT * FROM userTable WHERE role = 'Teacher' or role = 'Admin' or role = 'Accountant'")
    my_cur.execute(sql)
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
        present_label = Label(admin_attendance_of_employe,text=present)
        present_label.grid(row=6, column=4, ipadx=20, ipady=5)

        my_cursor.execute("SELECT COUNT(*) FROM attendanceTable WHERE date=? AND attendance=?",[date_box.get(),"L"])
        present = my_cursor.fetchall()
        present_label = Label(admin_attendance_of_employe,text=present)
        present_label.grid(row=7, column=4, ipadx=20, ipady=5)

        my_cursor.execute("SELECT COUNT(*) FROM attendanceTable WHERE date=? AND attendance=?",[date_box.get(),"A"])
        present = my_cursor.fetchall()
        present_label = Label(admin_attendance_of_employe,text=present)
        present_label.grid(row=8, column=4, ipadx=20, ipady=5)

    entries = []

    for index, x in enumerate(result):
    
        index = index+6
        
        variable = str(x[0])

        lookup_label = Label(admin_attendance_of_employe, text=x[0])
        lookup_label.grid(row=index, column=0, ipadx=10, ipady=5, sticky=W)
        

        lookup_label = Label(admin_attendance_of_employe, text=x[1])
        lookup_label.grid(row=index, column=1, ipadx=10, ipady=5,sticky=W)

        mark_box = Entry(admin_attendance_of_employe, width=10, font=("arial",10,"bold"), justify="center")
        mark_box.grid(row=index, column=2, ipadx=20, ipady=2,sticky=W)
        entries.append(mark_box)
    
    save_attendance = Button (admin_attendance_of_employe, text="Save Attendance", command=saveAttendance)
    save_attendance.grid(row=5, column=3, ipadx=0, ipady=5)

    total_present_label = Label(admin_attendance_of_employe, text="Total Present: ")
    total_present_label.grid(row=6, column=3, ipadx=0, ipady=5)

    total_leave_label = Label(admin_attendance_of_employe, text="Total Leave: ")
    total_leave_label.grid(row=7, column=3, ipadx=0, ipady=5)

    total_absent_label = Label(admin_attendance_of_employe, text="Total Leave: ")
    total_absent_label.grid(row=8, column=3, ipadx=0, ipady=5)



# Creating Admin Frame ##########################################################


def displayProfileFunction():
        
    shared_variable = userObject.getUserID()
    profileRecord = userObject.getAllRecord()



    profile_name = tk.Label(admin_frame_display_profile, text="Your Profile ", font=("arial",15,"bold"))
    profile_name.grid(row=6, column=2, columnspan=2, pady=10, ipadx=10)

    profile_name = tk.Label(admin_frame_display_profile, text="Your User ID is : ")
    profile_name.grid(row=7, column=2, pady=10, ipadx=10, sticky=W)
    profile_id = tk.Label(admin_frame_display_profile, text=shared_variable)
    profile_id.grid(row=7, column=3, pady=10, ipadx=10)


    profile_name = tk.Label(admin_frame_display_profile, text="Your Name is : ")
    profile_name.grid(row=8, column=2, pady=10, ipadx=10, sticky=W)
    profile_name = tk.Label(admin_frame_display_profile, text="Your Designation : ")
    profile_name.grid(row=9, column=2, pady=10, ipadx=10, sticky=W)
    profile_name = tk.Label(admin_frame_display_profile, text="Date of Birth is : ")
    profile_name.grid(row=10, column=2, pady=10, ipadx=10, sticky=W)
    profile_name = tk.Label(admin_frame_display_profile, text="Your Address is : ")
    profile_name.grid(row=11, column=2, pady=10, ipadx=10, sticky=W)
    profile_name = tk.Label(admin_frame_display_profile, text="Your Email is : ")
    profile_name.grid(row=12, column=2, pady=10, ipadx=10, sticky=W)
    profile_name = tk.Label(admin_frame_display_profile, text="Your Attendance : ")
    profile_name.grid(row=13, column=2, pady=10, ipadx=10, sticky=W)



    profile_name = tk.Label(admin_frame_display_profile, text=profileRecord[0][1])
    profile_name.grid(row=8, column=3, pady=10, ipadx=10)
    profile_name = tk.Label(admin_frame_display_profile, text=profileRecord[0][3])
    profile_name.grid(row=9, column=3, pady=10, ipadx=10)
    profile_name = tk.Label(admin_frame_display_profile, text=profileRecord[0][4])
    profile_name.grid(row=10, column=3, pady=10, ipadx=10)
    profile_name = tk.Label(admin_frame_display_profile, text=profileRecord[0][5])
    profile_name.grid(row=11, column=3, pady=10, ipadx=10)
    profile_name = tk.Label(admin_frame_display_profile, text=profileRecord[0][6])
    profile_name.grid(row=12, column=3, pady=10, ipadx=10)



    total_leave = previouseMonthAttendance(shared_variable)


    profile_name = tk.Label(admin_frame_display_profile, text=str(total_leave), bg="light blue", bd=5)
    profile_name.grid(row=13, column=3, pady=10, ipadx=10)

    empty_label = Label(admin_frame_display_profile, text=" Label ")
    empty_label.grid(row=13, column=6, pady=500, padx=1000)

    profile_Label = tk.Label(admin_frame_display_profile, text=shared_variable, bg="light blue")
    profile_Label.grid(row=7, column=3, pady=10, ipadx=10)

### ADMIN PAGE ###################################################




admin_frame = Frame(root, width=1250, height=600, bg="red")




# Create Notebook
admin_notebook = ttk.Notebook(admin_frame)

admin_frame_display_profile = Frame(admin_notebook, width=1200, height=600)
admin_frame_register_employee = Frame(admin_notebook, width=1200, height=600)
admin_frame_register_student = Frame(admin_notebook, width=1200, height=600)
admin_attendance_of_employe = Frame(admin_notebook, width=1200, height=600)
admin_display_all_record = Frame(admin_notebook, width=1200, height=600)


admin_notebook.add(admin_frame_display_profile, text="Admin Profile")
admin_notebook.add(admin_frame_register_employee, text="Register Employee")
admin_notebook.add(admin_frame_register_student, text="Register Student")
admin_notebook.add(admin_attendance_of_employe, text="Attendance of Employee")
admin_notebook.add(admin_display_all_record, text="Display All Records")


Obj8 = DisplayAllRecordClass(admin_display_all_record)

logout_button_admin_frame = Button(admin_frame,command=userLogOut, text="Logout", bg="red", fg="white")
logout_button_admin_frame.place(x=1100, y=20, width=75)

employeeAttendance()









# Employe Registeration Page ##############################################

def RegisterEmployeeIntoSystem():
 
    def EMPdeleteRecord():
        
        userObjectToDelete = user(userObject.getUserID())
        userObjectToDelete.deleteUser()

        salaryObjectToDelete = salary(userObject.getUserID)
        salaryObjectToDelete.deleteUser()

        courseObjectToDelete = Course(userObject.getUserID)
        courseObjectToDelete.deleteCourse()

        EMP_select_id_text_box.delete(0, END)
        

        # clrear text boxes 

        EMP_student_id_box.delete(0,END)
        EMP_student_name_box.delete(0,END)
        EMP_password_box.delete(0,END)
        EMP_dob_box.delete(0,END)
        EMP_address_box.delete(0,END)
        EMP_email_box.delete(0,END)
        EMP_salary_box.delete(0,END)
        EMP_course_box.delete(0,END)

        del userObjectToDelete
        del salaryObjectToDelet
        del courseObjectToDelete
        
    global EMP_student_id_box
    global EMP_student_name_box
    global EMP_password_box
    global EMP_rold_id_box
    global EMP_dob_box
    global EMP_address_box
    global EMP_email_box
    global EMP_salary_box
    global EMP_course_box
    global EMP_select_id_text_box
    global EMP_designation_box


    def EMPSearchRecord():

       
        record_id = EMP_select_id_text_box.get()
        
        userObjectToSearch = user(record_id)
        user_records = userObjectToSearch.getAllRecord()

        salaryObjectToSearch = Salary(record_id)
        salary_records = salaryObjectToSearch.getAllRecord()

        courseObjectToSearch = Course(record_id)
        course_records = courseObjectToSearch.courseGetter()

        employeeObjectToSearch = Employee(record_id)
        employee_records = employeeObjectToSearch.getter()

        # clrear text boxes 
        EMP_designation_box.delete(0,END)
        EMP_student_id_box.delete(0,END)
        EMP_student_name_box.delete(0,END)
        EMP_password_box.delete(0,END)
        EMP_dob_box.delete(0,END)
        EMP_address_box.delete(0,END)
        EMP_email_box.delete(0,END)
        EMP_salary_box.delete(0,END)
        EMP_course_box.delete(0,END)

        for record in user_records:
            EMP_student_id_box.insert(0, record[0])
            EMP_student_name_box.insert(0, record[1])
            EMP_password_box.insert(0, record[2])
            EMP_dob_box.insert(0, record[4])
            EMP_address_box.insert(0, record[5])
            EMP_email_box.insert(0, record[6])

        for record in salary_records:
            EMP_salary_box.insert(0, record[1])

        for record in course_records:
            EMP_course_box.insert(0, record[1])

        for record in employee_records:
            EMP_designation_box.insert(0, record[1])

        del userObjectToSearch    
        del salaryObjectToSearch  
        del courseObjectToSearch     
        del employeeObjectToSearch

    def EMPinsert():

        #Checking User Exists or not

        userObjectExist = user(EMP_student_id_box.get())
        resultFind = userObjectExist.checkUserID()
        del userObjectExist

        if any ([len(EMP_student_id_box.get())==0,len(EMP_student_name_box.get())==0,
        len(EMP_password_box.get())==0,len(EMP_dob_box.get())==0,
        len(EMP_address_box.get())==0,len(EMP_email_box.get())==0,
        len(EMP_designation_box.get())==0,len(EMP_salary_box.get())==0]):
            messagebox.showerror("Error","All fields are required !! ")
                
        elif resultFind:
            messagebox.showinfo("Error in Inserting","User ID Already Exits !!! ")
        elif (len(EMP_student_id_box.get())!=5):
            messagebox.showerror("Error","Enter 5 Digit Number Without Dashes")
        elif not (EMP_student_id_box.get()).isdigit():
            messagebox.showerror("Error","For User ID Only Numeric Value You can Enter")
        elif not EMP_dob_box.get().split('/'):
            messagebox.showerror("Error","Date Format is Not Valid")

        
        else:
            #Inserting Records

        
            record_id = EMP_select_id_text_box.get()
            
            userObjectToInsert = user(EMP_student_id_box.get(),EMP_student_name_box.get(),EMP_password_box.get(),EMP_designation_box.get(),EMP_dob_box.get(),EMP_address_box.get(),EMP_email_box.get())
            user_records = userObjectToInsert.setter()

            salaryObjectToInsert = Salary(EMP_student_id_box.get(),EMP_salary_box.get())
            salary_records = salaryObjectToInsert.setter()

            courseObjectToInsert = Course(EMP_student_id_box.get(),EMP_course_box.get())
            course_records = courseObjectToInsert.setter()

            employeeObjectToInsert = Employee(EMP_student_id_box.get(),EMP_designation_box.get())
            employee_records = employeeObjectToInsert.setter()

            del userObjectToInsert
            del salaryObjectToInsert
            del courseObjectToInsert
            del employeeObjectToInsert

            # clrear text boxes 

            EMP_student_id_box.delete(0,END)
            EMP_student_name_box.delete(0,END)
            EMP_password_box.delete(0,END)
            EMP_dob_box.delete(0,END)
            EMP_address_box.delete(0,END)
            EMP_email_box.delete(0,END)
            EMP_designation_box.delete(0,END)
            EMP_salary_box.delete(0,END)
            EMP_course_box.delete(0,END)


    def EMPupdateRecord():
        
        conn = sqlite3.connect('collegeEasyApp.db')
        curser = conn.cursor()

        #Error Checking
        find_student = ('SELECT user_id FROM userTable WHERE user_id = ?')
        curser.execute(find_student,[(EMP_student_id_box.get())])
        resultFind = curser.fetchall()


        if any ([len(EMP_student_id_box.get())==0,len(EMP_student_name_box.get())==0,
        len(EMP_password_box.get())==0,len(EMP_dob_box.get())==0,
        len(EMP_address_box.get())==0,len(EMP_email_box.get())==0,
        len(EMP_course_box.get())==0,len(EMP_salary_box.get())==0]):
            messagebox.showerror("Error","All fields are required !! ")

        elif (len(EMP_student_id_box.get())!=5):
            messagebox.showerror("Error","User ID is not correct! Enter 5 Digit Number Without Dashes")
        elif not (EMP_student_id_box.get()).isdigit():
            messagebox.showerror("Error","For NIC Only Numeric Value You can Enter")

        
        else:
            
            recordID = EMP_select_id_text_box.get()
            #Inserting Records
            curser.execute(""" UPDATE userTable SET 
                user_id = :student_id,
                name = :name,
                password = :password, 
                role = :role, 
                date_of_birth = :date_of_birth, 
                address = :address, 
                email = :email

                WHERE user_id = :oid""",

                    {
                    'student_id': EMP_student_id_box.get(),
                    'name': EMP_student_name_box.get(),
                    'password': EMP_password_box.get(),
                    'role': EMP_designation_box.get(),
                    'date_of_birth': EMP_dob_box.get(),
                    'address': EMP_address_box.get(),
                    'email': EMP_email_box.get(),
                    'oid': EMP_select_id_text_box.get()
                    })
                    
            curser.execute(""" UPDATE courseTable SET 

                    course_name = :course

                    WHERE user_id= :uoid""",
                    {
                
                    'course': EMP_course_box.get(),
                    'uoid': EMP_select_id_text_box.get()

                    })

            curser.execute(""" UPDATE salaryTable SET 

                    salary = :salary

                    WHERE user_id= :uuoid""",
                    {
                
                    'salary': EMP_salary_box.get(),
                    'uuoid': EMP_select_id_text_box.get()

                    })
            curser.execute(""" UPDATE EmployeeTable SET 

                    EmpDesignation = :EmpDesignation

                    WHERE EmployeeID= :uuoid""",
                    {
                
                    'EmpDesignation': EMP_designation_box.get(),
                    'uuoid': EMP_select_id_text_box.get()

                    })



            # clrear text boxes 

            EMP_student_id_box.delete(0,END)
            EMP_student_name_box.delete(0,END)
            EMP_password_box.delete(0,END)
            EMP_dob_box.delete(0,END)
            EMP_address_box.delete(0,END)
            EMP_email_box.delete(0,END)
            EMP_salary_box.delete(0,END)
            EMP_course_box.delete(0,END)
            EMP_designation_box.delete(0,END)

        conn.commit()
        conn.close()




    #=============== EMPLOYEE MANAGEMENT PANEL ================

    registerationTitle = tk.Label(admin_frame_register_employee,text="MANAGE EMPLOYEE",bg="GRAY", fg="blue",
    font=("times new roman",20,"bold"))
    registerationTitle.grid(row=31, column=0, pady=5, padx=5, columnspan=3, sticky=W)

    # Labels

    student_name = tk.Label(admin_frame_register_employee, text="Employee Name")
    student_name.grid(row=32, column=0, pady=5, padx=5, sticky=W)

    student_id = tk.Label(admin_frame_register_employee, text="Employe ID")
    student_id.grid(row=33, column=0, pady=5, padx=5, sticky=W)

    password = tk.Label(admin_frame_register_employee, text="Employee Password")
    password.grid(row=34, column=0, pady=5, padx=5, sticky=W)

    dob= tk.Label(admin_frame_register_employee, text="Date of Birth")
    dob.grid(row=36, column=0, pady=5, padx=5, sticky=W)

    address = tk.Label(admin_frame_register_employee, text="Address")
    address.grid(row=37, column=0, pady=5, padx=5, sticky=W)

    email = tk.Label(admin_frame_register_employee, text="Email ")
    email.grid(row=38, column=0, pady=5, padx=5, sticky=W)

    salary = tk.Label(admin_frame_register_employee, text="Salary ")
    salary.grid(row=39, column=0, pady=5, padx=5, sticky=W)

    designation = tk.Label(admin_frame_register_employee, text="Designation ")
    designation.grid(row=40, column=0, pady=5, padx=5, sticky=W)

    course = tk.Label(admin_frame_register_employee, text="Course ")
    course.grid(row=41, column=0, pady=5, padx=5, sticky=W)



    # Enter Boxes

    EMP_student_name_box = tk.Entry(admin_frame_register_employee, width=30)
    EMP_student_name_box.grid(row=32, column=1, pady=5, padx=5, sticky=W)

    EMP_student_id_box = tk.Entry(admin_frame_register_employee, width=30)
    EMP_student_id_box.grid(row=33, column=1, pady=5, padx=5, sticky=W)

    EMP_password_box = tk.Entry(admin_frame_register_employee, width=30)
    EMP_password_box.grid(row=34, column=1, pady=5, padx=5, sticky=W)

    EMP_dob_box = DateEntry(admin_frame_register_employee, width=20, background='darkblue',foreground='white', borderwidth=2)
    EMP_dob_box.grid(row=36, column=1, pady=5, padx=5)

    EMP_address_box = tk.Entry(admin_frame_register_employee, width=30)
    EMP_address_box.grid(row=37, column=1, pady=5, padx=5, sticky=W)

    EMP_email_box = tk.Entry(admin_frame_register_employee, width=30)
    EMP_email_box.grid(row=38, column=1, pady=5, padx=5, sticky=W)

    EMP_salary_box = tk.Entry(admin_frame_register_employee, width=30)
    EMP_salary_box.grid(row=39, column=1, pady=5, padx=5, sticky=W)

    EMP_designation_box = tk.Entry(admin_frame_register_employee, width=30)
    EMP_designation_box.grid(row=40, column=1, pady=5, padx=5, sticky=W)

    EMP_course_box = tk.Entry(admin_frame_register_employee, width=30)
    EMP_course_box.grid(row=41, column=1, pady=5, padx=5, sticky=W)

    insert_button = tk.Button (admin_frame_register_employee, text="Register Employee Data", command=EMPinsert,
    bg="pink",font=("times new roman",13,"bold"))
    insert_button.grid(row=50,column=0, columnspan=2, pady=5, padx=5, ipadx=60)








    # select update delete display record functions ===================

    heading = Label(admin_frame_register_employee, text="Search, Update, Delete Operations", fg="Red", bg="Yellow")
    heading.grid(row=32, column=2, pady=5, padx=5, sticky=W)

    student_select_id = Label(admin_frame_register_employee, text="Enter ID For Operation")
    student_select_id.grid(row=33, column=2, pady=5, padx=5, sticky=W)

    EMP_select_id_text_box = Entry(admin_frame_register_employee, width=30)
    EMP_select_id_text_box.grid(row=34, column=2, pady=5, padx=5, sticky=W)



    student_update_button = Button (admin_frame_register_employee, text="Update", command=EMPupdateRecord)
    student_update_button.grid(row=36,column=2, columnspan=1, pady=5, padx=5, ipadx=100)

    student_search_button = Button (admin_frame_register_employee, text="Search",command=EMPSearchRecord)
    student_search_button.grid(row=37,column=2, columnspan=1, pady=5, padx=5, ipadx=100)

    student_delete_button = Button (admin_frame_register_employee, text="Delete",command=EMPdeleteRecord)
    student_delete_button.grid(row=38, column=2, columnspan=1, pady=5, padx=5, ipadx=100)

# EMPLOYEE REGISTERATION FORM ENDSSSS  ########################################


# STUDENT REGISTERATIN FORM START  ########################################
# ===================== Delete Record Function ==============   
def deleteRecord():
    
    conn = sqlite3.connect('collegeEasyApp.db')
    curser = conn.cursor()
    
    curser.execute("DELETE FROM userTable WHERE user_id= " + ST_select_id_text_box.get())
    curser.execute("DELETE FROM feeTable WHERE user_id= " + ST_select_id_text_box.get())
    curser.execute("DELETE FROM courseTable WHERE user_id= " + ST_select_id_text_box.get())
    
    ST_select_id_text_box.delete(0, END)
    

    # clrear text boxes 

    ST_student_id_box.delete(0,END)
    ST_student_name_box.delete(0,END)
    ST_password_box.delete(0,END)
    ST_dob_box.delete(0,END)
    ST_address_box.delete(0,END)
    ST_email_box.delete(0,END)
    ST_fee_box.delete(0,END)
    ST_course_box.delete(0,END)
    
    conn.commit()
    conn.close()



#====== STUDENT REGISTRATION FUNCTION =======================================================

global ST_student_id_box
global ST_student_name_box
global ST_password_box
global ST_rold_id_box
global ST_dob_box
global ST_address_box
global ST_email_box
global ST_fee_box
global ST_course_box
global ST_select_id_text_box


def SearchRecord():

    conn = sqlite3.connect('collegeEasyApp.db')
    curser = conn.cursor()
    
    record_id = ST_select_id_text_box.get()
    
    curser.execute("SELECT * FROM userTable WHERE user_id=" + record_id)
    user_records = curser.fetchall()
    curser.execute("SELECT * FROM feeTable WHERE user_id=" + record_id)
    fee_records = curser.fetchall()
    curser.execute("SELECT * FROM courseTable WHERE user_id=" + record_id)
    course_records = curser.fetchall()

    # clrear text boxes 

    ST_student_id_box.delete(0,END)
    ST_student_name_box.delete(0,END)
    ST_password_box.delete(0,END)
    ST_dob_box.delete(0,END)
    ST_address_box.delete(0,END)
    ST_email_box.delete(0,END)
    ST_fee_box.delete(0,END)
    ST_course_box.delete(0,END)

    for record in user_records:
        ST_student_id_box.insert(0, record[0])
        ST_student_name_box.insert(0, record[1])
        ST_password_box.insert(0, record[2])
        ST_dob_box.insert(0, record[4])
        ST_address_box.insert(0, record[5])
        ST_email_box.insert(0, record[6])

    for record in fee_records:
        ST_fee_box.insert(0, record[1])

    for record in course_records:
        ST_course_box.insert(0, record[1])



    conn.commit()
    conn.close()


def insert():
    
    conn = sqlite3.connect('collegeEasyApp.db')
    curser = conn.cursor()

    #Error Checking
    find_student = ('SELECT user_id FROM userTable WHERE user_id = ?')
    curser.execute(find_student,[(ST_student_id_box.get())])
    resultFind = curser.fetchall()


    if any ([len(ST_student_id_box.get())==0,len(ST_student_name_box.get())==0,
    len(ST_password_box.get())==0,len(ST_dob_box.get())==0,
    len(ST_address_box.get())==0,len(ST_email_box.get())==0,
    len(ST_course_box.get())==0,len(ST_fee_box.get())==0]):
        messagebox.showerror("Error","All fields are required !! ")
            
    elif resultFind:
        messagebox.showinfo("Error in Inserting","User ID Already Exits !!! ")
    elif (len(ST_student_id_box.get())!=5):
        messagebox.showerror("Error","Enter 5 Digit Number Without Characters")
    elif not (ST_student_id_box.get()).isdigit():
        messagebox.showerror("Error","For User ID Only Numeric Value You can Enter")
    elif not ST_dob_box.get().split('/'):
        messagebox.showerror("Error","Date Format is Not Valid")

    
    else:
        #Inserting Records
        curser.execute(" INSERT INTO userTable VALUES(:student_id, :name, :password, :role_id, :date_of_birth, :address, :email)",
                {
                'student_id': ST_student_id_box.get(),
                'name': ST_student_name_box.get(),
                'password': ST_password_box.get(),
                'role_id': "Student",
                'date_of_birth': ST_dob_box.get(),
                'address': ST_address_box.get(),
                'email': ST_email_box.get()
                })
                
        curser.execute(" INSERT INTO courseTable VALUES(:user_id, :course)",
                {
                'user_id': ST_student_id_box.get(),
                'course': ST_course_box.get()
                })

        curser.execute(" INSERT INTO feeTable VALUES(:user_id, :fee, :paid_fee, :remaining_fee)",
                {
                'user_id': ST_student_id_box.get(),
                'fee': ST_fee_box.get(),
                'paid_fee': "",
                'remaining_fee': ""
                })




        # clrear text boxes 

        ST_student_id_box.delete(0,END)
        ST_student_name_box.delete(0,END)
        ST_password_box.delete(0,END)
        ST_dob_box.delete(0,END)
        ST_address_box.delete(0,END)
        ST_email_box.delete(0,END)
        ST_fee_box.delete(0,END)
        ST_course_box.delete(0,END)

    conn.commit()
    conn.close()


def updateRecord():
    
    conn = sqlite3.connect('collegeEasyApp.db')
    curser = conn.cursor()

    #Error Checking
    find_student = ('SELECT user_id FROM userTable WHERE user_id = ?')
    curser.execute(find_student,[(ST_student_id_box.get())])
    resultFind = curser.fetchall()


    if any ([len(ST_student_id_box.get())==0,len(ST_student_name_box.get())==0,
    len(ST_password_box.get())==0,len(ST_dob_box.get())==0,
    len(ST_address_box.get())==0,len(ST_email_box.get())==0,
    len(ST_course_box.get())==0,len(ST_fee_box.get())==0]):
        messagebox.showerror("Error","All fields are required !! ")

    elif (len(ST_student_id_box.get())!=5):
        messagebox.showerror("Error","User ID is not correct! Enter 5 Digit Number Without Dashes")
    elif not (ST_student_id_box.get()).isdigit():
        messagebox.showerror("Error","For NIC Only Numeric Value You can Enter")

    
    else:
        
        recordID = ST_select_id_text_box.get()
        #Inserting Records
        curser.execute(""" UPDATE userTable SET 
            user_id = :student_id,
            name = :name,
            password = :password, 
            role = :role, 
            date_of_birth = :date_of_birth, 
            address = :address, 
            email = :email

            WHERE user_id = :oid""",

                {
                'student_id': ST_student_id_box.get(),
                'name': ST_student_name_box.get(),
                'password': ST_password_box.get(),
                'role': "Student",
                'date_of_birth': ST_dob_box.get(),
                'address': ST_address_box.get(),
                'email': ST_email_box.get(),
                'oid': ST_select_id_text_box.get()
                })
                
        curser.execute(""" UPDATE courseTable SET 

                course_name = :course

                WHERE user_id= :uoid""",
                {
            
                'course': ST_course_box.get(),
                'uoid': ST_select_id_text_box.get()

                })

        curser.execute(""" UPDATE feeTable SET 

                total_fee = :fee

                WHERE user_id= :uuoid""",
                {
            
                'fee': ST_fee_box.get(),
                'uuoid': ST_select_id_text_box.get()

                })




        # clrear text boxes 

        ST_student_id_box.delete(0,END)
        ST_student_name_box.delete(0,END)
        ST_password_box.delete(0,END)
        ST_dob_box.delete(0,END)
        ST_address_box.delete(0,END)
        ST_email_box.delete(0,END)
        ST_fee_box.delete(0,END)
        ST_course_box.delete(0,END)

    conn.commit()
    conn.close()


registerationTitle = Label(admin_frame_register_student,text="MANAGE STUDENT",bg="GRAY", fg="blue",
font=("times new roman",20,"bold"))
registerationTitle.grid(row=31, column=0, pady=5, padx=5, columnspan=3, sticky=W)

# Labels

student_name = Label(admin_frame_register_student, text="Student Name")
student_name.grid(row=32, column=0, pady=5, padx=5, sticky=W)

student_id = Label(admin_frame_register_student, text="ID of Student")
student_id.grid(row=33, column=0, pady=5, padx=5, sticky=W)

password = Label(admin_frame_register_student, text="Student Password")
password.grid(row=34, column=0, pady=5, padx=5, sticky=W)

dob= Label(admin_frame_register_student, text="Date of Birth")
dob.grid(row=36, column=0, pady=5, padx=5, sticky=W)

address = Label(admin_frame_register_student, text="Address")
address.grid(row=37, column=0, pady=5, padx=5, sticky=W)

email = Label(admin_frame_register_student, text="Email ")
email.grid(row=38, column=0, pady=5, padx=5, sticky=W)

fee = Label(admin_frame_register_student, text="Fee ")
fee.grid(row=39, column=0, pady=5, padx=5, sticky=W)

course = Label(admin_frame_register_student, text="Course ")
course.grid(row=40, column=0, pady=5, padx=5, sticky=W)


# Enter Boxes

ST_student_name_box = Entry(admin_frame_register_student, width=30)
ST_student_name_box.grid(row=32, column=1, pady=5, padx=5, sticky=W)

ST_student_id_box = Entry(admin_frame_register_student, width=30)
ST_student_id_box.grid(row=33, column=1, pady=5, padx=5, sticky=W)

ST_password_box = Entry(admin_frame_register_student, width=30)
ST_password_box.grid(row=34, column=1, pady=5, padx=5, sticky=W)

ST_dob_box = DateEntry(admin_frame_register_student, width=20, background='darkblue',foreground='white', borderwidth=2)
ST_dob_box.grid(row=36, column=1, pady=5, padx=5)

ST_address_box = Entry(admin_frame_register_student, width=30)
ST_address_box.grid(row=37, column=1, pady=5, padx=5, sticky=W)

ST_email_box = Entry(admin_frame_register_student, width=30)
ST_email_box.grid(row=38, column=1, pady=5, padx=5, sticky=W)

ST_fee_box = Entry(admin_frame_register_student, width=30)
ST_fee_box.grid(row=39, column=1, pady=5, padx=5, sticky=W)

ST_course_box = Entry(admin_frame_register_student, width=30)
ST_course_box.grid(row=40, column=1, pady=5, padx=5, sticky=W)

insert_button = Button (admin_frame_register_student, text="Register Student Data", command=insert,
bg="pink",font=("times new roman",13,"bold"))
insert_button.grid(row=50,column=0, columnspan=2, pady=5, padx=5, ipadx=60)








# select update delete display record functions ===================

heading = Label(admin_frame_register_student, text="Search, Update, Delete Operations", fg="Red", bg="Yellow")
heading.grid(row=32, column=2, pady=5, padx=5, sticky=W)

student_select_id = Label(admin_frame_register_student, text="Enter ID For Operation")
student_select_id.grid(row=33, column=2, pady=5, padx=5, sticky=W)

ST_select_id_text_box = Entry(admin_frame_register_student, width=30)
ST_select_id_text_box.grid(row=34, column=2, pady=5, padx=5, sticky=W)



student_update_button = Button (admin_frame_register_student, text="Update", command=updateRecord)
student_update_button.grid(row=36,column=2, columnspan=1, pady=5, padx=5, ipadx=100)

student_search_button = Button (admin_frame_register_student, text="Search",command=SearchRecord)
student_search_button.grid(row=37,column=2, columnspan=1, pady=5, padx=5, ipadx=100)

student_delete_button = Button (admin_frame_register_student, text="Delete",command=deleteRecord)
student_delete_button.grid(row=38, column=2, columnspan=1, pady=5, padx=5, ipadx=100)


# STUDENT REGISTERATION FORM ENDSSSSSSS ########################################


# DISPLAY ALL RECORDS FORM STARTSSSSSS ########################################







# Display Profile ########################################


admin_notebook.grid(row=1, column=0)

admin_page_label = Label(admin_frame_display_profile, text="WELCOME ADMIN")
admin_page_label.grid(row=2,column=2, padx=10, pady=30, ipadx=50)











# Creating Teacher Page Frame ##########################################################

teacher_frame = Frame(root, width=1200, height=700, bg="red")



# Create Notebook
teacher_notebook = ttk.Notebook(teacher_frame)

teacher_frame_display_profile = Frame(teacher_notebook, width=1200, height=700, bg="pink")
teacher_frame_attendance = Frame(teacher_notebook, width=1200, height=700, bg="yellow")
teacher_frame_results = Frame(teacher_notebook, width=1200, height=700, bg="blue")
teacher_display_all_record = Frame(teacher_notebook, width=1200, height=700, bg="light blue")


teacher_notebook.add(teacher_frame_display_profile, text="Profile")
teacher_notebook.add(teacher_frame_attendance, text="Add Student Attendacne")
teacher_notebook.add(teacher_frame_results, text="Add Student Results")
teacher_notebook.add(teacher_display_all_record, text="All Student Records")

teacher_notebook.grid(row=0,column=0)

logout_button_teacher_frame = Button(teacher_frame,command=userLogOut, text="Logout", bg="red", fg="white")
logout_button_teacher_frame.place(x=500, y=250, width=75)


shared_variable = userObject.getUserID()

def studentAttendance():
    
    select_date = Label(teacher_frame_attendance, text="Select Date of Attendance",font=("Arial",10,"bold"))
    select_date.grid(row=3, column=0, columnspan=2, ipadx=20, ipady=10)


    date_box = CustomDateEntry(teacher_frame_attendance, width=20, background='darkblue',foreground='white', borderwidth=2)
    date_box._set_text(date_box._date.strftime('%m/%d/%Y'))
    date_box.grid(row=3, column=2, pady=5, padx=5)

    heading_label_1= Label(teacher_frame_attendance, text="User ID", bg="pink")
    heading_label_1.grid(row=4, column=0, ipadx=20)

    heading_label_2= Label(teacher_frame_attendance, text="User Name", bg="pink")
    heading_label_2.grid(row=4, column=1)

    heading_label_3= Label(teacher_frame_attendance, text="ATTENDENCE", bg="pink")
    heading_label_3.grid(row=4, column=2)

    
    courseObjectForAttendance = Course(userObject.getUserID())
    courseForAttendance = courseObjectForAttendance.checkCourse()

    userObjectForAttendance = user(userObject.getUserID())
    roleForAttendance = userObjectForAttendance.getRole()

    userTypeObject = userType(courseForAttendance,"Student")
    result = userTypeObject.studentCourse()


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
        present_label = Label(teacher_frame_attendance,text=present)
        present_label.grid(row=6, column=4, ipadx=20, ipady=5)

        my_cursor.execute("SELECT COUNT(*) FROM attendanceTable WHERE date=? AND attendance=?",[date_box.get(),"L"])
        present = my_cursor.fetchall()
        present_label = Label(teacher_frame_attendance,text=present)
        present_label.grid(row=7, column=4, ipadx=20, ipady=5)

        my_cursor.execute("SELECT COUNT(*) FROM attendanceTable WHERE date=? AND attendance=?",[date_box.get(),"A"])
        present = my_cursor.fetchall()
        present_label = Label(teacher_frame_attendance,text=present)
        present_label.grid(row=8, column=4, ipadx=20, ipady=5)

    entries = []

    for index, x in enumerate(result):
    
        index = index+6
        
        variable = str(x[0])

        lookup_label = Label(teacher_frame_attendance, text=x[0])
        lookup_label.grid(row=index, column=0, ipadx=10, ipady=5, sticky=W)
        

        lookup_label = Label(teacher_frame_attendance, text=x[1])
        lookup_label.grid(row=index, column=1, ipadx=10, ipady=5,sticky=W)

        mark_box = Entry(teacher_frame_attendance, width=10, font=("arial",10,"bold"), justify="center")
        mark_box.grid(row=index, column=2, ipadx=20, ipady=2,sticky=W)
        entries.append(mark_box)
    
    save_attendance = Button (teacher_frame_attendance, text="Save Attendance", command=saveAttendance)
    save_attendance.grid(row=5, column=3, ipadx=0, ipady=5)

    total_present_label = Label(teacher_frame_attendance, text="Total Present: ")
    total_present_label.grid(row=6, column=3, ipadx=0, ipady=5)

    total_leave_label = Label(teacher_frame_attendance, text="Total Leave: ")
    total_leave_label.grid(row=7, column=3, ipadx=0, ipady=5)

    total_absent_label = Label(teacher_frame_attendance, text="Total Leave: ")
    total_absent_label.grid(row=8, column=3, ipadx=0, ipady=5)





def profileTeacherDisplay():

        shared_variable = userObject.getUserID()

        conn =sqlite3.connect("CollegeEasyApp.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM userTable WHERE user_id=" + str(shared_variable))

        profileRecord = cur.fetchall()

        

        profile_name = tk.Label(teacher_frame_display_profile, text="Your Profile ", font=("arial",15,"bold"))
        profile_name.grid(row=6, column=2, columnspan=2, pady=10, ipadx=10)

        profile_name = tk.Label(teacher_frame_display_profile, text="Your User ID is : ")
        profile_name.grid(row=7, column=2, pady=10, ipadx=10, sticky=W)
        profile_id = tk.Label(teacher_frame_display_profile, text=shared_variable)
        profile_id.grid(row=7, column=3, pady=10, ipadx=10)


        profile_name = tk.Label(teacher_frame_display_profile, text="Your Name is : ")
        profile_name.grid(row=8, column=2, pady=10, ipadx=10, sticky=W)
        profile_name = tk.Label(teacher_frame_display_profile, text="Your Designation : ")
        profile_name.grid(row=9, column=2, pady=10, ipadx=10, sticky=W)
        profile_name = tk.Label(teacher_frame_display_profile, text="Date of Birth is : ")
        profile_name.grid(row=10, column=2, pady=10, ipadx=10, sticky=W)
        profile_name = tk.Label(teacher_frame_display_profile, text="Your Address is : ")
        profile_name.grid(row=11, column=2, pady=10, ipadx=10, sticky=W)
        profile_name = tk.Label(teacher_frame_display_profile, text="Your Email is : ")
        profile_name.grid(row=12, column=2, pady=10, ipadx=10, sticky=W)
        profile_name = tk.Label(teacher_frame_display_profile, text="Your Attendance : ")
        profile_name.grid(row=13, column=2, pady=10, ipadx=10, sticky=W)



        profile_name = tk.Label(teacher_frame_display_profile, text=profileRecord[0][1])
        profile_name.grid(row=8, column=3, pady=10, ipadx=10)
        profile_name = tk.Label(teacher_frame_display_profile, text=profileRecord[0][3])
        profile_name.grid(row=9, column=3, pady=10, ipadx=10)
        profile_name = tk.Label(teacher_frame_display_profile, text=profileRecord[0][4])
        profile_name.grid(row=10, column=3, pady=10, ipadx=10)
        profile_name = tk.Label(teacher_frame_display_profile, text=profileRecord[0][5])
        profile_name.grid(row=11, column=3, pady=10, ipadx=10)
        profile_name = tk.Label(teacher_frame_display_profile, text=profileRecord[0][6])
        profile_name.grid(row=12, column=3, pady=10, ipadx=10)
        

        total_leave = previouseMonthAttendance(shared_variable)
        

        profile_name = tk.Label(teacher_frame_display_profile, text=str(total_leave), bg="light blue", bd=5)
        profile_name.grid(row=13, column=3, pady=10, ipadx=10)



        profile_Label = tk.Label(teacher_frame_display_profile, text=shared_variable, bg="light blue")
        profile_Label.grid(row=7, column=3, pady=10, ipadx=10)


def studentResultPage():

    student_result_page = StudentResultPage(teacher_frame_results,userObject)

    student_result_page.pageContent(teacher_frame_results,userObject)

def studentRecrodPage():
    
    student_result_page = StudentDisplayResultPage(teacher_display_all_record,userObject)

    student_result_page.pageContent(teacher_display_all_record,userObject)


# END OF  Teacher Page Frame ##########################################################





# Creating Student Page Frame ##########################################################

student_frame = Frame(root, width=1200, height=600, bg="red")

# Create Notebook
student_notebook = ttk.Notebook(student_frame)

student_frame_display_profile = Frame(student_notebook, width=1200, height=700, bg="pink")
student_frame_result_display = Frame(student_notebook, width=1200, height=700, bg="yellow")


student_notebook.add(student_frame_display_profile, text="Profile")
student_notebook.add(student_frame_result_display, text="Add Student Attendacne")

logout_button_student_frame = Button(student_frame,command=userLogOut, text="Logout", bg="red", fg="white")
logout_button_student_frame.place(x=800, y=300, width=75)


student_notebook.grid(row=0,column=0)



def studentProfilePage():
    
    student_profile_student_page = StudentProfilePage(student_frame_display_profile,userObject)

    student_profile_student_page.pageContent(student_frame_display_profile,userObject)

def studentResultStudentPage():

    student_result_studen_page = StudentResultStudentPage(student_frame_result_display,userObject)

    student_result_studen_page.pageContent(student_frame_result_display,userObject)




##### END OF STUDENT PAGE ####################



# Creating Accountant Page Frame ##########################################################

accountant_frame = Frame(root, width=1200, height=600)

# Create Notebook
accountant_frame_notebook = ttk.Notebook(accountant_frame)

accountant_frame_profile = Frame(accountant_frame, width=1200, height=700, bg="light pink")
accountant_frame_salary = Frame(accountant_frame, width=1200, height=700, bg="light green")


accountant_frame_notebook.add(accountant_frame_profile, text="Profile")
accountant_frame_notebook.add(accountant_frame_salary, text="Salary of All Employees")

accountant_frame_notebook.grid(row=0,column=0)

logout_button_accountant_frame = Button(accountant_frame,command=userLogOut, text="Logout", bg="red", fg="white")
logout_button_accountant_frame.place(x=500, y=300, width=75)

def accountantProfilePage():
    
    accountant_profile_page = AccountantProfilePage(accountant_frame_profile,userObject)

    accountant_profile_page.pageContent(accountant_frame_profile,userObject)

def accountantSalaryPage():

    accountant_salary_page = AccountantSalaryPage(accountant_frame_salary,userObject)

    accountant_salary_page.pageContent(accountant_frame_profile,userObject)


root.mainloop()