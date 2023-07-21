from tkinter import *
from tkinter.ttk import Label, LabelFrame
from login import Login
from functools import partial

window = Tk()

window.title("PyTracer Contact Tracing App")
window.geometry('400x200')

welcome_splash = LabelFrame(window, text='Welcome!')
welcome_splash.pack(expand='yes', fill='both')
first_label = Label(welcome_splash , text= "Please click to your destination.")
first_label.place(x=110, y=30)
signup = Button(welcome_splash, text="Sign up").place(x=160, y=120)

def login_prompt():
    window.destroy()
    Login.prompt()

login_prompt = partial(login_prompt)

login = Button(welcome_splash, text='Log in', command=login_prompt).place(x=165, y=70)

window.mainloop()