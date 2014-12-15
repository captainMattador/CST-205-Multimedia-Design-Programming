
import calendar
from datetime import date


# pre condition: takes 2 parameters year and month
# prints the calendar of a given birth month
def birthMonth(year, month):
  calendar.prmonth(year, month)
  



# pre condotion: takes 3 paramaters year, month, day
# post condition: determines the days between now,
# and the future bday that is entered and returns
# the number of days
def daysUntilBday(year, month, day):
  d1 = date(year, month, day)
  d2 = date.today()
  return (d1-d2).days




# pre condotion: takes 3 paramaters year, month, day
# post condition: determines the day of week the date is on
def dayOfWeek(year, month, day):
  d1 = date(year, month, day).isoweekday()
  if d1 == 1:
    print "Monday"
  elif d1 == 2:
    print "Tuesday"
  elif d1 == 3:
    print "Wednesday"
  elif d1 == 4:
    print "Thursday"
  elif d1 == 5:
    print "Friday"
  elif d1 == 6:
    print "Saturday"
  elif d1 == 7:
    print "Sunday"
  else:
    print "There was an error."



# caller function to print calandr of month I was born
birthMonth(1983, 5)

# caller function to print the days until my bday
d = daysUntilBday(2015, 5, 15)
print d


# caller function to print the day of the week was the 
# Declaration of Independence ratified by the Continental Congress
dayOfWeek(1776, 7, 4)