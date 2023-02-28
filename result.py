import sqlite3

class Result:
    def __init__(self, user_id, result="Pass"):
        self.user_id = user_id
        self.result = result

    def getter(self):


        conn =sqlite3.connect("CollegeEasyApp.db")
        cur = conn.cursor()
       
        cur.execute("SELECT * FROM resultTable WHERE user_id=" + str(self.user_id))

        profileRecord = cur.fetchall()

        return profileRecord       
        