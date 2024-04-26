# With datetime module we can deal with - different timezones, date formats, daylight saving times

# ------------------------------------------------------------------
"""
- How computer count time?
    all computers count time from an instant called the Unix epoch.
    This occurred on January 1, 1970, at 00:00:00 UTC. 
    UTC is often called Greenwhich Mean Time too.

- Python has 3 built-in libraries like - 
    1. time: we can work with time in this
    2. datetime: we can manipulate date and time with this
    3. calendar:
"""

# example -
import time
print(time.time())

#lets calcualte time taken by loop
start_time = time.time()
for i in range(2):
    time.sleep(i)
end_time = time.time()
print(f"Number of seconds loop took: {(end_time - start_time):.2} secs")
print()

# ------------------------------------------------------------------
"""
- Another problem with date is:
    The USA writes date in: MM-DD-YYYY
    Europe and most of the Indian region write: DD-MM-YYYY

So, to avoid these mistakes - ISO developed: "ISO 8601"
this standard specify that all dates should be written in: "YYYY-MM-DD HH:MM:SS"
"""

# Lets start datetime module
print("------STARTING DATETIME MODULE------")
"""
- time module is less powerful and more complicated to use than datetime module. 

- In datetime we have these three classes which are really helpful

    1. datetime.date: this assumes the Gregorian calendar extends infinitely into the future and past. 
                      This object stores the year, month, and day.

    2. datetime.time: this assumes there are 86,400 seconds per day with no leap seconds. 
                      This object stores the hour, minute, second, microsecond, and tzinfo.
            
    3. datetime.datetime: this is a combo of a date and time, and has all attributes of date and time
"""

# Lets see time, date and datetime classes in action
from datetime import date, time, datetime

# Instantiate imported classes
print("Date: ", date(year=2024, month=4, day=26))
print("Time: ", time(hour=8, minute=55, second=50))
print("Datetime: ", datetime(year=2024, month=4, day=26, hour=8, minute=55, second=50))

# ------------------------------------------------------------------
print()
print("Convinent way to create datetime instances")
"""
- In above we have to specify attribute to get those date and time
  but there is a way where we dont need to specify any attribute.

  1. date.today() - creates current local date
  2. datetime.now() - creates current local date and time
  3. datetime.combine() - combines instances of datetime.date and datetime.time into a single datetime.datetime instance.
"""

print("Today date is: ", date.today())
print("Right now date and time is: ", datetime.now())

# ------------------------------------------------------------------
print()
print("Using string to create datetime object")
"""
- we have .fromisoformat() from date class - to use this method, you provide a string with the date in the ISO 8601 format(YYYY-MM-DD)
  and converts string object into datetime object
"""
print("From ISO standard String to Datetime: ",date.fromisoformat("1997-08-29"))

"""
- What if string is not in ISO 8601 format then?
  then we have strptime() method from datetime class

- How to use? 
  So, suppose if we are giving this string "29-08-1997"
  above string is in DD-MM-YYYY format, so we also need to provide this format in strptime function
"""
date_string = "29-08-1997"
print("Example of conversion using strptime: ", datetime.strptime(date_string, "%d-%m-%Y"))

# so, lets give full date including time
date_string = "29-08-1997 02:00:00" # time is in 24 hrs
print("My exact birth time: ", datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S"))
# ------------------------------------------------------------------

"""
- Some useful info
0: Monday
1: Tuesday
2: Wednesday
3: Thursday
4: Friday
5: Saturday
6: Sunday

------------------------------
strftime method in datetime
------------------------------
%Y: get current year in YYYY, for example - 2023.
%y: get current year in YY, for example - current year is 2023 so we will get - 23.
%m: get month in number, example - if current month is November then we will get 11.
%B: get month name in Full, example - November
%b or %h: Abbreviated month name, example - Jan, Nov)
%d: get date of month - like if it is 28/Nov/2023 then we will get 28.
%A: get weekday name, example - Monday, Sunday
%a: Abbreviated weekday name, example -  Mon, Sun

usage:
today_date = datetime.now()
current_month = today_date.strftime('%B')
"""

"""
- What if I want to convert datetime object into string?
  Then we have: strftime from datetime
  It's used to convert a datetime object into a string representation that's formatted according to a specific pattern.
"""
print()
# let see usecase, I want to get today day only
today_date = datetime.now()
print("Today date is:", today_date)
#Now, from above output - I just want to get Month or year or minutes or anythin, we can get it with strftime
extracted_date = today_date.strftime("%d")
print("Date is:",extracted_date)

# or we can format like -
print("Formatted topday date:", today_date.strftime("%d-%m-%Y"))

"""
- All formats
    Day, Month, Year Formats:
        %d: Day of the month as a zero-padded decimal number.
        %m: Month as a zero-padded decimal number.
        %Y: Year with century as a decimal number.
        %B: Month as locale's full name.
        %b: Month as locale's abbreviated name.
    Time Formats:
        %H: Hour (24-hour clock) as a zero-padded decimal number.
        %I: Hour (12-hour clock) as a zero-padded decimal number.
        %M: Minute as a zero-padded decimal number.
        %S: Second as a zero-padded decimal number.
        %p: Locale's equivalent of either AM or PM.
    Special Formats:
        %A: Weekday as locale's full name.
        %a: Weekday as locale's abbreviated name.
        %w: Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
"""
# ------------------------------------------------------------------

print()
# We should also know how we can go previous day or tomorrow or generate a day
# for going back and forth from datetime object we have timedelta
from datetime import timedelta

# lets take tomorrow's and yesterday's date
print("Yesterday is: ", datetime.now() - timedelta(1)) # going 1 day back so specifying 1 in timedelta parameter
print("Tomorrow is: ", datetime.now() + timedelta(1))

# generating random date
print("Random date in mind: ", datetime(2015,3,31)) # we can generate random date with datetime class directly, but it expects integer