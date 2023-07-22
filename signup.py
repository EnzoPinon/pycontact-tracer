from tkinter import *
from tkinter.ttk import Label, LabelFrame
from functools import partial
from subprocess import call

class Signup:
    
    def new_registry():

        def return_prompt():
            login_window.destroy()
            call(["python", "pycontact.py"])

        return_prompt = partial(return_prompt)
    
        login_window = Tk()
        login_window.title("PyTracer Contact Tracing App")
        login_window.geometry('500x300')

        login_Frame = LabelFrame(login_window, text='Create an account')
        login_Frame.pack(expand='yes', fill='both')
        first_label = Label(login_Frame , text= "Get Started")
        first_label.place(x=215, y=30)
        second_label = Label(login_Frame, text="Part 01: account information")
        second_label.place(x=175, y=50)
        user_name = Label(login_Frame, text = "Username:").place(x = 40, y = 80)
        passcode = Label(login_Frame, text = "Your password:",).place(x = 40, y = 120)
        passcode = Label(login_Frame, text = "Confirm password:",).place(x = 40, y = 160)
        user_name_input_area = Entry(login_Frame,width = 30).place(x = 170, y = 80) 
        user_password_entry_area = Entry(login_Frame, show='*',width = 30)
        user_password_entry_area.place(x = 170,y = 120)
        confirm_password_entry = Entry(login_Frame, show='*',width = 30)
        confirm_password_entry.place(x = 170,y = 160)
        go_back = Button(login_Frame, text="Go Back", command=return_prompt).place(x=40, y=200)

        def password_show():
            if user_password_entry_area.cget('show') == '':
                user_password_entry_area.config(show= '*')
                show_password.config(text='show')
            else:
                user_password_entry_area.config(show= '')
                show_password.config(text='hide')
        
        def password_show_2():
            if confirm_password_entry.cget('show') == '':
                confirm_password_entry.config(show= '*')
                show_password_again.config(text='show')
            else:
                confirm_password_entry.config(show= '')
                show_password_again.config(text='hide')
        password_show = partial(password_show)
        password_show_2 = partial(password_show_2)

        show_password = Button(login_Frame, text='show', command=password_show)
        show_password.place(x=380, y=117)
        show_password_again = Button(login_Frame, text='show', command=password_show_2)
        show_password_again.place(x=380, y=157)
        login_window.mainloop()