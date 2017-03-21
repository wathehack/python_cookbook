import sys


# Simply write the byte data to the files underlying buffer.
try:
    sys.stdout.write(b'Hello\n')
except TypeError as e:
    print(e)
sys.stdout.buffer.write(b'Hello\n')
