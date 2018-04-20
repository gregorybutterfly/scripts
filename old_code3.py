This is crazy code :). One of my first 'proper' coding. The best  function is contract_dates. This is true imagination.

"""

class datesTimes():

    def __init__(self, date):
        self.date = datetime.strptime(date, "%d-%m-%Y")

    def __str__(self):

        def weekend(self):
            while True:
                if self.date.isoweekday() == 6 or self.date.isoweekday() == 7:
                    print("Weekend: ", self.date)
                    return False
                else:
                    return True

        def bankholidays(self):
            bankhols = BankHolidays()

            for bank_holiday in bankhols.get_holidays():
                if bank_holiday['date'].strftime("%d-%m-%Y") == self.date.strftime("%d-%m-%Y"):
                    print("Wrong date because: " + str(bank_holiday['date']) + " - " + str(bank_holiday['title']))
                    return False

        def forbiddendates(self):
            dates = ['24-12-2017', '25-12-2017', '26-12-2017', '27-12-2017', '28-12-2017', '29-12-2017', '30-12-2017','31-12-2017']

            for date in dates:
                if datetime.strptime(date, "%d-%m-%Y") == self.date:
                    return False
            else:
                return True

        while True:
            if bankholidays(self) == False:
                self.date = self.date + timedelta(days=+1)
            elif weekend(self) == False:
                self.date = self.date + timedelta(days=+1)
                print("Next date", self.date)
            elif forbiddendates(self) is not True:
                print("Forbidden Date", self.date)
                self.date = self.date + timedelta(days=+1)
            else:
                return(str(self.date))

def contract_dates(id=0, mode=0, date=0, days=365):
     if mode == 0:
         print("Do Nothing")

     # Mode 1 - Returns contract END DATE.
     # contract_dates(mode=1, date="", days=365)
     elif mode == 1 and date != 0:
         contract_start = datetime.strptime(date, "%d-%m-%Y")
         contract_end = contract_start + timedelta(days=days) + relativedelta(weekday=FR)
         contract_end = datesTimes(date=contract_end.strftime("%d-%m-%Y"))
         return contract_end

     # Mode 2 - Returns END DATE COUNTER (use date from mode 1).
     # contract_dates(mode=2, date="")
     elif mode == 2:
         con_ed = datetime.strptime(date, "%d-%m-%Y")
         con_count = con_ed - today
         print("Mode 2 - End date counter returned")
         return int(con_count.days)

     # Mode 3 - Updates END DATE COUNTER in DB for ONE user. Use id="", mode=3
     # contract_dates(id="", mode=3)
     elif id != 0 and mode == 3:
         c.execute("SELECT con_ed FROM datestimes WHERE id='%s';" % id)
         userid = c.fetchone()
         con_ed_db = datetime.strptime(userid[0], "%d-%m-%Y")
         con_count_db = con_ed_db - today
         conn.execute("UPDATE datestimes SET con_ed_count='%s' WHERE id=%s;" % (con_count_db.days, id))
         conn.commit()
         print("Mode 3 - End date counter updated for ONE user (DB)", id, con_count_db.days)

     # Mode 4 - Updates END DATE COUNTER in DB for EVERY user
     # contract_dates(mode=4)
     elif mode == 4:
         c.execute("SELECT id, con_ed FROM datestimes;")
         rows = c.fetchall()

         for row in rows:
             result = datetime.strptime(row[1], "%d-%m-%Y")
             result = result - today
             conn.execute("UPDATE datestimes SET con_ed_count='%s' WHERE id=%s;" % (result.days, row[0]))
             conn.commit()
             print("Mode 4 - End date counter updated for EVERY user (DB)", row[0], result.days)

     # Mode 5 - Returns contract review date
     # contract_dates(mode=5, date="")
     elif mode == 5 and date != 0:
         con_rev = datetime.strptime(date, "%d-%m-%Y")
         con_rev = con_rev - relativedelta(weekday=WE(-3))
         print("Mode 5 - Contract reviev date returned")
         return con_rev.strftime("%d-%m-%Y")

     # Mode 6 - Update contract reviev date for one user (DB)
     # contract_dates(mode=6, id="")
     elif mode == 6 and id != 0:
         c.execute("SELECT con_ed FROM datestimes WHERE id=%s;" % id)
         con_rev_data = datetime.strptime(c.fetchone()[0], "%d-%m-%Y")
         con_rev_db = con_rev_data - relativedelta(weekday=WE(-3))
         c2.execute("UPDATE datestimes SET con_rev='%s' WHERE id=%s;" % (con_rev_db.strftime("%d-%m-%Y"), id))
         print("Mode 6 - Contract review date UPDATED (db) for ", id, con_rev_db.strftime("%d-%m-%Y"))
         conn.commit()

     # Mode 7 - Update contract reviev counter for ONE user (DB)
     # contract_dates(mode=6, id="")
     elif mode == 7 and id != 0:
         c.execute("SELECT con_rev FROM datestimes WHERE id=%s;" % id)
         con_rev_counter = c.fetchone()
         con_rev_counter = datetime.strptime(con_rev_counter[0], "%d-%m-%Y")
         con_rev_counter = con_rev_counter - today
         c.execute("UPDATE datestimes SET con_rev_count='%s' WHERE id='%s'" % (con_rev_counter.days, id))
         print("Mode 7 - Contract review counter for ONE user (DB) with id ", id, con_rev_counter.days)
         conn.commit()

     # Mode 8 - Updates contract review counter for EVERY user (DB)
     # contract_dates(mode=8)
     elif mode == 8:
         c.execute("SELECT id, con_rev FROM datestimes;")
         rows = c.fetchall()

         for row in rows:
             result_rev_count = datetime.strptime(row[1], "%d-%m-%Y")
             result_rev_count = result_rev_count - today
             conn.execute("UPDATE datestimes SET con_rev_count='%s' WHERE id=%s;" % (result_rev_count.days, row[0]))
             conn.commit()
             print("Mode 8 - Contract reviev counter updated for EVERY user (DB)", row[0], result_rev_count.days)


"""


