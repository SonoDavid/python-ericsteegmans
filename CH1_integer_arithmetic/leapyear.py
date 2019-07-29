# Check whether a given year is a leap year.
#  A year is a leap year if it is a multiple of 4 and
#  not a multiple of 100, or it is a multiple of 400.
#
# Author: Joachim David
# Date: June 2019

year = int(input("Enter the year to examine: "))

if ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0):
    print(f'The year {year} is a leap year!')
else:
    print(f'The year {year} is not a leap year!')