from datetime import datetime, timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *


# Python's datetime module has utility functions and classes to help
# perform calculations or finding a date for the last occurrence of a day
# of the week.
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

print(datetime.today())
print(get_previous_byday('Monday'))
print(get_previous_byday('Sunday', datetime(2012, 12, 21)))

d = datetime.now()
print(d)
# Next Friday.
print(d + relativedelta(weekday=FR))
# Last Friday.
print(d + relativedelta(weekday=FR(-1)))
