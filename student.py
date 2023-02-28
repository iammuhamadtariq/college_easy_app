import sqlite3
from user import User

class Student:
    def __init__(self, user_id='user_id', name='name', password='name1', gender='Male', date_of_birth='05/05/1995',email='email', address='address', phone_number='03326026272', course='Python', fee=28500, paid_fee=0):

        self.user_id = user_id
        self.name = name
        self.password = password
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.course = course
        self.fee = fee
        self.paid_fee = paid_fee


    def setter(self):
         
        conn = sqlite3.connect('collegeEasyApp.db')
        curser = conn.cursor()
        
        curser.execute(" INSERT INTO studentTable VALUES(:user_id, :name, :password, :gender, :date_of_birth, :email, :address, :phone_number, :course, :fee, :paid_fee)",
                {
                'user_id': self.user_id,
                'name': self.name,
                'password': self.password,
                'gender': self.gender,
                'date_of_birth': self.date_of_birth,
                'email': self.email,
                'address': self.address,
                'phone_number': self.phone_number,
                'course': self.course,
                'fee': self.fee,
                'paid_fee': self.paid_fee
                })
        
        conn.commit()
        conn.close()



    def update(self):

        conn =sqlite3.connect("collegeEasyApp.db")
        cur2 = conn.cursor()
        cur2.execute("UPDATE studentTable SET user_id=?, name=?, password=?, gender=?, date_of_birth=?, email=?, address=?, phone_number=?, course=?, fee=?, paid_fee=? WHERE user_id=?",(
                                                                    self.user_id,
                                                                    self.name,
                                                                    self.password,
                                                                    self.gender,
                                                                    self.date_of_birth,
                                                                    self.email,
                                                                    self.address,
                                                                    self.phone_number,
                                                                    self.course,
                                                                    self.fee,
                                                                    self.paid_fee,
                                                                    self.user_id
        ))
        conn.commit()
        conn.close()
    
    def remove(self):
        
        conn =sqlite3.connect("collegeEasyapp.db")
        cur2 = conn.cursor()
        cur2.execute("DELETE from studentTable WHERE user_id=?",(
                                                                    self.user_id,
        ))

        conn.commit()
        conn.close()


    def getter(self):

        conn = sqlite3.connect('collegeEasyApp.db')
        my_cur = conn.cursor()

        find_student = ('SELECT * FROM studentTable WHERE user_id = ?')
        my_cur.execute(find_student,[(self.user_id),])
        result = my_cur.fetchall()
        conn.close()
        return result

        