# import requests
# response = requests.get('https://www.google.com/')
# print(response.status_code)



#Datetime methods


import datetime
from datetime import date
now = datetime.datetime.now()
print(now)         #Current date & time

Today = datetime.date.today()
print(Today)          #Get current date

Time = datetime.time()
print(Time)

print(dir(datetime))

t = now.strftime("%H:%M:%S")
print("Time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)