"""
LOGIN: admin
PASS: 

Some code was removed
"""

import tkinter.ttk as ttk
import sqlite3
from dateutil import relativedelta, parser
from dateutil.relativedelta import relativedelta, FR, MO, weekday
import datetime
from tkinter import *
from PIL import Image,ImageTk

MAIN_FONT = 'Helvetica', 12

conn = sqlite3.connect("wsw-contract.db")
c =  conn.cursor()

today = datetime.datetime.today()
#print(today)

### ### ###
### ### ###

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS contracts(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name VARCHAR(20), surname VARCHAR(20), contract_sd DATE, contract_ed DATE, contract_lenght INTEGER, birth_date DATE, to_birthdays INTEGER)")
    print ("DB has been created")

def insert_db_data(*input_data):
    c.execute("INSERT INTO contracts(name, surname, contract_sd, contract_ed, contract_lenght, birth_date, to_birthdays) VALUES (?,?,?,?,?,?,?)",(input_data))
    conn.commit()
    print("Data has been inserted")

def input_data():

    inp_data = []

    name = input("Name: ")
    surname = input("Surname: ")
    start_date = parser.parse(input("Start Date: ")).strftime("%d-%m-%Y")
    start_date_convert = datetime.datetime.strptime(start_date, "%d-%m-%Y")

    start_date_convert_str = start_date_convert.strftime("%d-%m-%Y")

    contract_lenght = int(input("Contract lenght in days: "))
    end_date = start_date_convert + datetime.timedelta(days=contract_lenght) + relativedelta(weekday=FR)

    end_date_str = end_date.strftime("%d-%m-%Y")

    birth_date = parser.parse(input("Birth Date: ")).strftime("%d-%m-%Y")
    birth_date = datetime.datetime.strptime(birth_date, "%d-%m-%Y").strftime("%d-%m-%Y")
    to_birthdays = 365

    for i in (name, surname, start_date_convert_str, contract_lenght, end_date_str, birth_date, to_birthdays):
        if start_date_convert:
            inp_data.append(i)

    insert_db_data(*inp_data)

def read_db():
    c.execute("SELECT * FROM contracts")

    data = c.fetchall()

    for rows in data:
        print (rows[0], rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7])


#### GUI ####

class Users(object):

    def __init__(self, name):
        self.name = name

    def printName(self):
        return ("Hello again, {0}".format(self.name))

