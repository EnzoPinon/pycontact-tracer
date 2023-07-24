from tkinter import *
from tkinter.ttk import Label, LabelFrame
from functools import partial
from subprocess import call

class main_menu:
    
    def user_menu(username):
        menu_window = Tk()
        menu_window.title("PyTracer Contact Tracing App")
        menu_window.geometry('600x300')

        login_Frame = LabelFrame(menu_window, text='Main Menu')
        login_Frame.pack(expand='yes', fill='both')
        first_label = Label(login_Frame , text= "Welcome, " + username)
        first_label.place(x=150, y=30)
        menu_window.mainloop()

    def user_settings():
        pass

    def logout_user():
        pass