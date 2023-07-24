from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Label, LabelFrame
from functools import partial
from subprocess import call
import datetime
import csv

class main_menu:
    
    def user_menu(username):
        date_now = datetime.datetime.now()
        date_string = date_now.strftime('%c')
        menu_window = Tk()
        menu_window.title("PyTracer Contact Tracing App")
        menu_window.geometry('500x300')

        login_Frame = LabelFrame(menu_window, text='Main Menu')
        login_Frame.pack(expand='yes', fill='both')
        side_bar = Canvas()
        side_bar.create_line(300, 0, 300, 300, dash = (5, 2))
        side_bar.pack(expand='yes', fill='both')
        first_label = Label(side_bar , text= "Welcome, " + username)
        first_label.place(x=120, y=30)
        second_label = Label(side_bar, text= "Date and Time:").place(x=360, y=100)
        date_time = Label(side_bar, text=date_string).place(x=335, y=140)

        def logout_user():
            confirm_logout = messagebox.askquestion("Log out of PyTracer", "Are you sure you want to log out?")
            if confirm_logout == 'no':
                return
            if confirm_logout == 'yes':
                print("button clicked")
                main_menu.end_session()
                menu_window.destroy()
                call(["python", "pycontact.py"])
        logout_user = partial(logout_user)


        user_setting = Button(side_bar, text= "User Settings")
        user_setting.place(x=70, y=70)
        hdf_maker = Button(side_bar, text='Create Health Declaration Form')
        hdf_maker.place(x=70, y=110)
        print_hdf = Button(side_bar, text= "Generate HDF Report")
        print_hdf.place(x=70, y=150)
        logout = Button(side_bar, text= "Log Out", command=logout_user)
        logout.place(x=70, y=190)

        menu_window.mainloop()

    def user_settings():
        pass

    def end_session():
        print("end session active")
        with open('active_session.csv', 'w') as my_file:
            writer = csv.writer(my_file)
            writer.writerow(" ")
            print("Ended session")
            my_file.close()
        return