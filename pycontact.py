from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Label, LabelFrame
from login import Login
from signup import Signup
from functools import partial

def login_prompt():
    window.destroy()
    Login.prompt()

login_prompt = partial(login_prompt)

def signup_prompt():
    window.destroy()
    Signup.new_registry()

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
first_label = Label(welcome_splash , text= "Please click to your destination.")
first_label.place(x=110, y=30)

signup = Button(welcome_splash, text="Sign up", command=signup_prompt).place(x=110, y=70)
exit_button = Button(welcome_splash, text="close PyTracer", command=close_app).place(x=150, y=150)
login = Button(welcome_splash, text='Log in', command=login_prompt).place(x=230, y=70)

window.mainloop()