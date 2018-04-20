Sentimental reasons :)

import sqlite3
import dateutil
from dateutil.relativedelta import relativedelta, FR, MO, WE
from dateutil import parser
import datetime
from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import *

conn = sqlite3.connect("wsw.db")
c = conn.cursor()

MAIN_FONT = 'Helvetica', 12

#### CODE ####

# start date on mondey week before and week after the date
td = datetime.date.today()
print("Today: ", datetime.date.today())
start_date_before = datetime.date.today() + relativedelta(weekday=MO(-1))
print("Last Monday: ", start_date_before.strftime("%d-%m-%Y"))
start_date_after = datetime.date.today() + relativedelta(weekday=MO(+1))
print("Next Monday: ", start_date_after.strftime("%d-%m-%Y"))

# contract start date
start_date = "2017-01-31"  # input("Start date: ")
start_date = dateutil.parser.parse(start_date).strftime("%d-%m-%Y")
start_date = datetime.datetime.strptime(start_date, '%d-%m-%Y')

# contrat end date
contract_lenght = 365  # int(input("How long in days?: "))
contract_calculation = start_date + datetime.timedelta(days=contract_lenght) + relativedelta(weekday=FR)
contract_calculation.strftime("%d-%m-%Y")
print("end date on friday", contract_calculation)

# contract review date (two weeks before on wednesday)
contract_review_date = contract_calculation - relativedelta(weekday=WE(-3))
print("Review date is: ", contract_review_date)


#### END CODE ####

def raise_frame(frame):
    frame.tkraise()

img_path = 'logo.jpg'

root = Tk()
root.title("WSW Centre")
root.geometry("900x600+100+100")

#top frame with logo

f1 = Frame(root)

f2 = Frame(root)

f3 = Frame(root)

##### f4 - ADD NEW USER #####
f4 = Frame(root)
f4_lbl = Label(text="Dupa kurwa")
f4_lbl.grid(row=0, sticky='we', columnspan=5)

add_name = Label(f4, text="Name:")
add_name.grid(row=10, column=0, sticky="e")
add_name_entry = Entry(f4)
add_name_entry.grid(row=10, column=1)

add_surname = Label(f4, text="Surname:")
add_surname.grid(row=10, column=2, sticky="e")
add_surname_entry = Entry(f4)
add_surname_entry.grid(row=10, column=3)

add_birth_date = Label(f4, text="Birth Date:")
add_birth_date.grid(row=11, column=0, sticky="e")
add_birth_date_entry = Entry(f4)
add_birth_date_entry.grid(row=11, column=1)

add_gender = Label(f4, text="Gender:")
add_gender.grid(row=11, column=2, sticky="e")
add_gender_entry = Entry(f4)
add_gender_entry.grid(row=11, column=3)

add_nationality = Label(f4, text="Nationality:")
add_nationality.grid(row=12, column=0, sticky="e")
add_nationality_entry = Entry(f4)
add_nationality_entry.grid(row=12, column=1)

add_religion = Label(f4, text="Religion:")
add_religion.grid(row=12, column=2, sticky="e")
add_religion_entry = Entry(f4)
add_religion_entry.grid(row=12, column=3)

add_nino = Label(f4, text="NI No:")
add_nino.grid(row=13, column=0, sticky="e")
add_nino_entry = Entry(f4)
add_nino_entry.grid(row=13, column=1)

add_language = Label(f4, text="Language:")
add_language.grid(row=13, column=2, sticky="e")
add_language_entry = Entry(f4)
add_language_entry.grid(row=13, column=3)

add_marital = Label(f4, text="Marital Status:")
add_marital.grid(row=14, column=0, sticky="e")
add_marital_entry = Entry(f4)
add_marital_entry.grid(row=14, column=1)

add_disability = Label(f4, text="disability:")
add_disability.grid(row=14, column=2, sticky="e")
add_disability_entry = Entry(f4)
add_disability_entry.grid(row=14, column=3)

add_address = Label(f4, text="Adress:")
add_address.grid(row=10, column=4, sticky="w")
add_address_entry = Text(f4, height=3, width=30, font=MAIN_FONT)
add_address_entry.grid(row=11, column=4, columnspan=2, rowspan=3, padx=10)

add_postcode = Label(f4, text="Postcode:")
add_postcode.grid(row=14, column=4, sticky="w")
add_postcode_entry = Entry(f4)
add_postcode_entry.grid(row=14, column=5)

### >>>>> TOP END <<<<<<<
f4_lbl2 = Label(f4, text="Dupa kurwa huj cipa")
f4_lbl2.grid(row=15, sticky='we', columnspan=5)

