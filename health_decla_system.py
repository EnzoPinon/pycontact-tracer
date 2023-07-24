from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Label, LabelFrame
from functools import partial
import datetime
import csv

class health_check:
    
    def locate_info():
        from main_menu import main_menu
        def return_prompt():
            login_window.destroy()
            main_menu.user_menu()

        return_prompt = partial(return_prompt)
    
        login_window = Tk()
        login_window.title("PyTracer Contact Tracing App")
        login_window.geometry('500x500')

        login_Frame = LabelFrame(login_window, text='Health Declaration Form (1/4)')
        login_Frame.pack(expand='yes', fill='both')
        first_label = Label(login_Frame , text= "Update your Information")
        first_label.place(x=175, y=30)
        second_label = Label(login_Frame, text="Part 01 of 04")
        second_label.place(x=205, y=50)
        question_1 = Label(login_Frame, text = "Where will you go today?").place(x = 40, y = 80)
        question_2 = Label(login_Frame, text = "When will you visit there?",).place(x = 40, y = 160)
        question_3 = Label(login_Frame, text = "When did you last go out with your friends?",).place(x = 40, y = 240)
        question_4 = Label(login_Frame, text="Where did you last went during that day?").place(x=40, y=320)

        first_a = StringVar()
        second_a = StringVar()
        third_a = StringVar()
        fourth_a = StringVar()

        def part02():
            health_check.symptom_check()
        part02 = partial(part02)
        answer_01 = Entry(login_Frame,width = 40, textvariable=first_a)
        answer_01.place(x = 40, y = 120) 
        answer_02 = Entry(login_Frame, width = 40, textvariable=second_a)
        answer_02.place(x = 40,y = 200)
        answer_03 = Entry(login_Frame,width = 40, textvariable=third_a)
        answer_03.place(x = 40,y = 280)
        answer_04 = Entry(login_Frame,width = 40, textvariable=fourth_a)
        answer_04.place(x = 40,y = 360)

        go_back = Button(login_Frame, text="Go Back", command=return_prompt).place(x=140, y=400)
        go_back = Button(login_Frame, text="Next Part",command=part02).place(x=280, y=400)

        login_window.mainloop()

    def symptom_check():
        from main_menu import main_menu
        def return_prompt():
            login_window.destroy()
            main_menu.user_menu()

        return_prompt = partial(return_prompt)
    
        login_window = Tk()
        login_window.title("PyTracer Contact Tracing App")
        login_window.geometry('500x500')

        login_Frame = LabelFrame(login_window, text='Health Declaration Form (2/4)')
        login_Frame.pack(expand='yes', fill='both')
        first_label = Label(login_Frame , text= "Update your Information")
        first_label.place(x=175, y=30)
        second_label = Label(login_Frame, text="Part 02 of 04")
        second_label.place(x=205, y=50)
        question_1 = Label(login_Frame, text = "Have you experienced the following for the past seven (7) days?").place(x = 40, y = 80)

        first_a = StringVar()
        second_a = StringVar()
        third_a = StringVar()
        fourth_a = StringVar()
        def part02():
            health_check.vacc_test_status()
        part02 = partial(part02)
        answer_01 = Entry(login_Frame,width = 40, textvariable=first_a)
        answer_01.place(x = 40, y = 120) 
        answer_02 = Entry(login_Frame, width = 40, textvariable=second_a)
        answer_02.place(x = 40,y = 200)
        answer_03 = Entry(login_Frame,width = 40, textvariable=third_a)
        answer_03.place(x = 40,y = 280)
        answer_04 = Entry(login_Frame,width = 40, textvariable=fourth_a)
        answer_04.place(x = 40,y = 360)

        go_back = Button(login_Frame, text="Go Back", command=return_prompt).place(x=140, y=400)
        go_back = Button(login_Frame, text="Next Part", command=part02).place(x=280, y=400)

        login_window.mainloop()
    
    def vacc_test_status():
        from main_menu import main_menu
        def return_prompt():
            login_window.destroy()
            main_menu.user_menu()

        return_prompt = partial(return_prompt)
    
        login_window = Tk()
        login_window.title("PyTracer Contact Tracing App")
        login_window.geometry('500x500')

        login_Frame = LabelFrame(login_window, text='Health Declaration Form (3/4)')
        login_Frame.pack(expand='yes', fill='both')
        first_label = Label(login_Frame , text= "Update your Information")
        first_label.place(x=175, y=30)
        second_label = Label(login_Frame, text="Part 03 of 04")
        second_label.place(x=205, y=50)
        question_1 = Label(login_Frame, text = "Where will you go today?").place(x = 40, y = 80)
        question_2 = Label(login_Frame, text = "When will you visit there?",).place(x = 40, y = 160)
        question_3 = Label(login_Frame, text = "When did you last go out with your friends?",).place(x = 40, y = 240)
        question_4 = Label(login_Frame, text="Where did you last went during that day?").place(x=40, y=320)

        first_a = StringVar()
        second_a = StringVar()
        third_a = StringVar()
        fourth_a = StringVar()
        def part02():
            health_check.contact_info()
        part02 = partial(part02)
        answer_01 = Entry(login_Frame,width = 40, textvariable=first_a)
        answer_01.place(x = 40, y = 120) 
        answer_02 = Entry(login_Frame, width = 40, textvariable=second_a)
        answer_02.place(x = 40,y = 200)
        answer_03 = Entry(login_Frame,width = 40, textvariable=third_a)
        answer_03.place(x = 40,y = 280)
        answer_04 = Entry(login_Frame,width = 40, textvariable=fourth_a)
        answer_04.place(x = 40,y = 360)

        go_back = Button(login_Frame, text="Go Back", command=return_prompt).place(x=140, y=400)
        go_back = Button(login_Frame, text="Next Part", command=part02).place(x=280, y=400)

        login_window.mainloop()

    def contact_info():
        from main_menu import main_menu
        def return_prompt():
            login_window.destroy()
            main_menu.user_menu()

        return_prompt = partial(return_prompt)
    
        login_window = Tk()
        login_window.title("PyTracer Contact Tracing App")
        login_window.geometry('500x500')

        login_Frame = LabelFrame(login_window, text='Health Declaration Form (4/4)')
        login_Frame.pack(expand='yes', fill='both')
        first_label = Label(login_Frame , text= "Update your Information")
        first_label.place(x=175, y=30)
        second_label = Label(login_Frame, text="Part 04 of 04")
        second_label.place(x=205, y=50)
        question_1 = Label(login_Frame, text = "Email:").place(x = 40, y = 80)
        question_2 = Label(login_Frame, text = "Contact Number:",).place(x = 40, y = 160)

        first_a = StringVar()
        second_a = StringVar()

        answer_01 = Entry(login_Frame,width = 40, textvariable=first_a)
        answer_01.place(x = 40, y = 120) 
        answer_02 = Entry(login_Frame, width = 40, textvariable=second_a)
        answer_02.place(x = 40,y = 200)

        go_back = Button(login_Frame, text="Go Back", command=return_prompt).place(x=140, y=240)
        go_back = Button(login_Frame, text="Next part").place(x=280, y=240)

        login_window.mainloop()