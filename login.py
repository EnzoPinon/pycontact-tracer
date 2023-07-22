from tkinter import *
from tkinter.ttk import Label, LabelFrame
from functools import partial
from subprocess import call

class Login:
    
    def prompt():

        def return_prompt():
            login_window.destroy()
            call(["python", "pycontact.py"])

        return_prompt = partial(return_prompt)
    
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
        passcode = Label(login_Frame, text = "Password:",).place(x = 40, y = 120)

        def password_show():
            if user_password_entry_area.cget('show') == '':
                user_password_entry_area.config(show= '*')
                show_password.config(text='show')
            else:
                user_password_entry_area.config(show= '')
                show_password.config(text='hide')
        password_show = partial(password_show)
        user_name_input_area = Entry(login_Frame,width = 30).place(x = 110, y = 80) 
        user_password_entry_area = Entry(login_Frame, show='*',width = 30)
        user_password_entry_area.place(x = 110,y = 120)
        go_back = Button(login_Frame, text="Go Back", command=return_prompt).place(x=40, y=150)
        show_password = Button(login_Frame, text='show', command=password_show)
        show_password.place(x=310, y=117)
        login_window.mainloop()