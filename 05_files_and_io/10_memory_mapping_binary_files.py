import os
import mmap


# Use the mmap module to memory map a binary file into a mutable byte array.
def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

size = 100
with open('somefile.bin', 'wb') as f:
    f.seek(size - 1)
    f.write(b'\x00')

m = memory_map('somefile.bin')
print(len(m), m[0:16], m[0])
m[0:16] = b'Hello, it is me!'
m.close()
with open('somefile.bin', 'rb') as f:
    print(f.read(16))

# The mmap object returned by mmap() can also be used as a context manager.
with memory_map('somefile.bin') as m:
    print(len(m))
    print(m[0:16])

m = memory_map('somefile.bin')
# Memoryview of unsigned integers.
v = memoryview(m).cast('I')
v[0] = 7
print(m[0:4])
m[0:4] = b'\x07\x01\x00\x00'
print(v[0])
