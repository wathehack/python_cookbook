import array


# Read the entire file as a single byte string.
with open('somefile.bin', 'rb') as f:
    data = f.read()
    print(data)

# Write binary data to a file.
with open('hello.bin', 'wb') as f:
    f.write(b'Hello, it is me!\n')

# Text string.
t = 'Hello World!'
for c in t:
    print(c)

# Byte string.
b = b'Hello World!'
for c in b:
    print(c)

# Decode or encode a binary-mode file If reading or writing text from it.
with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('hello.bin', 'ab') as f:
    text = 'Hello from the other side!'
    f.write(text.encode('utf-8'))

# Objects such as arrays and C structures can be used for writing without any
# kind of intermediate conversion to a bytes object.
nums = array.array('i', [1, 2, 3, 4])
with open('hello.bin', 'wb') as f:
    f.write(nums)

# Binary data can be directly read into their underlying memory using the
# readinto() method of files.
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('hello.bin', 'rb') as f:
    f.readinto(a)
    print(a)
