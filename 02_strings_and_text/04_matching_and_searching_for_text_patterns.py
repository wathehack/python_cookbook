import re


# Matching or Searching text for a specific pattern.
# match() always tries to find the match at the start of a string.
text = '11/27/2012'
if re.match(r'\d+/\d+/\d+', text):
    print('yes')
else:
    print('no')

# Precompiling the regular expression pattern into a pattern object.
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text):
    print('yes')
else:
    print('no')

# Searching text for all occurrences of a pattern using the findall() method.
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

# Capture groups often simplify subsequent processing of the matched text
# because the contents of each group can be extracted individually.
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())

print(datepat.findall(text))
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# Using the finditer() method to find matches iteratively.
for m in datepat.finditer(text):
    print(m.groups())

# If you want an exact match, make sure the pattern includes the
# end-marker ($).
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(datepat.match('11/27/2012abcdef'))
print(datepat.match('11/27/2012'))
