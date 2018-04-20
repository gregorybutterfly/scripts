import dateutil.parser
from dateutil.relativedelta import relativedelta, FR
import datetime

today = input("Date: ")
today_parse = dateutil.parser.parse(today).strftime("%d-%m-%Y")
today_day = datetime.datetime.strptime(today_parse, '%d-%m-%Y')
contract = int(input("Days: "))
print (today_day, contract)
contract_end = today_day + relativedelta(days=contract)


print (today_parse)
print (contract_end.strftime("%d-%m-%Y"))
