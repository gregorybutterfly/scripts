My old code :). Crazy times: 
I will keep it form sentimental reason.

import sqlite3
from dateutil import relativedelta, parser
from dateutil.relativedelta import relativedelta, MO, FR, WE, weekday
from datetime import datetime, timedelta, date
from govuk_bank_holidays.bank_holidays import BankHolidays

conn = sqlite3.connect("database.db")
c = conn.cursor()
c2 = conn.cursor()


#todays date
today = datetime.today()

### FUNCTIONS FOR ALL

#ALL update birthdays conter every time for every user
def birthdays_end_counter_update():
    c.execute("SELECT id FROM datestimes;")
    rows = c.fetchall()

    for row in rows:
        birthdays_end_counter(int(row[0]))
        print("Birthdays counter for id=%s has been updated;" % int(row[0]))

#ALL updates contract end counter for every user
def contract_end_counter_update():
    c.execute("SELECT id FROM datestimes;")
    rows = c.fetchall()

    for row in rows:
        contract_end_counter(int(row[0]))
        print("Contract end ounter for id=%s has been updated;" % int(row[0]))

def contract_rev_counter_for_all():
    c.execute("SELECT id FROM datestimes;")
    rows = c.fetchall()

    for row in rows:
        contract_rev_counter(int(row[0]))
        print("Contract rev ounter for id=%s has been updated;" % int(row[0]))

### END OF FUNCTIONS FOR ALL

### FUNCTIONS PER ID

# counts and returns contract end date (default number of days 365)
def contract_end_date(id, days=365, con_start="0"):
    if id != 0:
        c.execute("SELECT id, con_sd FROM datestimes;")
        rows = c.fetchall()
        for row in rows:
            if int(row[0]) == int(id):
                contract_start = parser.parse(row[1])
                contract_end = contract_start + timedelta(days=days) + relativedelta(weekday=FR)
                if bankhols(contract_end) == False:
                    contract_end = contract_end + relativedelta(weekday=FR (+2))
                    print("Oops! ends on bank holiday + 1 week aded", contract_end)
                    return contract_end
        else:
            print("Contract End: ", contract_end)
            return contract_end
    else:
        contract_start = parser.parse(con_start)
        contract_end = contract_start + timedelta(days=days) + relativedelta(weekday=FR)
        return contract_end.strftime("%d-%m-%Y")

# takes contract end date and counts how many days left to that day
def contract_end_counter(id, con_ed=0):
    if id != 0:
        c.execute("SELECT id, con_ed FROM datestimes;")
        rows = c.fetchall()

        for row in rows:
            if int(row[0]) == int(id):
                result = parser.parse(row[1]) - today
                conn.execute("UPDATE datestimes SET con_ed_count=%s WHERE id=%s;" % (result.days, row[0]))
                conn.commit()
                print("contract_end_days -> con_ed_counter UPDATED")
    else:
        con_count = parser.parse(con_ed) - today
        return con_count.days

# takes birthday and counts how many days left to that day
def birthdays_end_counter(id, birthdays=0):
    if id != 0:
        c.execute("SELECT id, birthdays, birthdays_count FROM datestimes;")
        rows = c.fetchall()

        for row in rows:
            if id == row[0]:
                print (row[1], row[2])
                birthdays = parser.parse(row[1])
                birthdays = birthdays.replace(year=today.year)
                if birthdays < today:
                    birthdays = birthdays.replace(year=today.year + 1)
                    birthdays = birthdays - today
                    c.execute("UPDATE datestimes SET birthdays_count=%s WHERE id=%s;" % (birthdays.days, id))
                    conn.commit()
                    print("+ 1 year")
                else:
                    birthdays = birthdays - today
                    c.execute("UPDATE datestimes SET birthdays_count=%s WHERE id=%s;" % (birthdays.days, id))
                    conn.commit()
                    print("+ 0 years")
    else:
        birthdays = parser.parse(birthdays)
        birthdays = birthdays.replace(year=today.year)
        if birthdays < today:
            birthdays = birthdays.replace(year=today.year + 1)
            birthdays = birthdays - today
            return birthdays.days
        else:
            birthdays = birthdays - today
            return birthdays.days

