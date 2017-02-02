import os
from urllib.request import urlopen


# Checking the start or end of a string for specific text patterns, such as
# filename extensions, URL schemes, and so on.
filename = 'spam.txt'
print(filename.endswith('.txt'))

url = 'http://www.python.org'
print(url.startswith('http:'))

# Providing a tuple of possibilities to startswith() or endswith() to check
# against multiple choices.
filenames = os.listdir('.')
print(filenames)
print([name for name in filenames if name.endswith(('.c', '.h', '1.py'))])
print(any(name.endswith('.py') for name in filenames))


# A tuple is actually required as input. If you happen to have the choices
# specified in a list or set, just make sure you convert them using tuple()
# first.
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

choices = ['http:', 'ftp:']
url = 'http://www.python.org'

try:
    url.startswith(choices)
except TypeError as e:
    print(e)

print(url.startswith(tuple(choices)))
