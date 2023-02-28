import sqlite3
from user import User

class Accountant:
    def __init__(self, user_id='user_id', name='name', password='name1', gender='Male', date_of_birth='05/05/1995',email='email', address='address', phone_number='03326026272', scale='15', salary=50000):

        self.user_id = user_id
        self.name = name
        self.password = password
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.scale = scale
        self.salary = salary



    def setter(self):
         
        conn = sqlite3.connect('collegeEasyApp.db')
        curser = conn.cursor()
        
        curser.execute(" INSERT INTO accountantTable VALUES(:user_id, :name, :password, :gender, :date_of_birth, :email, :address, :phone_number, :scale, :salary)",
                {
                'user_id': self.user_id,
                'name': self.name,
                'password': self.password,
                'gender': self.gender,
                'date_of_birth': self.date_of_birth,
                'email': self.email,
                'address': self.address,
                'phone_number': self.phone_number,
                'scale': self.scale,
                'salary': self.salary
                
                })
        
        conn.commit()
        conn.close()



    def update(self):

        conn =sqlite3.connect("collegeEasyApp.db")
        cur2 = conn.cursor()
        cur2.execute("UPDATE accountantTable SET user_id=?, name=?, password=?, gender=?, date_of_birth=?, email=?, address=?, phone_number=?, scale=?, salary=? WHERE user_id=?",(
                                                                    self.user_id,
                                                                    self.name,
                                                                    self.password,
                                                                    self.gender,
                                                                    self.date_of_birth,
                                                                    self.email,
                                                                    self.address,
                                                                    self.phone_number,
                                                                    self.scale,
                                                                    self.salary,
                                                                    self.user_id
        ))
        conn.commit()
        conn.close()
    
    def remove(self):
        
        conn =sqlite3.connect("collegeEasyapp.db")
        cur2 = conn.cursor()
        cur2.execute("DELETE from accountantTable WHERE user_id=?",(
                                                                    self.user_id,
        ))

        conn.commit()
        conn.close()

    def getter_all(self):
        
        conn =sqlite3.connect("collegeEasyapp.db")
        cur2 = conn.cursor()
        cur2.execute("SELECT * from accountantTable")
        result = cur2.fetchall()

        conn.commit()
        conn.close()
        return result