add_email = Label(f4, text="Email:")
add_email.grid(row=16, column=0, sticky="e")
add_email_entry = Entry(f4)
add_email_entry.grid(row=16, column=1)

add_tel_no = Label(f4, text="Telephone No:")
add_tel_no.grid(row=16, column=2, sticky="e")
add_tel_no_entry = Entry(f4)
add_tel_no_entry.grid(row=16, column=3)

add_mob_no = Label(f4, text="Mobile No:")
add_mob_no.grid(row=17, column=0, sticky="e")
add_mob_no_entry = Entry(f4)
add_mob_no_entry.grid(row=17, column=1)

add_car_reg = Label(f4, text="Car Registration:")
add_car_reg.grid(row=17, column=2, sticky="e")
add_car_reg_entry = Entry(f4)
add_car_reg_entry.grid(row=17, column=3)

add_school_attended = Label(f4, text="School Attended:")
add_school_attended.grid(row=16, column=4, sticky="e")
add_school_attended_entry = Entry(f4)
add_school_attended_entry.grid(row=16, column=5)

add_specialised = Label(f4, text="Specialised:")
add_specialised.grid(row=17, column=4, sticky="e")
add_specialised_entry = Entry(f4)
add_specialised_entry.grid(row=17, column=5)
## kin ##
f4_lbl2 = Label(f4, text="Dupa kurwa huj cipa kromka z maslem")
f4_lbl2.grid(row=18, sticky='we', columnspan=5)

add_kin_name = Label(f4, text="Next/Kin Name:")
add_kin_name.grid(row=19, column=0, sticky="e")
add_kin_name_entry = Entry(f4)
add_kin_name_entry.grid(row=19, column=1)

add_kin_surname = Label(f4, text="Next/Kin Surname:")
add_kin_surname.grid(row=20, column=0, sticky="e")
add_kin_surname_entry = Entry(f4)
add_kin_surname_entry.grid(row=20, column=1)

add_kin_relationship = Label(f4, text="Next/Kin Relationship:")
add_kin_relationship.grid(row=21, column=0, sticky="e")
add_kin_relationship_entry = Entry(f4)
add_kin_relationship_entry.grid(row=21, column=1)

add_kin_address = Label(f4, text="Next/Kin Address:")
add_kin_address.grid(row=19, column=4, sticky="e")
add_kin_address_entry = Text(f4, height=3, width=30, font=MAIN_FONT)
add_kin_address_entry.grid(row=20, column=4, columnspan=2, rowspan=3)

add_kin_postcode = Label(f4, text="Next/Kin Postcode:")
add_kin_postcode.grid(row=22, column=2, sticky="e")
add_kin_postcode_entry = Entry(f4)
add_kin_postcode_entry.grid(row=22, column=3)

add_kin_telno = Label(f4, text="Next/Kin Telephone:")
add_kin_telno.grid(row=19, column=2, sticky="e")
add_kin_telno_entry = Entry(f4)
add_kin_telno_entry.grid(row=19, column=3)

add_kin_mobno = Label(f4, text="Next/Kin Mobile No:")
add_kin_mobno.grid(row=20, column=2, sticky="e")
add_kin_mobno_entry = Entry(f4)
add_kin_mobno_entry.grid(row=20, column=3)

add_kin_email = Label(f4, text="Next/Kin Email:")
add_kin_email.grid(row=21, column=2, sticky="e")
add_kin_email_entry = Entry(f4)
add_kin_email_entry.grid(row=21, column=3)

## GP ##
f4_lbl2 = Label(f4, text="Dupa kurwa huj cipa kromka z maslem i serem")
f4_lbl2.grid(row=23, sticky='we', pady=10, columnspan=5)


add_gp_name = Label(f4, text="GP Name:")
add_gp_name.grid(row=24, column=0, sticky="e")
add_gp_name_entry = Entry(f4)
add_gp_name_entry.grid(row=24, column=1)

add_gp_surname = Label(f4, text="GP Surname:")
add_gp_surname.grid(row=25, column=0, sticky="e")
add_gp_surname_entry = Entry(f4)
add_gp_surname_entry.grid(row=25, column=1)

add_gp_organisation = Label(f4, text="Surgery Name:")
add_gp_organisation.grid(row=26, column=0, sticky="e")
add_gp_organisation_entry = Entry(f4)
add_gp_organisation_entry.grid(row=26, column=1)

add_gp_address = Label(f4, text="Surgery Address:")
add_gp_address.grid(row=24, column=2, sticky="e")
add_gp_address_entry = Text(f4, height=3, width=30, font=MAIN_FONT)
add_gp_address_entry.grid(row=25, column=2, columnspan=2, rowspan=3)