import sqlite3
from dateutil import relativedelta, parser
from dateutil.relativedelta import relativedelta, MO, FR, WE, weekday
from datetime import datetime, timedelta, date
from govuk_bank_holidays.bank_holidays import BankHolidays

def contract_dates(id=0, mode=0, date=0, days=0):

    if mode == 0:
        print("Do Nothing")

    # Mode 1 - Returns contract END DATE
    if mode == 1:
        if date != 0 and days != 0:
            contract_start = datetime.strptime(date, "%d-%m-%Y")
            contract_end = contract_start + timedelta(days=days) + relativedelta(weekday=FR)
            return contract_end.strftime("%d-%m-%Y")
        else:
            print("No date OR No days")

    # Mode 2 - Returns contract counter (use date from mode 1)
    if mode == 2:
        con_ed = datetime.strptime(date, "%d-%m-%Y")
        con_count = con_ed - today
        return int(con_count.days)

    if mode == 3:


conn = sqlite3.connect("./db/database.db")
c = conn.cursor()
c2 = conn.cursor()


#todays date
today = datetime.today()

#######################

def birthdays(id=0, mode=0, date=0):

    """
    BIRTHDAYS FUNCTION:
    MODE 0 - DO NOTHING
    MODE 1 - RETURN NUMBER OF DAYS TILL NEXT BIRTHDAYS AS INT
    MODE 2 - UPDATE EXISTING BIRTHDAYS COUNTER FROM DB
    """

    # MODE 0 - DO NOTHING
    if mode == 0:
        print("Nothing")

    # MODE 1 - REGISTER
    elif mode == 1:
        print("Register")
        birthdays = datetime.strptime(date, "%d-%m-%Y")
        birthdays = birthdays.replace(year=today.year)
        if birthdays < today:
            birthdays = birthdays.replace(year=today.year + 1)
            birthdays = birthdays - today
            return int(birthdays.days)
        else:
            birthdays = birthdays - today
            return int(birthdays.days)

    # MODE 2 - UPDATE
    elif mode == 2:
        print("Update")
        c.execute("SELECT id, birthdays, birthdays_count FROM datestimes;")
        rows = c.fetchall()

        for row in rows:
            if id == row[0]:
                birthdays = datetime.strptime(row[1], "%d-%m-%Y")
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

#######################

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
                contract_start = datetime.strptime(row[1], "%d-%m-%Y")
                #contract_start = parser.parse(row[1])
                contract_end = contract_start + timedelta(days=days) + relativedelta(weekday=FR)
                if bankhols(contract_end) == False:
                    contract_end = contract_end + relativedelta(weekday=FR (+2))
                    print("Oops! ends on bank holiday + 1 week aded", contract_end)
                    return contract_end
                else:
                    print("Contract End: ", contract_end)
                    return contract_end
    else:
        contract_start = datetime.strptime(con_start, "%d-%m-%Y")
        #contract_start = parser.parse(con_start)
        contract_end = contract_start + timedelta(days=days) + relativedelta(weekday=FR)
        return contract_end.strftime("%d-%m-%Y")

# takes contract end date and counts how many days left to that day
def contract_end_counter(id, con_ed=0):
    if id != 0:
        c.execute("SELECT id, con_ed FROM datestimes;")
        rows = c.fetchall()

        for row in rows:
            if int(row[0]) == int(id):
                result = datetime.strptime(row[1], "%d-%m-%Y")
                print("ID", row[0])
                result = result - today
                print("Count", result.days)
                conn.execute("UPDATE datestimes SET con_ed_count='%s' WHERE id=%s;" % (result.days, row[0]))
                conn.commit()
                print("contract_end_days -> con_ed_counter UPDATED")
    else:
        con_ed = datetime.strptime(con_ed, "%d-%m-%Y")
        con_count = con_ed - today
        return con_count.days

# takes birthday and counts how many days left to that day
def birthdays_end_counter(id, birthdays=0):
    pass


