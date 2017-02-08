import re


# Byte strings already support most of the same built-in operations as text
# strings.
data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

# You can apply regular expression pattern matching to byte strings, but the
# patterns themselves need to be specified as bytes.
data = b'FOO:BAR,SPAM'
try:
    print(re.split('[:,]', data))
except TypeError as e:
    print(e)
print(re.split(b'[:,]', data))

# Indexing of byte strings produces integers, not individual characters.
a = 'Hello World'
print(a[0])
print(a[1])
b = b'Hello World'
print(b[0])
print(b[1])

# Byte strings don't provide a nice string representation and don't print
# cleanly unless first decoded into a text string.
s = b'Hello World'
print(s)
print(s.decode('ascii'))

# There are no string formatting operations available to byte strings.
try:
    print(b'%10s %10d %10.2f' % (b'ACME', 100, 490.1))
except TypeError as e:
    print(e)
try:
    print(b'{} {} {}'.format(b'ACME', 100, 490.1))
except AttributeError as e:
    print(e)

# Formatting applied to byte strings should be done using normal text strings
# and encoding.
print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))
