# Read the entire file as a single string.
with open('somefile.txt', 'rt') as f:
    data = f.read()
    print(data)

# Iterate over the lines of the file.
with open('somefile.txt', 'rt') as f:
    for line in f:
        print(line)

# Write chunks of text data.
with open('hello.txt', 'w') as f:
    f.write('Hello, it is me!\n')

# Redirected print statement.
with open('hello.txt', 'a') as f:
    print('Hello from the other side!', file=f)

# When control leaves the with block, the file will be closed automatically.
# Remember to close the file if not using the with statement.
f = open('somefile.txt', 'rt')
data = f.read()
f.close()

# An encoding or decoding error happens if not reading the file in the
# correct encoding.
# Replace bad chars with Unicode U+fffd replacement char.
f = open('somefile.txt', 'rt', encoding='ascii', errors='replace')
f.read()
f.close()

# Ignore bad chars entirely.
g = open('somefile.txt', 'rt', encoding='ascii', errors='ignore')
g.read()
f.close()