# works with contract_end_date. Takes that date and checks if it is not bank holiday.
def bankhols(date):
    bankhols = BankHolidays()
    print("printed")
    for bank_holiday in bankhols.get_holidays():
        if bank_holiday['date'] == date:
            print("Dupa bo: " + str(bank_holiday['date']) + " - " + str(bank_holiday['title']))
            return False
    else:
        return True

def select_all():
    c.execute("SELECT * FROM datestimes;")
    rows = c.fetchall()

    for row in rows:
        print (row)

def parse_birthdate():
    c.execute("SELECT id, con_sd FROM datestimes;")
    rows = c.fetchall()

    for row in rows:
        con = parser.parse(row[1])
        date = datetime.strftime(con, "%d-%m-%Y")

        c.execute("UPDATE datestimes SET con_sd='%s' WHERE id=%s;" % (date, row[0]))
        print("Record has been updated")

# Sets contract reviev date for ID
def contract_rev_date(id, con_ed=0):
    if id != 0:
        c.execute("SELECT con_ed FROM datestimes WHERE id=%s;" % id)
        data = parser.parse(c.fetchone()[0])
        print (data)

        two_weeks_before = data - relativedelta(weekday=WE(-3))
        dat = two_weeks_before.strftime("%d-%m-%Y")

        print("Review date is: ", two_weeks_before.strftime("%d-%m-%Y"))
        c2.execute("UPDATE datestimes SET con_rev='%s' WHERE id=%s;" % (dat, id))
        #print(data)
        print("Contract review date has been updated")
        conn.commit()
        #return two_weeks_before
    else:
        two_weeks_before = parser.parse(con_ed) - relativedelta(weekday=WE(-3))
        dat = two_weeks_before.strftime("%d-%m-%Y")
        return dat

# Sets contract reviev counter for ID
def contract_rev_counter(id, con_rev=0):
    if id != 0:
        c.execute("SELECT con_rev FROM datestimes WHERE id=%s;" % id)
        rows = c.fetchall()

        for row in rows:
            print("TESTING END DATE", row[0])
            con_rev_d = parser.parse(row[0]).strftime("%d-%m-%Y")
            con_rev_d = parser.parse(con_rev_d) - today
            print("Dni do konca", con_rev_d.days)
            c.execute("UPDATE datestimes SET con_rev_count='%s' WHERE id='%s'" % (con_rev_d.days, id))
            print ("Contract review date for user %s has been updated" % id)
            conn.commit()
    else:
        con_rev = parser.parse(con_rev).strftime("%d-%m-%Y")
        con_rev = parser.parse(con_rev) - today
        return con_rev.days

# checks if input is date
def isdate(string):
    while True:
        try:
            x = parser.parse(input(string)).strftime("%d-%m-%Y")
            return x
        except:
            print("Try again!")

# checks if input is alphabetical
def isalpha(string):
    while True:
        x = input(string).capitalize()
        if x.isalpha():
            return x
        else:
            print("Wrong input. Try again!")

#gets last id from db
def get_id_from_db():

    c.execute("SELECT COUNT(*) FROM users;")
    d = c.fetchone()

    return (d[0] + 1)

def daysofwork_for_all(id = 0):
    if id != 0:
        print("print for one user")
        c.execute("SELECT users.id, name, surname, daysofwork.monday, daysofwork.tuesday, daysofwork.wednesday, daysofwork.thursday, daysofwork.friday FROM users JOIN daysofwork ON users.id=daysofwork.uid WHERE users.id=%s" % id)

        rows = c.fetchall()
        print(rows)
    else:
        print("print for all users")
        c.execute(
            "SELECT users.id, name, surname, daysofwork.monday, daysofwork.tuesday, daysofwork.wednesday, daysofwork.thursday, daysofwork.friday FROM users INNER JOIN daysofwork ON users.id = daysofwork.id;")

        rows = c.fetchall()

        for row in rows:
            print(row)