add_gp_postcode = Label(f4, text="Surgery Postcode:")
add_gp_postcode.grid(row=27, column=0, sticky="e")
add_gp_postcode_entry = Entry(f4)
add_gp_postcode_entry.grid(row=27, column=1)

add_gp_telno = Label(f4, text="Surgery Telephone No:")
add_gp_telno.grid(row=27, column=0, sticky="e")
add_gp_telno_entry = Entry(f4)
add_gp_telno_entry.grid(row=27, column=1)
f4_lbl2 = Label(f4, text=" ")
f4_lbl2.grid(row=28, sticky='we', pady=10)
add_personal_circumstances = Label(f4, text="Personal Circumstances:")

add_personal_circumstances.grid(row=29, column=0, sticky="e")
add_personal_circumstances_entry = Text(f4, height=10, width=100)
add_personal_circumstances_entry.grid(row=30, column=0, columnspan=5)

'''

gp_telno
personal_circumstances
contract
contract_sd
contract_ed
'''

menu = Menu(root)
file_menu = Menu(menu)
file_menu.add_command(label="Home", command=lambda: raise_frame(f1))
file_menu.add_command(label="Open")
file_menu.add_command(label="Quit")
menu.add_cascade(label="File", menu=file_menu)

users_menu = Menu(menu)
users_menu.add_command(label="Add", command=lambda: raise_frame(f4))
menu.add_cascade(label="Users", menu=users_menu)

root.config(menu=menu)

for frame in (f1, f2, f3, f4):
    frame.grid(row=20, column=0, sticky='news')

#Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
#Label(f1, text='FRAME 1').pack()

#Label(f2, text='FRAME 2').pack()
#Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

#Label(f3, text='FRAME 3').pack(side='left')
#Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

#Label(f4, text='FRAME 4').pack()
#Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()

raise_frame(f1)
root.mainloop()




def progz():


    # start date on mondey week before and week after the date
    td = datetime.date.today()
    print("Today: ", datetime.date.today())
    start_date_before = datetime.date.today() + relativedelta(weekday=MO(-1))
    print("Last Monday: ", start_date_before.strftime("%d-%m-%Y"))
    start_date_after = datetime.date.today() + relativedelta(weekday=MO(+1))
    print("Next Monday: ", start_date_after.strftime("%d-%m-%Y"))

    # contract start date
    start_date = "2017-01-31"  # input("Start date: ")
    start_date = dateutil.parser.parse(start_date).strftime("%d-%m-%Y")
    start_date = datetime.datetime.strptime(start_date, '%d-%m-%Y')

    # contrat end date
    contract_lenght = 365  # int(input("How long in days?: "))
    contract_calculation = start_date + datetime.timedelta(days=contract_lenght) + relativedelta(weekday=FR)
    contract_calculation.strftime("%d-%m-%Y")
    print("end date on friday", contract_calculation)

    # contract review date (two weeks before on wednesday)
    contract_review_date = contract_calculation - relativedelta(weekday=WE(-3))
    print("Review date is: ", contract_review_date)

    ##########

    root = Tk()
    root.geometry("650x300")
    # root.option_add("*Font", "helvetica 12")

    menu = Menu(root)
    root.config(menu=menu)
    file_menu = Menu(menu)
    file_menu.add_command(label="Quit")
    menu.add_cascade(label="File", menu=file_menu)

    help_menu = Menu(menu)
    help_menu.add_command(label="Help")
    menu.add_cascade(label="Help", menu=help_menu)

    ################################ END OF MENU ##############
    label1 = Label(root, text=" ").grid(row=0, sticky='w')
    label2 = Label(root, text="Todays date:").grid(row=1, sticky='e', padx=10)
    label3 = Label(root, text="Monday before:").grid(row=1, column=3, sticky='e', padx=10)
    label4 = Label(root, text="Monday after: ").grid(row=2, column=3, sticky='e', padx=10)

    label6 = Label(root, text="Contract Start Date: ").grid(row=6, sticky='e', padx=10, pady=10)
    start_date_btn = Button(text="Add Date").grid(row=6, column=2, columnspan=3, sticky='w', pady=10)

    e_today = Entry(root)
    e_today.insert(END, td)

    e_mon_before = Entry(root)
    e_mon_before.insert(END, start_date_before)

    e_mon_after = Entry(root)
    e_mon_after.insert(END, start_date_after)

    e_start_date = Entry(root)

    e_today.grid(row=1, column=1)
    e_mon_before.grid(row=1, column=4)
    e_mon_after.grid(row=2, column=4)
    e_start_date.grid(row=6, column=1, pady=10)

    root.mainloop()
