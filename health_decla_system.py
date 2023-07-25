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
        question_4 = Label(login_Frame, text="Where did you last made contact during that day?").place(x=40, y=320)

        first_a = StringVar()
        second_a = StringVar()
        third_a = StringVar()
        fourth_a = StringVar()

        def part02():
            login_window.destroy()
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
        def return_prompt():
            login_window.destroy()
            health_check.locate_info()

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
        question_2 = Label(login_Frame, text = "Have you come into contact with someone experiencing any of the symptoms?",).place(x = 40, y = 250)

        first_a = StringVar()
        second_a = StringVar()
        third_a = StringVar()
        fourth_a = StringVar()
        def part02():
            login_window.destroy()
            health_check.vacc_test_status()
        part02 = partial(part02)
        symp01 = Checkbutton(login_Frame, text="Shortness of Breath")
        symp01.place(x=40, y=100)
        symp02 = Checkbutton(login_Frame, text="High Fever")
        symp02.place(x=40, y=120)
        symp03 = Checkbutton(login_Frame, text="Diarrhea")
        symp03.place(x=40, y=140)
        symp04 = Checkbutton(login_Frame, text="Fatigue")
        symp04.place(x=40, y=160)
        symp05 = Checkbutton(login_Frame, text="Body/muscle pain")
        symp05.place(x=40, y=180)
        symp06 = Checkbutton(login_Frame, text="runny nose")
        symp06.place(x=40, y=200)
        symp07 = Checkbutton(login_Frame, text="Cough")
        symp07.place(x=300, y=100)
        symp08 = Checkbutton(login_Frame, text="Nausea/Vomiting")
        symp08.place(x=300, y=120)
        symp09 = Checkbutton(login_Frame, text="Headache")
        symp09.place(x=300, y=140)
        symp10 = Checkbutton(login_Frame, text="Sore Throat")
        symp10.place(x=300, y=160)
        symp11 = Checkbutton(login_Frame, text="Loss of senses (taste/smell)")
        symp11.place(x=300, y=180)
        
        made_contact = Radiobutton(login_Frame, text='Yes', value='symptom_contact', indicatoron=False)
        made_contact.place(x=140, y=290)
        no_contact = Radiobutton(login_Frame, text='No', value='made_symptom_contact', indicatoron=False)
        no_contact.place(x=280, y=290)
        go_back = Button(login_Frame, text="Go Back", command=return_prompt).place(x=140, y=370)
        go_back = Button(login_Frame, text="Next Part", command=part02).place(x=280, y=370)

        login_window.mainloop()
    
    def vacc_test_status():
        def return_prompt():
            login_window.destroy()
            health_check.symptom_check()

        return_prompt = partial(return_prompt)
    
        login_window = Tk()
        login_window.title("PyTracer Contact Tracing App")
        login_window.geometry('500x450')

        login_Frame = LabelFrame(login_window, text='Health Declaration Form (3/4)')
        login_Frame.pack(expand='yes', fill='both')
        first_label = Label(login_Frame , text= "Update your Information")
        first_label.place(x=175, y=30)
        second_label = Label(login_Frame, text="Part 03 of 04")
        second_label.place(x=205, y=50)
        question_1 = Label(login_Frame, text = "Vaccination Status:").place(x = 40, y = 80)
        # first dose, second dose, booster, 2nd booster,  unvaccinated
        question_2 = Label(login_Frame, text = "Have you been tested for <insert Disease here>?",).place(x = 40, y = 170)
        #No, Yes-Pending, Yes-Negative, Yes-Positive
        question_3 = Label(login_Frame, text = "Have you been in contact with someone who's a probable/confirmed case?",).place(x = 40, y = 260)

        vacc_choice = StringVar()
        tester_choice = StringVar()
        third_a = StringVar()

        vacc_choice.set("choose from dropdown...")
        tester_choice.set("choose from dropdown...")
        def part02():
            login_window.destroy()
            health_check.contact_info()
        part02 = partial(part02)

        vacc_choices = [
            "unvaccinated",
            'first dose',
            'second dose (Fully Vaccinated)',
            "First Booster",
            "Second Booster"
        ]

        test_choices =[
            "No",
            "Yes-Pending",
            "Yes-Negative",
            "Yes-Positive"
        ]
        vacc_status = OptionMenu(login_Frame, vacc_choice, *vacc_choices)
        vacc_status.place(x=40, y=120)
        test_status = OptionMenu(login_Frame,  tester_choice, *test_choices)
        test_status.place(x=40, y=210)
        made_contact = Radiobutton(login_Frame, text='Yes', value='close_contact',indicatoron=False)
        made_contact.place(x=140, y=300)
        no_contact = Radiobutton(login_Frame, text='No', value='no_close_contact',indicatoron=False)
        no_contact.place(x=280, y=300)
        go_back = Button(login_Frame, text="Go Back", command=return_prompt).place(x=140, y=380)
        go_back = Button(login_Frame, text="Next Part", command=part02).place(x=280, y=380)

        login_window.mainloop()

    def contact_info():
        def return_prompt():
            login_window.destroy()
            health_check.vacc_test_status()

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
        question_1 = Label(login_Frame, text = "Name:").place(x = 40, y = 80)
        question_2 = Label(login_Frame, text = "Contact Number",).place(x = 40, y = 160)
        question_3 = Label(login_Frame, text = "Email:",).place(x = 40, y = 240)
        first_a = StringVar()
        second_a = StringVar()
        third_a = StringVar()

        answer_01 = Entry(login_Frame,width = 40, textvariable=first_a)
        answer_01.place(x = 40, y = 120) 
        answer_02 = Entry(login_Frame, width = 40, textvariable=second_a)
        answer_02.place(x = 40,y = 200)
        answer_03 = Entry(login_Frame,width = 40, textvariable=third_a)
        answer_03.place(x = 40,y = 280)

        go_back = Button(login_Frame, text="Go Back", command=return_prompt).place(x=140, y=400)
        go_back = Button(login_Frame, text="Next Part").place(x=280, y=400)

        login_window.mainloop()