from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from adminTab1 import AdminTab1 #adminProfile
from adminTab2 import AdminTab2 #Student Manage
from adminTab3 import AdminTab3 #Teacher Manage
from adminTab4 import AdminTab4 #Accountant manage
from adminTab5 import AdminTab5 #Admin manage
from adminTab6 import AdminTab6 #Employee Attendance

from teacherTab1 import TeacherTab1 # Teacher Profile
from teacherTab2 import TeacherTab2 # Teacher Attendance
from teacherTab3 import TeacherTab3 # Teacher Result Page

from studentTab2 import StudentTab2 # Student Result Page
from studentTab1 import StudentTab1 # Student Profile Page

from accountantTab1 import AccountantTab1 # Accountant Profile Page
from accountantTab2 import AccountantTab2 # Accountant Salary Page
from user import User

global userObject


class CollegeEasyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("College Easy App")
        self.root.geometry("1325x680+10+10")

        ########## Page Contents #########

        my_menu = Menu(self.root)
        root.config(menu=my_menu)

        #create menu items

        menu_item = Menu(my_menu)
        
        my_menu.add_cascade(label="   Exit / SignOut   ", menu=menu_item)
        menu_item.add_command(label="Sign Out", command=self.login_frame_open)

        menu_item.add_separator()
        menu_item.add_separator()    
        menu_item.add_command(label="Exit", command=self.root.quit)
        menu_item.add_separator() 

        # Login Frame

        self.login_frame = Frame(self.root, bg="light pink")
        self.login_frame.place(x=0, y=0, width=1325, height=680)

        self.login_title = Label(self.login_frame, text="College Easy App", bg="pink", fg="red", font=("arial",35,"bold"))
        self.login_title.place(x=0,y=0, width=1325)

        self.user_id_label = Label (self.login_frame, text="Enter User ID",bg="blue", fg="white", font=("arial",15,"bold"))
        self.user_id_label.place(x=300, y=200, width=300)
    
        self.user_password_label = Label (self.login_frame, text="Enter Password",bg="blue", fg="white", font=("arial",15,"bold"))
        self.user_password_label.place(x=300, y=250, width=300)

        self.user_id_entry = Entry (self.login_frame, text="Enter User ID",bg="blue", fg="white", font=("arial",15,"bold"))
        self.user_id_entry.place(x=650, y=200, width=300)
    
        self.user_password_entry = Entry (self.login_frame, text="Enter Password",bg="blue", fg="white", font=("arial",15,"bold"), show="*")
        self.user_password_entry.place(x=650, y=250, width=300)
    
        self.login_button = Button(self.login_frame, text="Login", bg="red", fg="white", font=("areial",12,"bold"), command=self.loginFunction)
        self.login_button.place(x=750, y=300, width=200)

        # Admin Frame

        self.admin_frame = Frame(self.root, bg="plum")

        # Create Admin Notebook

        self.admin_notebook = ttk.Notebook(self.admin_frame)

        self.admin_tab1 = Frame(self.admin_notebook, width=1325, height=680, bg="lightgreen")
        self.admin_tab2 = Frame(self.admin_notebook, width=1325, height=680, bg="light pink")
        self.admin_tab3 = Frame(self.admin_notebook, width=1325, height=680, bg="lightblue")
        self.admin_tab4 = Frame(self.admin_notebook, width=1325, height=680, bg="cyan")
        self.admin_tab5 = Frame(self.admin_notebook, width=1325, height=680, bg="lightgreen")
        self.admin_tab6 = Frame(self.admin_notebook, width=1325, height=680, bg="lightblue")

        self.admin_notebook.add(self.admin_tab1, text="adminProfile")
        self.admin_notebook.add(self.admin_tab2, text="Manage Student")
        self.admin_notebook.add(self.admin_tab3, text="Manage Teacher")
        self.admin_notebook.add(self.admin_tab4, text="Manage Accountant")
        self.admin_notebook.add(self.admin_tab5, text="Manage Admin")
        self.admin_notebook.add(self.admin_tab6, text="Employee Attendance")

        self.admin_notebook.place(x=0, y=0)


        
        self.tab2_object = AdminTab2 (self.admin_tab2)
        self.tab3_object = AdminTab3 (self.admin_tab3)
        self.tab4_object = AdminTab4 (self.admin_tab4)
        self.tab5_object = AdminTab5 (self.admin_tab5)
        self.tab6_object = AdminTab6 (self.admin_tab6)





        # Teacher Frame

        self.teacher_frame = Frame(self.root, bg="gold")

        self.teacher_notebook = ttk.Notebook(self.teacher_frame)

        self.teacher_tab1 = Frame(self.teacher_notebook, width=1325, height=680, bg="lightgreen")
        self.teacher_tab2 = Frame(self.teacher_notebook, width=1325, height=680, bg="light pink")
        self.teacher_tab3 = Frame(self.teacher_notebook, width=1325, height=680, bg="lightblue")

        self.teacher_notebook.add(self.teacher_tab1, text="adminProfile")
        self.teacher_notebook.add(self.teacher_tab2, text="Mark Attendance")
        self.teacher_notebook.add(self.teacher_tab3, text="Add Result")

        self.teacher_notebook.place(x=0, y=0)





        #Accountant Frame

        self.accountant_frame = Frame(self.root, bg="light green")

        self.accountant_frame = Frame(self.root, bg="gold")

        self.accountant_notebook = ttk.Notebook(self.accountant_frame)

        self.accountant_tab1 = Frame(self.accountant_notebook, width=1325, height=680, bg="lightgreen")
        self.accountant_tab2 = Frame(self.accountant_notebook, width=1325, height=680, bg="light pink")

        self.accountant_notebook.add(self.accountant_tab1, text="  adminProfile  ")
        self.accountant_notebook.add(self.accountant_tab2, text="  Salary Sheet  ")


        self.accountant_notebook.place(x=0, y=0)


        # Student Frame

        self.student_frame = Frame(self.root, bg="light cyan")


        self.student_frame = Frame(self.root, bg="gold")

        self.student_notebook = ttk.Notebook(self.student_frame)

        self.student_tab1 = Frame(self.student_notebook, width=1325, height=680, bg="lightgreen")
        self.student_tab2 = Frame(self.student_notebook, width=1325, height=680, bg="light pink")
  
        self.student_notebook.add(self.student_tab1, text="  adminProfile  ")
        self.student_notebook.add(self.student_tab2, text="  Check Result  ")

        self.student_notebook.place(x=0, y=0)

    def loginFunction(self):
            
        # Create objects of classes 

        global userObject
        userObject = User(self.user_id_entry.get())
        

        if self.user_id_entry.get()=="" or self.user_password_entry.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif (self.user_id_entry.get()!="" and self.user_password_entry.get()!=""):

            result = userObject.checkUser()

            if result:

                role_type = (userObject.getter_user_type())[0][0]
                
                if role_type == "teacher":
                    self.teacherProfile()
                    self.teacher_frame_open()

                elif role_type == "accountant":
                    self.accountantProfile()
                    self.accountant_frame_open()

                elif role_type == "admin":
                    self.adminProfile()
                    self.admin_frame_open()

                else:
                    self.studentProfile()
                    self.student_frame_open()
                
            else:
                messagebox.showerror("Error","Invalid Username or Password")

        

    def admin_frame_open(self):
        self.hide_all_frame()
        self.admin_frame.place(x=0, y=0, width=1325, height=680)
    
    def login_frame_open(self):
        self.hide_all_frame()
        self.login_frame.place(x=0, y=0, width=1325, height=680)


    def teacher_frame_open(self):
        self.hide_all_frame()
        self.teacher_frame.place(x=0, y=0, width=1325, height=680)

    def accountant_frame_open(self):
        self.hide_all_frame()
        self.accountant_frame.place(x=0, y=0, width=1325, height=680)

    def student_frame_open(self):
        self.hide_all_frame()
        self.student_frame.place(x=0, y=0, width=1325, height=680)

    def hide_all_frame(self):
        self.login_frame.place_forget()
        self.admin_frame.place_forget()
        self.teacher_frame.place_forget()
        self.student_frame.place_forget()
        self.accountant_frame.place_forget()       

    def adminProfile(self):
        self.tab1_object = AdminTab1 (self.admin_tab1,userObject.getter())

    def teacherProfile(self):
        
        self.teacher_tab1_object = TeacherTab1 (self.teacher_tab1,userObject.getter())
        self.teacher_tab2_object = TeacherTab2(self.teacher_tab2,userObject.getter())
        self.teacher_tab3_object = TeacherTab3(self.teacher_tab3,userObject.getter(),userObject)


    def studentProfile(self):

        self.student_tab2_object = StudentTab2(self.student_tab2, userObject.getter(), userObject)
        self.student_tab1_object = StudentTab1 (self.student_tab1,userObject.getter())


    def accountantProfile(self):

        self.accountant_tab1_object = AccountantTab1(self.accountant_tab1, userObject.getter())
        self.accountant_tab2_object = AccountantTab2(self.accountant_tab2, userObject.getter())

root = Tk()
CollegeEasyApp_Object = CollegeEasyApp(root)
root.mainloop()