import sys


# Using an iterator to iteratively process data until some kind of test
# condition fails.
# This scenario in programs involving I/O is to write code with while loop.
def reader(s):
    CHUNKSIZE = 8192
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)


# A little-known feature of the built-in iter() function is that it
# optionally accepts a zero argument callable and sentinel (terminating)
# value as inputs. When used in this way, it creates an iterator that
# repeatedly calls the supplied callable over and over again until it returns
# the value given as a sentinel.
def reader(s):
    CHUNKSIZE = 8192
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        process_data(data)

f = open('somefile.txt')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)
