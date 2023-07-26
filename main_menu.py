from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Label, LabelFrame
from functools import partial
from health_decla_system import health_check
import datetime

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
                menu_window.destroy()
                main_menu.startup()
        logout_user = partial(logout_user)

        def hdf_start():
            menu_window.destroy()
            health_check.locate_info()
        hdf_start = partial(hdf_start)

        def hdfsearch_start():
            menu_window.destroy()
            main_menu.search_HDF()
        hdfsearch_start = partial(hdfsearch_start)
        
        def about_show():
            menu_window.destroy()
            main_menu.AboutPyTracer()
        about_show = partial(about_show)

        user_setting = Button(side_bar, text= "About PyTracer", command=about_show)
        user_setting.place(x=70, y=70)
        hdf_maker = Button(side_bar, text='Create HDF Log', command=hdf_start)
        hdf_maker.place(x=70, y=110)
        print_hdf = Button(side_bar, text= "Search HDF Log", command=hdfsearch_start)
        print_hdf.place(x=70, y=150)
        logout = Button(side_bar, text= "Log Out", command=logout_user)
        logout.place(x=70, y=190)

        menu_window.mainloop()

    def AboutPyTracer():
        def return_prompt():
            window.destroy()
            main_menu.user_menu()

        return_prompt = partial(return_prompt)

        window = Tk()

        window.title("PyTracer Contact Tracing App")
        window.geometry('500x350')

        welcome_splash = LabelFrame(window, text='About PyTracer')
        welcome_splash.pack(expand='yes', fill='both')
        first_label = Label(welcome_splash , text= "PyTracer: A Contact Tracing App in Python.")
        first_label.place(x=120, y=30)
        description = Label(welcome_splash , text= "PyTracer is an Open Source Contact Tracing App written purely in Python\nby Lorenzo Pinon, a Computer Engineering student of the\nPolytechnic University of the Philippines (Sta. Mesa Branch).\n\nOur Goal:\n\nTo provide a user-friendly and reliable Contact Tracing app to all establishments\nwithout the need to pay anything.")
        description.place(x=30, y=70)

        def go_to_repo():
            import webbrowser
            webbrowser.open('https://github.com/EnzoPinon/pycontact-tracer')
        go_to_repo = partial(go_to_repo)

        print_hdf = Button(welcome_splash, text= "View Our Repository", command=go_to_repo)
        print_hdf.place(x=70, y=250)
        logout = Button(welcome_splash, text= "Back to Menu", command=return_prompt)
        logout.place(x=300, y=250)

    def search_HDF():
        def return_prompt():
            login_window.destroy()
            main_menu.user_menu()

        return_prompt = partial(return_prompt)
    
        login_window = Tk()
        login_window.title("PyTracer Contact Tracing App")
        login_window.geometry('500x400')

        login_Frame = LabelFrame(login_window, text='Search HDF Forms')
        login_Frame.pack(expand='yes', fill='both')
        first_label = Label(login_Frame , text= "Search an HDF Generated Form")
        first_label.place(x=175, y=30)
        second_label = Label(login_Frame, text="All parts are required.")
        second_label.place(x=205, y=50)
        question_1 = Label(login_Frame, text = "Name:").place(x = 40, y = 80)
        question_2 = Label(login_Frame, text = "Date (MM-DD-YYYY Format, separated by dashes):",).place(x = 40, y = 160)
        question_3 = Label(login_Frame, text = "Time (HH:MM, separated by colon. Use 0000 format.):",).place(x = 40, y = 240)

        first_a = StringVar()
        second_a = StringVar()
        third_a = StringVar()

        def part02(ans01, ans02, ans03):
            import subprocess
            import datetime
            import os
            ans01 = first_a.get()
            ans02 = second_a.get()
            ans03 = third_a.get()
            fulltime = ans02 + ' ' + ans03

            try:
                testdate = datetime.datetime.strptime(fulltime, '%m-%d-%Y %H:%M')
            except ValueError:
                return messagebox.showerror("Invalid date/time Format", "The date and time provided is in an invalid format.\nPlease follow the format mentioned.\n\nDate: MM-DD-YYYY (ex: 01-01-2000)\nTime: HH:MM in 0000hr format (ex: 13:00)")
            mydate = datetime.datetime.strptime(fulltime, '%m-%d-%Y %H:%M')
            year = mydate.strftime('%Y')
            day = mydate.strftime('%j')
            hour = mydate.strftime('%H')
            minute = mydate.strftime('%M')

            check = main_menu.filesearch(ans01, year, day, hour, minute)
            if check == True:
                filename = ans01 + '-' + year + '-' + day + '-' + hour + '-' + minute + '.txt'
                login_window.destroy()
                subprocess.Popen(['notepad', os.path.join('./HDF_generations/' + filename)])
                messagebox.showinfo("HDF Opened", "An HDF has been found with the given parameters and has been displayed.")
                main_menu.user_menu()
            if check == False:
                messagebox.showerror("No HDF Found", "We couldn't find an HDF at the given information.\nEnsure that your date, name, and time are at the right format.\n\nDate: MM-DD-YYYY (ex: 01-01-2000)\nTime: HH:MM in 0000 format (ex: 13:00)")

        part02 = partial(part02, first_a, second_a, third_a)
        answer_01 = Entry(login_Frame,width = 40, textvariable=first_a)
        answer_01.place(x = 40, y = 120) 
        answer_02 = Entry(login_Frame, width = 40, textvariable=second_a)
        answer_02.place(x = 40,y = 200)
        answer_03 = Entry(login_Frame,width = 40, textvariable=third_a)
        answer_03.place(x = 40,y = 280)

        go_back = Button(login_Frame, text="Go Back", command=return_prompt).place(x=140, y=320)
        go_back = Button(login_Frame, text="Search",command=part02).place(x=280, y=320)

        login_window.mainloop()
    
    def filesearch(name, year, day, hour, minute):

        filename = name + '-' + year + '-' + day + '-' + hour + '-' + minute + '.txt'
        import os
        
        hdf_list = os.listdir('./HDF_generations')
        is_found = False
        for name in hdf_list:
            if name == filename:
                is_found = True

        return is_found
                

            