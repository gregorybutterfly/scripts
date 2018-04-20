""" Add and monitor your members
LOGIN: admin
PASS: 123456
"""

import sqlite3
import datetime
from dateutil.relativedelta import relativedelta, FR
import dateutil.parser

conn = sqlite3.connect("wsw.db")
c = conn.cursor()

def create_test_user():
    c.execute("INSERT INTO employees(login, password) VALUES ('admin','123456')")
    conn.commit()
    print("Created")

def login_form():
    print ("Login Form")
    login = input("Login: ")
    password = input("Password: ")

    c.execute("SELECT * FROM employees WHERE login='%s' AND password='%s'" % (login, password))

    if c.fetchone() is not None:
        main_window()
    else:
        print ("Fail")


def create_db():

    c.execute(
        "CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT, surname TEXT, birth_date TEXT, gender TEXT, nationality TEXT, religion TEXT, nino TEXT, language TEXT, marital_status TEXT, disability TEXT, address TEXT, postcode TEXT, email TEXT, tel_no TEXT, mob_no TEXT, car_reg TEXT, school_attended TEXT, specialised TEXT, kin_name TEXT, kin_surname TEXT, kin_relationship TEXT, kin_address TEXT, kin_postcode TEXT, kin_telno TEXT, kin_mobno TEXT, kin_email TEXT, gp_name TEXT, gp_surname TEXT, gp_organisation TEXT, gp_address TEXT, gp_postcode TEXT, gp_telno TEXT, personal_circumstances TEXT, contract TEXT, contract_sd TEXT, contract_ed TEXT, login TEXT, password TEXT)")
    return


def new_user():

    try:
        name = input("Name: ")
        surname = input("Surname: ")
        birth_date = input("Birth Date: ")
        gender = input("Gender (M/F): ")
        nationality = input("Nationality: ")
        religion = input("Religion: ")
        nino = input("National Insurance Number: ")
        language = input("Preferred Language: ")
        marital_status = input("Marital Status (Y/N): ")
        disability = input("Disability: ")
        address = input("Address: ")
        postcode = input("Postcode: ")
        email = input("Email Address: ")
        tel_no = input("Telephone Number: ")
        mob_no = input("Mobile Number: ")
        car_reg = input("Car Reg: ")
        school_attended = input("School Attended: ")
        specialised = input("Specialised: ")

        kin_name = input("(Next/Kin) Name: ")
        kin_surname = input("(Next/Kin) Surname: ")
        kin_relationship = input("(Next/Kin) Relationship: ")
        kin_address = input("(Next/Kin) Address: ")
        kin_postcode = input("(Next/Kin) Postcode: ")
        kin_telno = input("(Next/Kin) Telephone Number: ")
        kin_mobno = input("(Next/Kin) Mobile Number: ")
        kin_email = input("(Next/Kin) Email Address: ")

        gp_name = input("(GP) Name: ")
        gp_surname = input("(GP) Surname: ")
        gp_organisation = input("(GP) Surgery Name: ")
        gp_address = input("(GP) Surgery Address: ")
        gp_postcode = input("(GP) Postocde: ")
        gp_telno = input("(GP) Telephone Number:: ")
        ### Disability and others ###
        personal_circumstances = input("Personal Circumstances: ")
        ### contract (WC, HCS, Volunteer, Director, Paid, Casual, Other ###
        contract = input("Contract: ")

        contract_sd_temp = input("Contract Start Date: ")
        contract_sd_temp2 = dateutil.parser.parse(contract_sd_temp).strftime("%d-%m-%Y")
        contract_sd = datetime.datetime.strptime(contract_sd_temp2, '%d-%m-%Y')
        contract_lenght = int(input("Contract lenght in days: "))
        contract_12 = datetime.timedelta(days=contract_lenght)
        contract_ed = contract_sd + contract_12 + relativedelta(weekday=FR)
    except:
        print ("Wrong")
    else:
        c.execute("INSERT INTO employees(name, surname, birth_date, gender, nationality, religion, nino, language, marital_status, disability, address, postcode, email, tel_no, mob_no, car_reg, school_attended, specialised, kin_name, kin_surname, kin_relationship, kin_address, kin_postcode, kin_telno, kin_mobno, kin_email, gp_name, gp_surname, gp_organisation, gp_address, gp_postcode, gp_telno, personal_circumstances, contract, contract_sd, contract_ed) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (name, surname, birth_date, gender, nationality, religion, nino, language, marital_status, disability, address, postcode, email, tel_no, mob_no, car_reg, school_attended, specialised, kin_name, kin_surname, kin_relationship, kin_address, kin_postcode, kin_telno, kin_mobno, kin_email, gp_name, gp_surname, gp_organisation, gp_address, gp_postcode,gp_telno, personal_circumstances, contract, contract_sd, contract_ed))
        conn.commit()
        main_window()


def show_users():
    c.execute("SELECT * FROM employees")
    row = c.fetchall()

    for rows in row:
        if rows[0] == 1:
            continue
        else:
            print (
               "ID: {0}, {1} {2}".format(str(rows[0]),str(rows[1]),str(rows[2]),str(rows[3])))
    main_window()


def delete_user():
    pass


def main_window():
    try:
        print (" ")
        print ('=' * 30)
        print("Main window")
        print ('=' * 30)
        print(" ")
        print("1. Add new user")
        print("2. Delete user")
        print("3. Show users in DB")
        print(" ")
        mi = int(input("Enter a number: "))
    except:
        print ("Something went wrong")
    else:
        if mi == 1:
            new_user()
        elif mi == 2:
            delete_user()
        else:
            show_users()
    print(" ")

create_db()
create_test_user()
login_form()
