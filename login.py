from tkinter import *
from tkinter.ttk import Label, LabelFrame

class Login:
    
    def prompt():
        login_window = Tk()
        login_window.title("PyTracer Contact Tracing App")
        login_window.geometry('400x300')

        login_Frame = LabelFrame(login_window, text='Login to PyTracer')
        login_Frame.pack(expand='yes', fill='both')
        first_label = Label(login_Frame , text= "Welcome back!")
        first_label.place(x=150, y=30)
        second_label = Label(login_Frame, text="We're happy to see you again.")
        second_label.place(x=110, y=50)
        user_name = Label(login_Frame, text = "Username:").place(x = 40, y = 80)
        passcode = Label(login_Frame, text = "Password:").place(x = 40, y = 120)
        user_name_input_area = Entry(login_Frame,width = 30).place(x = 110, y = 80) 
        user_password_entry_area = Entry(login_Frame,width = 30).place(x = 110,y = 120)
        login_window.mainloop()