import sys
import os


# All filenames are encoded and decoded according to the text encoding
# returned by sys.getfilesystemencoding().
print(sys.getfilesystemencoding())

# Wrte a file using a unicode filename.
with open('jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')

# Directory listing (raw).
print(os.listdir(b'.'))
