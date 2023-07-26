from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Label, LabelFrame
from functools import partial
import datetime

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

        def part02(ans01, ans02, ans03, ans04):
            ans01 = first_a.get()
            ans02 = second_a.get()
            ans03 = third_a.get()
            ans04 = fourth_a.get()
            login_window.destroy()
            health_check.hdf_make(ans01, ans02, ans03, ans04)
            health_check.symptom_check()

        part02 = partial(part02, first_a, second_a, third_a, fourth_a)
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

        first_a = IntVar()
        second_a = IntVar()
        third_a = IntVar()
        fourth_a = IntVar()
        fifth = IntVar()
        sixth = IntVar()
        seventh = IntVar()
        eighth = IntVar()
        ninth = IntVar()
        tenth = IntVar()
        eleventh = IntVar()
        twelth = IntVar()
        didcontact = StringVar(login_Frame, "1")

        def part02(doot1, doot2, doot3, doot4, doot5, doot6, doot7, doot8, doot9, doot10, doot11, doot12, constat):
            doot1 = first_a.get()
            doot2 = second_a.get()
            doot3 = third_a.get()
            doot4 = fourth_a.get()
            doot5 = fifth.get()
            doot6 = sixth.get()
            doot7 = seventh.get()
            doot8 = eighth.get()
            doot9 = ninth.get()
            doot10 = tenth.get()
            doot11 = eleventh.get()
            doot12 = twelth.get()
            constat = didcontact.get()

            symptomlist = []

            if doot1 == 1:
                symptomlist.append("Shortness of Breath")
            if doot2 == 1:
                symptomlist.append("High Fever")
            if doot3 == 1:
                symptomlist.append("Diarrhea")
            if doot4 == 1:
                symptomlist.append("Fatigue")
            if doot5 == 1:
                symptomlist.append("Body or Muscle Pain")
            if doot6 == 1:
                symptomlist.append("Runny Nose")
            if doot7 == 1:
                symptomlist.append("Coughing")
            if doot8 == 1:
                symptomlist.append("Nausea/Vomiting")
            if doot9 == 1:
                symptomlist.append("Headache")
            if doot10 == 1:
                symptomlist.append("Sore Throat")
            if doot11 == 1:
                symptomlist.append("Lost of Sense of Taste or Smell")
            if doot12 == 1:
                symptomlist.append("Does not have any of the symptoms Listed")
            
            login_window.destroy()
            sympcheck_stat = health_check.symptom_hdf(symptomlist, constat)
            health_check.vacc_test_status(sympcheck_stat)

        part02 = partial(part02, first_a, second_a, third_a, fourth_a, fifth, sixth, seventh, eighth, ninth, tenth, eleventh, twelth, didcontact)
        symp01 = Checkbutton(login_Frame, text="Shortness of Breath", variable=first_a, offvalue=0, onvalue=1)
        symp01.place(x=40, y=100)
        symp02 = Checkbutton(login_Frame, text="High Fever", variable=second_a, offvalue=0, onvalue=1)
        symp02.place(x=40, y=120)
        symp03 = Checkbutton(login_Frame, text="Diarrhea", variable=third_a, offvalue=0, onvalue=1)
        symp03.place(x=40, y=140)
        symp04 = Checkbutton(login_Frame, text="Fatigue",variable=fourth_a, offvalue=0, onvalue=1)
        symp04.place(x=40, y=160)
        symp05 = Checkbutton(login_Frame, text="Body/muscle pain", variable=fifth, offvalue=0, onvalue=1)
        symp05.place(x=40, y=180)
        symp06 = Checkbutton(login_Frame, text="runny nose", variable=sixth, offvalue=0, onvalue=1)
        symp06.place(x=40, y=200)
        symp07 = Checkbutton(login_Frame, text="Cough", variable=seventh, offvalue=0, onvalue=1)
        symp07.place(x=300, y=100)
        symp08 = Checkbutton(login_Frame, text="Nausea/Vomiting", variable=eighth, offvalue=0, onvalue=1)
        symp08.place(x=300, y=120)
        symp09 = Checkbutton(login_Frame, text="Headache", variable=ninth, offvalue=0, onvalue=1)
        symp09.place(x=300, y=140)
        symp10 = Checkbutton(login_Frame, text="Sore Throat",variable=tenth, offvalue=0, onvalue=1)
        symp10.place(x=300, y=160)
        symp11 = Checkbutton(login_Frame, text="Loss of senses (taste/smell)",variable=eleventh, offvalue=0, onvalue=1)
        symp11.place(x=300, y=180)
        symp12 = Checkbutton(login_Frame, text="none of the above",variable=twelth, offvalue=0, onvalue=1)
        symp12.place(x=300, y=200)
        
        made_contact = Radiobutton(login_Frame, text='Yes', value='symptom_contact', indicatoron=False, variable=didcontact)
        made_contact.place(x=140, y=290)
        no_contact = Radiobutton(login_Frame, text='No', value='no_symptom_contact', indicatoron=False, variable=didcontact)
        no_contact.place(x=280, y=290)
        go_back = Button(login_Frame, text="Next Part", command=part02).place(x=280, y=370)

        login_window.mainloop()
    
    def vacc_test_status(sympcheck_stat):
    
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
        def part02(vaccchoice,testerchoice,yesno):
            vaccchoice = vacc_choice.get()
            testerchoice = tester_choice.get()
            yesno = third_a.get()
            login_window.destroy()
            testcheckstat = health_check.vacc_hdf(sympcheck_stat, vaccchoice, testerchoice, yesno)
            health_check.contact_info(testcheckstat)
        part02 = partial(part02, vacc_choice, tester_choice, third_a)

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
        made_contact = Radiobutton(login_Frame, text='Yes', value='close_contact',indicatoron=False, variable=third_a)
        made_contact.place(x=140, y=300)
        no_contact = Radiobutton(login_Frame, text='No', value='no_close_contact',indicatoron=False, variable=third_a)
        no_contact.place(x=280, y=300)
        go_back = Button(login_Frame, text="Next Part", command=part02).place(x=280, y=380)

        login_window.mainloop()

    def contact_info(sympcheck_stat):
    
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

        def finisher(name, email, number):
            from main_menu import main_menu
            name = first_a.get()
            number = second_a.get()
            email =  third_a.get()
            login_window.destroy()
            finalstat = health_check.wrapup(sympcheck_stat, name, email, number)
            if finalstat == False:
                messagebox.showinfo("HDF Created", "HDF Created.\nRESULT: PASS\n\nYou are cleared to go to your next destination.\nRemember to wear your Face mask and observe proper social distancing!\nAlways disinfect when leaving/going home.\n\nThank you for using PyTracer! You may get your HDF at the HDF_generations folder.")
            if finalstat == True:
                messagebox.showinfo("HDF Created", "HDF Created.\nRESULT: FAIL\n\nYou are advised to remain at home and self-isolate. Do not make contact with anyone.\nWear Face Mask, and disinfect the isolation area, and get tested.\n\nThank you for using PyTracer! You may get your HDF at the HDF_generations folder.")
            main_menu.user_menu()
        finisher = partial(finisher, first_a, second_a, third_a)

        answer_01 = Entry(login_Frame,width = 40, textvariable=first_a)
        answer_01.place(x = 40, y = 120) 
        answer_02 = Entry(login_Frame, width = 40, textvariable=second_a)
        answer_02.place(x = 40,y = 200)
        answer_03 = Entry(login_Frame,width = 40, textvariable=third_a)
        answer_03.place(x = 40,y = 280)

        go_back = Button(login_Frame, text="Finish", command=finisher)
        go_back.place(x=280, y=400)

        login_window.mainloop()

    def hdf_make(answer_01, answer_02, answer_03, answer_04):
        import os
        path = "HDF_generations"
        if not os.path.exists(path):
            print("this doesn't exist :/")
            os.makedirs(path)
        # create file:
        with open(os.path.join(path, "My_records.txt"),'a') as new_hdf:
            new_hdf.write("==============================Health Declaration Form==============================")
            new_hdf.write("\n\n-Part 01: Travel Information-")
            new_hdf.write("\nNext Destination: " + answer_01 + "\n")
            new_hdf.write("Date of Travel: " + answer_02 + "\n")
            new_hdf.write("Recent Destination: " + answer_04 + "\n")
            new_hdf.write("Date of Last Travel: " + answer_03 + "\n")
            new_hdf.close()
    
    def symptom_hdf(symptoms,constat):
        
        donotgo = True

        if "Does not have any of the symptoms Listed" in symptoms:
            donotgo = False
        if  "Shortness of Breath" in symptoms and "Fatigue" in symptoms and "Body or Muscle Pain" in symptoms:
            donotgo = True
        if  len(symptoms) <= 5:
            donotgo = False
        if constat == "symptom_contact":
            donotgo = False
        
        with open("./HDF_generations/My_records.txt", 'a') as new_hdf:
            new_hdf.write("\n\n-Part 02: List of Symptoms-\n")
            for items in symptoms:
                new_hdf.write("\n= " + items)

            if constat == "symptom_contact":
                new_hdf.write("\n>USER HAS MADE CONTACT WITH SOMEONE EXPERIENCING SYMPTOMS OF COVID-19")
            if  constat == "no_symptom_contact":
                new_hdf.write("\n>User has not made contact with someone experiencing symptoms of COVID-19")

            if donotgo == True:
                new_hdf.write("\n\nSymptomCheck System Results: FAIL")
            if donotgo == False:
                new_hdf.write("\n\nSymptomCheck System Results: PASS")
            new_hdf.close()
        
        return donotgo
    
    def vacc_hdf(sympcheck_stat, vaccchoice, testerchoice, yesno):

        if testerchoice == "Yes-Positive" or testerchoice == "Yes-Pending":
            sympcheck_stat = True
        if yesno == "close_contact":
            sympcheck_stat = True
        
        with open("./HDF_generations/My_records.txt", 'a') as new_hdf:
            new_hdf.write("\n\n-Part 03: Vaccination and Test Status-")
            new_hdf.write("\nVaccination Status: " + vaccchoice)
            new_hdf.write("\nHas this user tested for COVID: " + testerchoice)
            if yesno == "no_close_contact":
                new_hdf.write("\n>This user did not made contact with anyone who has a probable/confirmed case\n\n")
            if yesno == "close_contact":
                new_hdf.write("\nTHIS USER HAS MADE CONTACT WITH SOMEONE WHO HAS A CONFIRMED/PROBABLE CASE\n\n")
            if  sympcheck_stat == False:
                new_hdf.write("TestCheck System Results: PASS")
            if sympcheck_stat == True:
                new_hdf.write("TestCheck System Results: FAIL")
            new_hdf.close()
        return sympcheck_stat
    
    def wrapup(sympcheck_stat, name, email, number):
        import os

        with open("./HDF_generations/My_records.txt", 'a') as new_hdf:
            new_hdf.write("\n\n-Part 04: Contact Details-")
            new_hdf.write("\nName: " + name)
            new_hdf.write("\nContact Number: " + number)
            new_hdf.write("\nEmail: " + email)

            if sympcheck_stat == False:
                new_hdf.write("\n\n=====RESULTS OF HDF=====\n\n")
                new_hdf.write("Result: PASS\n\nYou are cleared to go to your next destination.\nRemember to wear your Face mask and observe proper social distancing!\nAlways disinfect when leaving/going home.")
            if sympcheck_stat == True:
                new_hdf.write("\n\n=====RESULTS OF HDF=====\n\n")
                new_hdf.write("Result: FAIL\n\nYou are advised to remain at home and self-isolate. Do not make contact with anyone.\nWear Face Mask, and disinfect the isolation area, and get tested.")
            new_hdf.write("\n\n========================\nThis is an autogenerated Health Declaration Form by PyTracer Contact Tracing App.\nStay Safe and get vaccinated!\n")
            import datetime
            day = datetime.datetime.now()
            date_created = day.strftime('%c')
            new_hdf.print("HDF Generated on: " + date_created)
            new_hdf.close()

        mydate = datetime.datetime.now()
        year = mydate.strftime('%Y')
        day = mydate.strftime('%j')
        hour = mydate.strftime('%H')
        minute = mydate.strftime('%M')
        new_name = name + '-' + year + '-' + day + '-' + hour + '-' + minute + '.txt'
        os.rename("./HDF_generations/My_records.txt",  os.path.join('./HDF_generations', new_name))
        return sympcheck_stat
