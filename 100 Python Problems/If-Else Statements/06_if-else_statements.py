# 6.	Check leap year. 

import calendar as cal 

year = int(input("Enter the year: "))

if cal.isleap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")