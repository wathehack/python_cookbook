import io


# Use the io.StringIO() and io.BytesIO() classes to create file-like objects
# that operate on string data.
s = io.StringIO()
s.write('Hello World!\n')
print('This is a test', file=s)
print(s.getvalue())

# Wrap a file interface around an existing string.
s = io.StringIO('Hello\nWorld!\n')
print(s.read(2))
print(s.read(3))
print(s.read())

# If operating with binary data, use the io.BytesIO class.
s = io.BytesIO()
s.write(b'binary data')
print(s.getvalue())
