
'''import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m)) '''

from datetime import datetime
import calendar

curr_year = datetime.now().year
curr_month = datetime.now().month
curr_day = datetime.now().day

#ANSI escape sequences for colors
colored_day = '\033[92m' + str(curr_day) + '\033[0m'

calendar_output = (calendar.month(curr_year, curr_month))

#finds the first occurrence of today's date and changes its color 
highlighted_day = calendar_output.replace(str(curr_day), colored_day, 1)

print(highlighted_day)
