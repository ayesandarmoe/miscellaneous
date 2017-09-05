#!/bin/python

# https://www.hackerrank.com/challenges/day-of-the-programmer?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign


import sys
import calendar, datetime

def solve(year):
    # Complete this function
    numOfDays = 0
    for i in range(1, 13):
        if ( i == 2 ): # if it's february
            if year == 1918:
                if ( year % 4 == 0):
                    numOfDays += ( 29 - 14)
                else:
                    numOfDays += ( 28 - 14)
            elif 1700 <= year <= 1917: 
                if ( year % 4 == 0):
                    numOfDays += 29
                else:
                    numOfDays += 28
            else:
                if ( year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
                    numOfDays += 29
                else:
                    numOfDays += 28
        else:
            (start, end) = calendar.monthrange(year, i)
            numOfDays += end
            if 256 - numOfDays <= 30:
                dateObj = datetime.date(year,i + 1, 256-numOfDays)
                return dateObj.strftime("%d.%m.%Y")

 
        
year = int(raw_input().strip())
result = solve(year)
print(result)

