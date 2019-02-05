#!/usr/bin/env checkio --domain=py run date-and-time-converter

# https://py.checkio.org/mission/date-and-time-converter/

# Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
# Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
# Your task is simple - convert the input date and time from computer format into a "human" format.
# 
# 
# 
# Input:Date and time as a string
# 
# Output:The same date and time, but in a more readable format
# 
# Precondition:
# 0<date<= 31
# 0<month<= 12
# 0<year<= 3000
# 0<hours<24
# 0<minutes<60
# 
# 
# END_DESC

def date_time(time: str) -> str:
    #replace this for solution
    #list of all the months for converting month number to month text
    month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    #time.replace(" ", ".").replace(":",".") to convert 01.01.2000 00:00 to 01.01.2000.00.00 making it easier to split in one go
    day, month, year, hours, mins = time.replace(" ", ".").replace(":",".").split(".")
    
    #converts month number to month text need a - 1 because the list counts from 0 - 11 and the month number is from 1 - 12
    month = month_lst[int(month) - 1]
    
    #checks if the hours and minutes are 1 for grammer corrections
    if int(hours) == 1:
        hour = "hour"
    else:
        hour = "hours"
        
    if int(mins) == 1:
        min = "minute"
    else:
        min = "minutes"
    
    #formats the string in the desired way
    formated_date = "%d %s %s year %d %s %d %s"  % (int(day), month , year, int(hours),hour, int(mins),min)
    
    return formated_date

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")