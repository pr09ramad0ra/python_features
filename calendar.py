# Python has inbuilt module "calendar" with several functions: month, calendar
# to print the calendar of the current month:

import calendar
import datetime

current_year = datetime.date.today().year
current_month = datetime.date.today().month

print(calendar.month(current_year, current_month))

"""
     March 2023
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
"""

https://docs.python.org/3/library/calendar.html#calendar.Calendar
