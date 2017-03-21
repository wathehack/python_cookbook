import os.path


# To read data into a mutable array, use the readinto() method of files.
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

with open('somefile.bin', 'wb') as f:
    f.write(b'I kissed a girl.\n')
buf = read_into_buffer('somefile.bin')
print(buf)

buf[0:1] = b'We'
print(buf)
with open('somefile.bin', 'ab') as f:
    f.write(buf)

# Unlike the normal read() method, readinto() fills the contents of an
# existing buffer rather than allocating new objects and returning them. It
# can be used to avoid making extra memory allocations.
record_size = 32
buf = bytearray(record_size)
with open('somefile.txt', 'rb') as f:
    while True:
        n = f.readinto(buf)
        if n < record_size:
            break
print(buf)

# Make zero-copy slices of an existing buffer and even change its contents
# with memoryview.
buf = bytearray(b'Hello World!')
m1 = memoryview(buf)
m2 = m1[:5]
print(m2)
m2[:] = b'HELLO'
print(buf)
