import sqlite3


class User:
    def __init__(self, user_id='100', user_type='user_type'):
        self.user_id = user_id
        self.user_type = user_type

    def setter(self):
        
        conn = sqlite3.connect('collegeEasyApp.db')
        curser = conn.cursor()
        
        curser.execute(" INSERT INTO userTable VALUES(:user_id,:user_type)",
                {
                'user_id': self.user_id,
                'user_type': self.user_type
                })
        
        conn.commit()
        conn.close()
    
    def getter(self):
        return self.user_id
    
    def getter_user_type(self):
        
        conn =sqlite3.connect("CollegeEasyApp.db")
        cur = conn.cursor()
       
        cur.execute("SELECT user_type FROM userTable WHERE user_id=" + str(self.user_id))

        profileRecord = cur.fetchall()

        return profileRecord

    def remove(self):
             
        conn =sqlite3.connect("collegeEasyapp.db")
        cur2 = conn.cursor()
        cur2.execute("DELETE from userTable WHERE user_id=?",(
                                                                    self.user_id,
        ))

        conn.commit()
        conn.close()


    def checkUser(self):
    
        conn = sqlite3.connect('collegeEasyApp.db')
        my_cur = conn.cursor()

        find_student = ('SELECT * FROM userTable WHERE user_id = ?')
        my_cur.execute(find_student,[(self.user_id),])
        result = my_cur.fetchone()

        return result

        conn.close()