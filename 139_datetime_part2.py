"""
- Working with Time zones
  Python datetime provides tzinfo, which is an abstract base class that allows 
  datetime.datetime and datetime.time to include time zone information, 
  including an idea of daylight saving time.

datetime does not provide a direct way to interact with the IANA time zone database.
for this we have third-party package called dateutil. 
    python -m pip install python-dateutil

Note that the name of the package that you install from PyPI, 
python-dateutil, is different from the name that you use to import the package, which is just dateutil.


"""

from dateutil import tz
from datetime import datetime

# create a datetime instance set to the current time using .now()
# We also pass the tz keyword to .now() and set tz equal to tz.tzlocal()
now = datetime.now(tz=tz.tzlocal())
print(now)
print(now.tzname())

# we can also get the different timezone with - .gettz()

London_tz = tz.gettz("Europe/London") # we pass the official IANA name for time zone (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
now = datetime.now(tz=London_tz)
print("In london: ", now)

India_tz = tz.gettz("Asia/Kolkata")
india_now = datetime.now(tz=India_tz)
print("In India: ", india_now)