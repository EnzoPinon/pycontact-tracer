from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Label, LabelFrame
from functools import partial
from health_decla_system import health_check
import datetime
import csv

class main_menu:
    
    def startup():

        def signup_prompt():
            window.destroy()
            main_menu.user_menu()

        signup_prompt = partial(signup_prompt)

        def close_app():
            confirm = messagebox.askquestion('Exit PyTracer', 'Do you wish to exit the app?')

            if confirm == 'yes':
                window.destroy()
            else:
                return
            
        close_app = partial(close_app)

        window = Tk()

        window.title("PyTracer Contact Tracing App")
        window.geometry('400x200')

        welcome_splash = LabelFrame(window, text='Welcome!')
        welcome_splash.pack(expand='yes', fill='both')
        first_label = Label(welcome_splash , text= "Press 'Get Started' to begin.")
        first_label.place(x=130, y=30)

        signup = Button(welcome_splash, text="Get Started", command=signup_prompt).place(x=160, y=70)
        exit_button = Button(welcome_splash, text="close PyTracer", command=close_app).place(x=150, y=130)

        window.mainloop()

    def user_menu():
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
        first_label = Label(side_bar , text= "Main Menu")
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
                main_menu.startup()
        logout_user = partial(logout_user)

        def hdf_start():
            menu_window.destroy()
            health_check.locate_info()
        hdf_start = partial(hdf_start)

        user_setting = Button(side_bar, text= "About PyTracer")
        user_setting.place(x=70, y=70)
        hdf_maker = Button(side_bar, text='Create HDF Log', command=hdf_start)
        hdf_maker.place(x=70, y=110)
        print_hdf = Button(side_bar, text= "Search HDF Log")
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