import sqlite3
from datetime import datetime, date, timedelta

def previouseMonthLeave(user_id):

    conn = sqlite3.connect('collegeEasyApp.db')
    my_cursor = conn.cursor()

    last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
    start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)

    last_day = last_day_of_prev_month.strftime('%m/%d/%Y')
    first_day = start_day_of_prev_month.strftime('%m/%d/%Y')
  
    attendance = "P"

    my_cursor.execute("SELECT COUNT(*) FROM attendanceTable WHERE user_id = ? and attendance = ? and date BETWEEN ? and ? ",[user_id,attendance,first_day,last_day])
    present = my_cursor.fetchall()

    return present[0][0]

    conn.commit()
    conn.close()
