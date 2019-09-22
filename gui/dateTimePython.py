#DateTime module of Python

import datetime

now = datetime.date(2015, 7, 15)
print(now)

my_bd= datetime.date(1977, 8, 13)

print(now.day)
print(datetime.date.today().year)
print(datetime.date.today()-my_bd)
print("Year ",(datetime.date.today()-my_bd)/365 )