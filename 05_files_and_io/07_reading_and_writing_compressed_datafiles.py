import gzip
import bz2


# The gzip and bz2 modules make it easy to work with gzip or bz2 compression
# files.
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()

with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

# When writing compressed data, the compression level can be optionally
# specified using the compresslevel keyword argument. The default level is 9,
# which provides the highest level of compression. Lower levels offer better
# performance, but not as much compression.
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)

# gzip.open() and bz2.open() can be layered on top of an existing file opened
# in binary mode. This allows the gzip and bz2 modules to work with various
# file-like objects such as sockets, pipes, and in-memory files.
f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()