# works with contract_end_date. Takes that date and checks if it is not bank holiday.
def bankhols(date):

    dat = datetime.strptime(date, "%d-%m-%Y")
    christmas = datetime(today.year, 12, 23)

    bankhols = BankHolidays()
    print("printed")



    for bank_holiday in bankhols.get_holidays():
        if bank_holiday['date'] == date:
            print("Dupa bo: " + str(bank_holiday['date']) + " - " + str(bank_holiday['title']))
            return False
    else:
        return True

 def forbiddenDates(self):

        bankhols = BankHolidays()
        christmas = datetime(today.year, 12, 23)

        while True:
            if self.date >= christmas and self.date < datetime(today.year + 1, 1, 2):
                self.date = self.date + timedelta(days=+1)
                print("Wrong date", self.date)
            elif self.date.isoweekday() == 6 or self.date.isoweekday() == 7:
                self.date = self.date + timedelta(days=+1)
            else:
                for bank_holiday in bankhols.get_holidays():
                    if bank_holiday['date'].strftime("%d-%m-%Y") == self.date.strftime("%d-%m-%Y"):
                        print("Wrong date because: " + str(bank_holiday['date']) + " - " + str(bank_holiday['title']))
                        return False
                else:
                    return self.date



def select_all():
    c.execute("SELECT * FROM datestimes;")
    rows = c.fetchall()

    for row in rows:
        print (row)

def parse_birthdate():
    c.execute("SELECT id, con_sd FROM datestimes;")
    rows = c.fetchall()

    for row in rows:
        con = datetime.strptime(row[1], "%d-%m-%Y")
        date = str(con.strftime("%d-%m-%Y"))

        c.execute("UPDATE datestimes SET con_sd='%s' WHERE id=%s;" % (date, row[0]))
        print("Record has been updated")


# Sets contract reviev date for ID
def contract_rev_date(id, con_ed=0):
    if id != 0:
        c.execute("SELECT con_ed FROM datestimes WHERE id=%s;" % id)
        data = datetime.strptime(c.fetchone()[0], "%d-%m-%Y")
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
        contract_ed = datetime.strptime(con_ed, "%d-%m-%Y")
        two_weeks_before = contract_ed - relativedelta(weekday=WE(-3))
        dat = two_weeks_before.strftime("%d-%m-%Y")
        return dat

# Sets contract reviev counter for ID
def contract_rev_counter(id, con_rev=0):
    if id != 0:
        c.execute("SELECT con_rev FROM datestimes WHERE id=%s;" % id)
        rows = c.fetchall()

        for row in rows:
            print("TESTING END DATE", row[0])
            con_rev_d = datetime.strptime(row[0], "%d-%m-%Y")
            con_rev_d = con_rev_d - today
            print("Dni do konca", con_rev_d.days)
            c.execute("UPDATE datestimes SET con_rev_count='%s' WHERE id='%s'" % (con_rev_d.days, id))
            print ("Contract review date for user %s has been updated" % id)
            conn.commit()
    else:
        con_rev = datetime.strptime(con_rev, "%d-%m-%Y")
        con_rev = con_rev - today
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
#contract_end_counter(3)
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

#updates()

def testdb():

    c.execute("SELECT * FROM datestimes")

    rows = c.fetchall()
    for row in rows:
        print(row)

#end_of_contract()
#daysofwork_for_all()
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

#main_program()

### GUI

'''

(1, '19-07-2013', '20-02-2017', '23-02-2018', '17-06-1986', '370', '119', '07-02-2018', 499, 1)
(2, '13-01-2017', '20-01-2017', '26-01-2018', '11-11-1999', '342', '266', '10-01-2018', 590, 2)
(3, '13-05-2013', '01-10-2017', '12-01-2018', '22-11-1960', '650', '276', '14-11-2018', 633, 3)


    c.execute(
        "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY #AUTOINCREMENT, name TEXT NOT NULL, surname TEXT not null, contract TEXT NOT NULL, gender TEXT)")
    print("Database users has been created")

    c.execute(
        "CREATE TABLE IF NOT EXISTS datestimes(id INTEGER PRIMARY KEY AUTOINCREMENT, joined DATE, con_sd DATE, con_ed DATE, birthdays DATE)")
    print("Database datestimes has been created")

    c.execute(
        "CREATE TABLE IF NOT EXISTS daysofwork(id INTEGER PRIMARY KEY AUTOINCREMENT, monday TEXT, tuesday TEXT, wednesday TEXT, thursday TEXT, friday TEXT)")
    print("Database datestimes has been created")

    c.execute(
        "CREATE TABLE IF NOT EXISTS contacts(id INTEGER PRIMARY KEY AUTOINCREMENT, address1 TEXT, address2 TEXT, town TEXT, county TEXT, postcode TEXT, telno TEXT, mobno TEXT, email TEXT)")
    print("Database contacts has been created")

#c.execute("ALTER TABLE datestimes ADD COLUMN con_rev_count INTEGER")
#conn.commit()
#print("done")


'''
