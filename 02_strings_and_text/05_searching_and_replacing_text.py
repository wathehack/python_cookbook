import re
from calendar import month_abbr


# Searching for and replacing a text pattern in a string.
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

# The first argument to sub() is the pattern to match and the second argument
# is the replacement pattern. Backslashed digits such as \3 refer to capture
# group numbers in the pattern.
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))


# As input, the argument to the substitution callback is a match object, as
# returned by match() or find(). Use the .group() method to extract specific
# parts of the match. The function should return the replacement text.
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print(datepat.sub(change_date, text))

# Using re.subn() to know how many substitutions were made in addition to
# getting the replacement text.
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(n)
