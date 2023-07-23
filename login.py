from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Label, LabelFrame
from functools import partial
from subprocess import call
from pathlib import Path
import csv
import main_menu

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
            username = str(logname.get())
            password = str(logpass.get())
            login = Login.login_authenticator(username, password)
            if login == True:
                login_window.destroy()
        login_try = partial(login_try)

        go_back = Button(login_Frame, text="Go Back", command=return_prompt).place(x=130, y=170)
        go_auth = Button(login_Frame, text='Log in', command=login_try)
        go_auth.place(x=200, y=170)
        show_password = Button(login_Frame, text='show', command=password_show)
        show_password.place(x=310, y=117)
        login_window.mainloop()
    
    def login_authenticator(username, password):
        account_list = Path('./accounts.csv')
        if account_list.is_file():
            with open('accounts.csv', 'r') as user_list:
                user_list_reader = csv.reader(user_list)
                for column in user_list_reader:
                    user_find_value = column[0]
                    for row in user_find_value:
                        if str(row) == username:
                            user_login = row
                            for column in user_login:
                                recorded_password = str(column[1])
                                if recorded_password != password:
                                    messagebox.showerror('Incorrect password', 'Your password is invalid. Please try again.')
                                    login = False
                                    return login
                                if recorded_password == password:
                                    pass
                            else:
                                messagebox.showerror('User not found', 'The username is invalid. Please try again.')
                                login = False
                                return login
        if account_list.is_file() == False:
            with open('accounts.csv', 'w') as new_file:
                writer = csv.writer(new_file)
                writer.writerow(['username',  'password', 'is_positive', 'vacc_status', 'symptoms', 'expose_symptoms', 'is_close_contact', 'has_been_tested', 'phone_number', 'email'])
            messagebox.showinfo('Database created',"The application doesn't have a database yet, so we've made one for you. Please make an account first!")
            login = False
            return login