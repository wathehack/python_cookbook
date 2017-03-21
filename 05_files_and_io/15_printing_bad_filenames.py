import os
import sys


# When printing filenames of unknown origin, use the convention to avoid
# errors.
def bad_filename_1(filename):
    return repr(filename)[1:-1]

files = os.listdir('.')
for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename_1(name))


# Another option to print filenames of unknown origin is to re-encode the
# value.
def bad_filename_2(filename):
    temp = filename.encode(sys.getfilesystemencoding(),
                           errors='surrogateescape')
    return temp.decode('latin-1')

for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename_2(name))
