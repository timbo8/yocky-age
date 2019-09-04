# Yock's Birthday = 10 Jan 2018, Cat age = 7x Human age.
# Display Yock's age today

import datetime
from datetime import date

def diff_dates(date1, date2):
    return abs(date2-date1).days

today = date.today()
d1 = today.strftime("%d/%m/%Y")
dyear = d1[6:]
dmonth = d1[3:5]
dday = d1[0:2]

dyocksbd = date(2018,1,10)
dtoday = date(int(dyear),int(dmonth),int(dday))
daysold = diff_dates(dtoday, dyocksbd)

yocksage = 7 * daysold
yockyears = yocksage // 365
yockdays = yocksage % 365
print("Yocks is", yockyears, "year", yockdays, "days old today (", dtoday, ")")




