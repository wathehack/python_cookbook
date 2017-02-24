from datetime import timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta


# To perform conversions and arithmetic involving different units of time,
# use the date time module.
# To represent an interval of time, create a timedelta instance.
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.seconds / 3600)
print(c.total_seconds() / 3600)

# To represent specific dates and times, create datetime instances and use the
# standard mathematical operations to manipulate them.
a = datetime(2012, 9, 23)
print(a + timedelta(days=10))
b = datetime(2012, 12, 21)
d = b - a
print(d.days)
now = datetime.today()
print(now)
print(now + timedelta(minutes=10))

# The datetime is aware of leap years.
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print((a - b).days, (c - d).days)

# To perform more complex date manipulations, such as dealing with time
# zones, fuzzy time ranges, calculating the dates of holidays, and so forth,
# use dateutil module.
a = datetime(2012, 9, 23)
a + relativedelta(months=+1)
a + relativedelta(months=+4)

# Time between two dates.
b = datetime(2012, 12, 21)
d = b - a
print(d)
d = relativedelta(b, a)
print(d, d.months, d.days)
