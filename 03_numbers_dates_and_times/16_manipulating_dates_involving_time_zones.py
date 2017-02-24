from datetime import datetime
from pytz import timezone
from datetime import timedelta


# The pytz module provides the Olson time zone database, which is the de
# facto standard for time zone information found in many languages and
# operating systems.
d = datetime(2012, 12, 21, 9, 30, 0)
print(d)
# Localize the date for Chicago.
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)
# Convert to Bangalore time.
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

# Perform arithmetic with localized dates with daylight saving transitions.
d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)
