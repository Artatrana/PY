#python program to print the calendar of a given month of a year
import calendar
month = int(input(" Enter the month :"))
year = int(input (" Enter the year :"))
print(calendar.month(year,month))