class MyGui(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self, bg="white")

        menu = Menu(self)
        self.config(menu=menu)
        file_menu = Menu(menu)
        file_menu.add_command(label="Home", command=lambda: self.show_frame(StartPage))
        file_menu.add_separator()
        file_menu.add_command(label="Quit")
        menu.add_cascade(label="File", menu = file_menu)

        users_menu = Menu(menu)
        users_menu.add_command(label="Add", command=lambda: self.show_frame(Users_Add))
        menu.add_cascade(label="Users", menu= users_menu)

        container.pack(side='top', fill='both', expand='true')

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Users_Add, HelpPage):

            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew", pady=15, padx=10)

        self.show_frame(StartPage)

        status_bar = Label(self, text="Status:", relief=SUNKEN, anchor="w")
        status_bar.pack(side="bottom", fill='x')

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(Frame, Tk):
    def __init__(self, parent, controller):
        LabelFrame.__init__(self, parent, text="Info", padx=10, pady=10, bg="white", font=MAIN_FONT)

        ### TOP LEFT FRAME BEGIN ###
        startpage_top_left_frame = LabelFrame(self, bd=2, text="Statistics:", bg="white", width=50)
        #startpage_top_left_frame.config(highlightbackground="black", highlightcolor='black', highlightthickness=1)
        startpage_top_left_frame.grid(row=0, padx=10, pady=10)
        #label222 = Label(startpage_top_left_frame, text="TOP", width=52).grid(row=0)

        ###=== WELC MSG USERS NUMBER ===###
        c.execute("SELECT COUNT(id) FROM contracts")
        welc_msg_howmanyusers = c.fetchall()
        #=================================#

        ###=== NEWEST MEMBER ===###
        c.execute("SELECT name, contract_sd FROM contracts ORDER BY contract_sd DESC")
        welc_msg_newest = c.fetchall()
        #=========================#

        ###=== Birthday ===###
        c.execute("SELECT name, birth_date FROM contracts ORDER BY contract_sd ASC")
        welc_msg_birthday = c.fetchall()

        welc_msg_birthday = datetime.datetime.strptime(welc_msg_birthday[0][1], "%d-%m-%Y")

        #=====
        try:
            next_birthday = welc_msg_birthday.replace(year=today.year)
        except ValueError:
            # oops, not a leapyear this year, no february 29th; use the day before
            next_birthday = welc_msg_birthday.replace(day=28, year=today.year)

        if next_birthday < today:  # already passed this year, pick next year
            try:
                next_birthday = welc_msg_birthday.replace(year=today.year + 1)
            except ValueError:
                # oops, not a leapyear next year, no february 29th, use the day before
                next_birthday = welc_msg_birthday.replace(day=28, year=today.year + 1)

        difference = next_birthday - today
        months, days = divmod(difference.days, 30)  # assume 30 days per month
        print('Your birthday is in about {} months and {} days'.format(months, days))

        # =========================#

        welc_msg = StringVar()
        welcome_message = Label(startpage_top_left_frame, textvariable=welc_msg, font=MAIN_FONT, wraplength=450).grid(row=0)
        welc_msg.set("Welcome back! \n\nWe have {0} users in our database. Our newest member is {1} who joined the workshop on {2}. (IMIE KURWA) has birthday on (DATA KURWA) dasdakjsdkajskd kasjdkjaskdjkasj kasdjkasj dkajskdjak jaksdjkasjdkjakdja jaksdjkasjdkajs ajskdjaskdjkasjk ajksdjaskdjkasjdkj akdsjkasjdka".format(welc_msg_howmanyusers[0][0], welc_msg_newest[0][0], welc_msg_newest[0][1]))

        ### TOP LEFT FRAME END ###

        ### TOP RIGHT FRAME BEGIN ###
        startpage_top_right_frame = LabelFrame(self, bd=2, text="Dates", bg="white")
        #startpage_top_right_frame.config(highlightbackground="black", highlightcolor='black', highlightthickness=1)
        startpage_top_right_frame.grid(row=0, column=1, padx=10, pady=10)

        def today_date_func():
            todays_date_label = Label(startpage_top_right_frame, text="Todays Date:", bg="white", width=15)
            todays_date_label.grid(row=0, column=0)
            todays_date_var = StringVar()
            todays_date_entry = Entry(startpage_top_right_frame, textvariable=todays_date_var)
            todays_date_entry.grid(row=0, column=1)
            todays_date_var.set(today.strftime("%d-%m-%Y"))

        today_date_func()

        def last_mon_date_func():
            last_mon_date_label = Label(startpage_top_right_frame, text="Last Monday:", bg="white")
            last_mon_date_label.grid(row=2, column=0)
            last_mon_date_date_var = StringVar()
            last_mon_date_date_entry = Entry(startpage_top_right_frame, textvariable=last_mon_date_date_var)
            last_mon_date_date_entry.grid(row=2, column=1)
            last_mon_date_check = (today - relativedelta(weekday=MO(-1))).strftime("%d-%m-%Y")

            if last_mon_date_check == today:
                last_mon_date_date_var.set((today - relativedelta(weekday=MO(-1))).strftime("%d-%m-%Y"))
            else:
                last_mon_date_date_var.set((today - relativedelta(weekday=MO(-1))).strftime("%d-%m-%Y"))

        last_mon_date_func()

        def next_monday_date_func():
            next_mon_date_label = Label(startpage_top_right_frame, text="Next Monday:", bg="white")
            next_mon_date_label.grid(row=3, column=0)
            next_mon_date_date_var = StringVar()
            next_mon_date_date_entry = Entry(startpage_top_right_frame, textvariable=next_mon_date_date_var)
            next_mon_date_date_entry.grid(row=3, column=1)
            next_mon_date_date_check = ((today - relativedelta(weekday=MO(+1))).strftime("%d-%m-%Y"))

            if next_mon_date_date_check == today:
                next_mon_date_date_var.set((today - relativedelta(weekday=MO(+2))).strftime("%d-%m-%Y"))
            else:
                next_mon_date_date_var.set((today - relativedelta(weekday=MO(+1))).strftime("%d-%m-%Y"))

        next_monday_date_func()

        def last_friday_date_func():
            last_friday_date_label = Label(startpage_top_right_frame, text="Last Friday:", bg="white")
            last_friday_date_label.grid(row=4, column=0)
            last_friday_date_date_var = StringVar()
            last_friday_date_date_entry = Entry(startpage_top_right_frame, textvariable=last_friday_date_date_var)
            last_friday_date_date_entry.grid(row=4, column=1)
            last_friday_date_date_check = ((today - relativedelta(weekday=FR(-1))).strftime("%d-%m-%Y"))

            if last_friday_date_date_check == today:
                last_friday_date_date_var.set((today - relativedelta(weekday=FR(-2))).strftime("%d-%m-%Y"))
            else:
                last_friday_date_date_var.set((today - relativedelta(weekday=FR(-1))).strftime("%d-%m-%Y"))

        last_friday_date_func()

        def next_friday_date_func():
            next_friday_date_label = Label(startpage_top_right_frame, text="Next Friday:", bg="white")
            next_friday_date_label.grid(row=5, column=0)
            next_friday_date_date_var = StringVar()
            next_friday_date_date_entry = Entry(startpage_top_right_frame, textvariable=next_friday_date_date_var)
            next_friday_date_date_entry.grid(row=5, column=1)
            next_friday_date_date_check = ((today - relativedelta(weekday=FR(+1))).strftime("%d-%m-%Y"))

            if next_friday_date_date_check == today:
                next_friday_date_date_var.set((today - relativedelta(weekday=FR(+2))).strftime("%d-%m-%Y"))
            else:
                next_friday_date_date_var.set((today - relativedelta(weekday=FR(+1))).strftime("%d-%m-%Y"))

        next_friday_date_func()

        ### TOP RIGHT FRAME BEGIN ###

        ### CENTRAL FRAME BEGIN ###
        startpage_central_frame = LabelFrame(self, bd=2, text="InfoTab", bg="white")
        startpage_central_frame.grid(row=1, columnspan=2, padx=10, pady=10)

        def table():
            query = "SELECT * FROM contracts LIMIT 5"
            c.execute(query)
            data = c.fetchall()
            tree = ttk.Treeview(startpage_central_frame)

            for rows in data:
                tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")
                tree.column("#0", width=0)
                tree.column("1", width=30)
                tree.column("2", width=100)
                tree.column("3", width=100)
                tree.column("4", width=100)
                tree.column("5", width=100)
                tree.column("6", width=100)
                tree.column("7", width=100)
                tree.column("8", width=100)
                tree.heading("1", text="ID")
                tree.heading("2", text="Name")
                tree.heading("3", text="Surname")
                tree.heading("4", text="Start Date")
                tree.heading("5", text="Days Left")
                tree.heading("6", text="End Date")
                tree.heading("7", text="Birth Date")
                tree.heading("8", text="Days Left")
                tree.insert("", rows[0],
                            values=(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7]))
                tree.grid(row=0)
        table()
        ### CENTRAL FRAME END ###

class HelpPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Help Page")
        label.grid(row=1)

class Users_Add(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Add New User")
        label.grid(row=0)

def main_app():
    app = MyGui()
    app.title("WSW Centre")
    app.geometry("810x500+200+200")
    app.mainloop()

def loginPage():
    root2 = Tk()
    root_frame = LabelFrame(pady=10)
    root_frame.config(bg="white", pady=10, padx=10)
    root_frame.pack()
    logo_small = ''

    label_logo = Label(root_frame, image=logo_small).pack(side='top')

    label = Label(root_frame, text="Login Form", bg="white", font=('Helvetica', 12, 'bold'))
    label.pack(side='top', pady=20, fill='both', expand='yes')


    label_login = Label(root_frame, fg="#000000", bg="white", text="Login:", font=MAIN_FONT)
    label_login.pack(side='top')
    login1 = StringVar()
    login_entry = Entry(root_frame, textvariable=login1, font=MAIN_FONT)
    login_entry.pack(side='top')

    label_password = Label(root_frame, text="Passowrd", bg="white", font=MAIN_FONT)
    label_password.pack(side='top')
    passwd = StringVar()
    passwd_entry = Entry(root_frame, textvariable=passwd, show="*", font=MAIN_FONT)
    passwd_entry.pack(side='top')

    error_lbl_text = StringVar()
    error_lbl = Label(root_frame, textvariable=error_lbl_text, bg="white", fg="red", pady=1, padx=5).pack(pady=5)

    passwd_entry.bind("<Return>", lambda self: login_check())

    login_button = Button(root_frame, text="Login", bg="white", command=lambda: login_check(), font=MAIN_FONT)
    login_button.pack(side='top', pady=1)

    last_lbl = Label(root_frame, text="   ", bg="white", fg="white", pady=1, padx=5).pack(pady=5)

    def login_check():
        p = passwd.get()
        l = login1.get()
        #print (l, p)
        c.execute("SELECT * FROM admins WHERE Login='%s' AND Password='%s'" % (l, p))

        login_admin = Users(l)

        if c.fetchone() is not None:
            root2.destroy()
            print('Logged in as ', l)
            main_app()
        else:
            #print("Login Error")
            error_lbl_text.set(">> Wrogn Login/Password <<")

    root2.mainloop()

def admins_table():
    c.execute("CREATE TABLE IF NOT EXISTS admins(Login, Password, Email)")
    print("done")

def admins_table_insert():
    c.execute("INSERT INTO admins(Login, Password, Email) VALUES('admin','123456', 'email@address.com')")
    conn.commit()
    print("record inserted!")

create_table()
input_data()
read_db()

create_table()
admins_table()
admins_table_insert()
loginPage()
#main_app()