def add_new_member():

    # first free id from db
    id = get_id_from_db()
    print(id)

    # users
    name = isalpha("Name: ").capitalize()
    surname = isalpha("Surname: ").capitalize()
    contract = isalpha("Contract: ").upper()
    gender = isalpha("Gender (Male/Female): ").capitalize()
    joined = isdate("Date Joined (DD/MM/YY): ")

    # datestimes
    uid = id
    con_sd = isdate("Contract Start Date: ")
    print(con_sd, type(con_sd))
    con_ed = contract_end_date(0, con_start=con_sd)
    birthdays = isdate("Date of Birth: ")
    con_ed_count = contract_end_counter(0, con_ed=con_ed)
    birthdays_count = birthdays_end_counter(0, birthdays=birthdays)
    con_rev = contract_rev_date(0, con_ed=con_ed)
    con_rev_count = contract_rev_counter(0, con_rev = con_rev)

    # daysofwork
    uid2 = id
    monday = input("Work on Monday (Y/N): ").upper()
    tuesday = input("Work on Tuesday (Y/N): ").upper()
    wednesday = input("Work on Wednesday (Y/N): ").upper()
    thursday = input("Work on Thursday (Y/N): ").upper()
    friday = input("Work on Friday (Y/N): ").upper()

    # contacts
    uid3 = id
    address1 = input("Address 1: ").capitalize()
    address2 = input("Address 2: ").capitalize()
    town = isalpha("Town: ").capitalize()
    county = isalpha("County: ").capitalize()
    postcode = input("Postcode: ").upper()
    telno = input("Telephone Number: ")
    mobno = input("Mobile Number: ")
    email = input("Email: ")

    c.execute("INSERT INTO users(name, surname, contract, gender) VALUES ('%s', '%s', '%s', '%s');" % (name, surname, contract, gender))
    print ("table users has been updated")
    c.execute("INSERT INTO datestimes(joined, con_sd, con_ed, birthdays, con_ed_count, birthdays_count, con_rev, con_rev_count, uid) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' );" % (joined, con_sd, con_ed, birthdays, con_ed_count, birthdays_count, con_rev, con_rev_count, uid))
    print ("table datestimes has been updated")
    c.execute("INSERT INTO daysofwork(monday, tuesday, wednesday, thursday, friday, uid) VALUES ('%s','%s','%s','%s','%s', '%s');" % (
    monday, tuesday, wednesday, thursday, friday, uid2))
    print("table daysofwork has been updated")
    c.execute("INSERT INTO contacts(address1, address2, town, county, postcode, telno, mobno, email, uid) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (address1, address2, town, county, postcode, telno, mobno, email, uid3))
    print ("table contacts has been updated")
    conn.commit()

def show_all_users():
    c.execute("SELECT * FROM users")
    rows = c.fetchall()

    for row in rows:
        print (row)

#dat = date(2017, 4, 14)
#print (dat)
#print (bankhols(dat))

#contract_end_date(2)
#contract_end_counter(2)
#birthdays_end_counter(3)
#contract_end_counter_update()
#select_all()
#birthdays_end_counter_update()
#parse_birthdate()
#contract_rev_date(3)
#contract_rev_counter(1)

#> MAIN PROGRAM
def birthdays():

    c.execute("SELECT users.id, users.name, users.surname, datestimes.birthdays, datestimes.birthdays_count FROM users INNER JOIN datestimes ON users.id=datestimes.id")

    rows = c.fetchall()

    for row in rows:
        print("ID:", row[0], row[1], row[2], \
              "\nBirthdays: ", row[3], \
              "Next Birthdays in days: ", row[4]
              )

def end_of_contract():

    c.execute("SELECT users.id, users.name, users.surname, datestimes.con_ed, datestimes.con_ed_count, datestimes.con_rev, datestimes.con_rev_count FROM users INNER JOIN datestimes ON users.id=datestimes.uid")

    rows = c.fetchall()

    for row in rows:
        print(row)

def updates():
    birthdays_end_counter_update()
    contract_end_counter_update()
    contract_rev_counter_for_all()

def testdb():

    c.execute("SELECT * FROM datestimes")

    rows = c.fetchall()
    for row in rows:
        print(row)

#daysofwork_for_all(1)
#testdb()
#add_new_member()

def main_program():
    updates()
    def mmtop():
        print(" ")
        print("MAIN MENU")
        print(" ")
    mmtop()

    print("1 FILE")
    print("1.1 - Quit")
    print(" ")
    print("2 Users")
    print("2.1 - Add New User")
    print(" ")

    print("TAB 1 - DAYS OF WORK")
    daysofwork_for_all()
    print("")
    print("")
    print("TAB 2 - BIRTHDAYS")
    birthdays()
    print("")
    print("")
    print("TAB 3 - END OF CONTRACT")
    end_of_contract()

    print("")
    print("")
    print("Status Bar")

main_program()
