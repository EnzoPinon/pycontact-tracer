from tkinter import *
from tkinter.ttk import Label, LabelFrame

window = Tk()

window.title("Pycontact-tracer: A contact tracing app in Python")
window.geometry('1024x576')

welcome_splash = LabelFrame(window, text='Welcome!')
welcome_splash.pack(expand='yes', fill='both')
first_label = Label(welcome_splash , text= "Please click to your destination.")
first_label.place(x=100, y=200)
window.mainloop()