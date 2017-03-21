from functools import partial


# Using the iter() function and functools.partial() to iterate over a
# collection of fixed-sized records or chunks.
RECORD_SIZE = 32
with open('somefile.txt', 'rb') as f:
    # The records object is an iterable that will produce fixed-sized chunks
    # until the end of the file is reached.
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)
