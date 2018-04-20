""" Checks if employee contracts are still valid and counts time to their next birthdate. I was working as an Admin Assistant for coupe of years and found this CONCEPT to be useful.
"""

import sqlite3
from datetime import datetime, timedelta
from dateutil import parser
from dateutil.relativedelta import relativedelta, MO, FR
from tkinter import *
from tkinter import ttk

conn = sqlite3.connect("wsw.db")
c = conn.cursor()

today = datetime.today()

class NewMember():
    """ Add new member to our database. Java inspired :)
    """
    
    def __init__(self, name, surname, joined, con_sd, birthday):
        self.name = name
        self.surname = surname
        self.joined = joined
        self.con_sd = con_sd
        self.con_ed = self.setContractEd()
        self.birthday = birthday

    def setName(self, new_name):
        self.name = new_name

    def getName(self):
        return self.name

    def setSurname(self, new_surname):
        self.surname = new_surname

    def getSurname(self):
        return self.surname

    def getJoined(self):
        return self.joined

    def setJoined(self, new_joined):
        self.joined = new_joined

    def setContractSd(self, new_con_sd):
        self.con_sd = new_con_sd

    def getContractSd(self):
        return self.con_sd

    def setContractEd(self):
        return self.con_sd + timedelta(days=365) + relativedelta(weekday=FR(+1))

    def getContractEd(self):
        return self.con_ed

    def getBirthday(self):
        return self.birthday

    def setBirthday(self, new_birthday):
        self.birthday = new_birthday

    # days to go to end of contract
    def daysToGo(self):
        res = self.con_ed - self.con_sd
        return res.days

    def birthdaysToGo(self):
        btg = self.getBirthday()
        btg = btg + relativedelta(year=today.year)
        if btg < today:
            btg = btg.replace(year=today.year + 1)
        diff = btg - today

        return diff.days


def add_new_member():
    name = input("Name: ")
    surname = input("Surname: ")
    joined = input("Date Joined: ")
    con_sd = parser.parse(input("Start Date: "))
    birthday = parser.parse(input("Birthday Date: "))
    memb = NewMember(name, surname, joined, con_sd, birthday)

    c.execute(
        "INSERT INTO members(name, surname, joined, con_sd, con_ed, birthday, con_days_to_go, birthdays_to_go) VALUES (?,?,?,?,?,?,?,?)", (memb.getName(), memb.getSurname(), memb.getJoined(), memb.getContractSd(), memb.getContractEd(), memb.getBirthday(), memb.daysToGo(), memb.birthdaysToGo()))
    conn.commit()
    print ("New member has been added")

def create_db():
    c.execute("CREATE TABLE IF NOT EXISTS members(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(15), surname VARCHAR(15), joined DATE, con_sd DATE, con_ed DATE, birthday DATE, con_days_to_go INT, birthdays_to_go INT)")
    print("Db has been created")

def select_all():
    c.execute("SELECT * FROM members")

    rows = c.fetchall()

    for row in rows:
        print ("ID: ", row[0],
               "Name: ", row[1],
               "\nSurname: ", row[2],
               "\nJoined: ", row[3],
               "\nContract Started: ", row[4],
               "\nEnd of Contract: ", row[5],
               "\nDOB: ", row[6],
               "\nNext birthday: ", row[8],
               "\nDays to Go: ", row[7])
        print(" ")

def validContractDates(*val):
    
    print ("Valid contracts")
    val = list(val)
    for i in range(0, len(val)):
        c.execute("SELECT id, con_ed, con_days_to_go FROM members WHERE id=%s" % val[i])
        data = c.fetchone()
        exp_dat = datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")
        res = exp_dat - today
        #print(res.days)
        c.execute("UPDATE members SET con_days_to_go ={0} WHERE id ={1}".format(res.days, val[i]))
        conn.commit()

def expiredContractsDates(*exp):

    print("Expired Contracts")
    exp = list(exp)
    for i in range(0, len(exp)):
        c.execute("SELECT id, con_ed, con_days_to_go FROM members WHERE id=%s" % exp[i])
        data = c.fetchone()
        print("EXPIRED ", data[0], data[1], data[2])

def contractsDates():

    expired_contracts = []
    valid_contracts = []
    c.execute("SELECT id, name, surname, con_ed FROM members")
    rows = c.fetchall()
    for row in rows:
        #contract end date
        res = parser.parse(row[3])

        if res < today:
            expired_contracts.append(row[0])
            continue
        else:
            res = res - today
            valid_contracts.append(row[0])

    #> print ("Valid contracts: ", valid_contracts)
    validContractDates(*valid_contracts)
    #> print ("Expired contracts: ", expired_contracts)
    expiredContractsDates(*expired_contracts)

# CREATE DATABASE
#create_db()
# ADD NEW MEMBER
#add_new_member()

select_all()

