from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Label, LabelFrame
from functools import partial
from subprocess import call
from pathlib import Path
import csv
from main_menu import main_menu

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
        
        logname = StringVar()
        logpass = StringVar()
        user_name_input_area = Entry(login_Frame,width = 30, textvariable=logname)
        user_name_input_area.place(x = 110, y = 80) 
        user_password_entry_area = Entry(login_Frame, show='*',width = 30, textvariable=logpass)
        user_password_entry_area.place(x = 110,y = 120)

        def login_try():
            db_exist = Login.validate_database()
            if db_exist == True:
                username = str(logname.get())
                password = str(logpass.get())
                login = Login.authenticate(username, password)
                if login == True:
                    with open('active_session.csv', 'w') as active_session:
                        writer = csv.writer(active_session)
                        writer.writerow([username])
                    active_session.close()
                    login_window.destroy()
                    main_menu.user_menu(username)
        login_try = partial(login_try)

        go_back = Button(login_Frame, text="Go Back", command=return_prompt).place(x=130, y=170)
        go_auth = Button(login_Frame, text='Log in', command=login_try)
        go_auth.place(x=200, y=170)
        show_password = Button(login_Frame, text='show', command=password_show)
        show_password.place(x=310, y=117)
        login_window.mainloop()
    
    def validate_database():
        account_list = Path('./accounts.csv').is_file()
        if account_list:
            db_exist = True
            return db_exist
        else:
            with open('accounts.csv', 'w', newline='') as new_file:
                writer = csv.writer(new_file)
                writer.writerow(['username',  'password', 'is_positive', 'vacc_status', 'symptoms', 'expose_symptoms', 'is_close_contact', 'has_been_tested', 'phone_number', 'email'])
                messagebox.showinfo('Database created',"The application doesn't have a database yet, so we've made one for you.")
                db_exist = True
                return db_exist
    
    def authenticate(username, password):
        print('active')
        with open('accounts.csv', 'r') as user_list:

            user_list_reader = csv.reader(user_list, delimiter=',')
            next(user_list_reader, None)

            user_exist = False
            while user_exist == False:
                for row in user_list_reader:
                    typed_credentials = [username, password]
                    recorded = [row[0], row[1]]
                    if recorded == typed_credentials:
                        login = True
                        return login
                if user_exist == False:
                    messagebox.showerror("Invalid Credentials", "The password and/or username is invalid. Please try again.")
                    login = False
                    return