# Write a Python program to extract year, month, date and time using Lambda

import datetime
current_date_time = datetime.datetime.now()

current_date = lambda x : x.date()
print("The Current date is", current_date(current_date_time))


current_time = lambda x : x.time()
print("The current_time is ", current_time(current_date_time))

current_year = lambda x : x.year
print("The current year is", current_year(current_date_time))

current_month = lambda x : x.month
print("The current_month",current_month (current_date_time))