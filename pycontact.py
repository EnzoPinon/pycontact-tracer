from tkinter import *
from tkinter.ttk import Label, LabelFrame

window = Tk()

window.title("Pycontact-tracer: A contact tracing app in Python")
window.geometry('400x200')

welcome_splash = LabelFrame(window, text='Welcome!')
welcome_splash.pack(expand='yes', fill='both')
first_label = Label(welcome_splash , text= "Please click to your destination.")
first_label.place(x=110, y=30)
employee_button = Button(welcome_splash, text="Sign up").place(x=160, y=120)
admin_button = Button(welcome_splash, text='Log in').place(x=165, y=70)
window.mainloop()