

from tkinter import *  


my_window = Tk()
my_window.title("This is my title ")
my_window.geometry("600x300")

my_label = Label(my_window, text="This is my label")
my_label.place(x=400,y=50)

my_button = Button(my_window, text="Submit")
my_button.place(x=200, y=50)

my_window.mainloop()