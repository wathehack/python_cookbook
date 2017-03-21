from tempfile import TemporaryFile
from tempfile import NamedTemporaryFile
from tempfile import TemporaryDirectory


# The tempfile module has a variety of functions to create a temporary file
# or directory for use when a program executes.
with TemporaryFile('w+t') as f:
    # Read/write to the file.
    f.write('Hello World!')
    # Seek back to beginning and read the data.
    f.seek(0)
    data = f.read()
    # Temporary file is destroyed.

f = TemporaryFile('w+t')
f.write('Hello World!')
f.seek(0)
data = f.read()
f.close()
# Temporary file is destroyed.

# TemporaryFile() additionally accepts the same arguments as the built-in
# open() function.
with TemporaryFile('w+t', encoding='utf-8') as f:
    f.write('Hello World!')

# On most Unix systems, the file created by TemporaryFile() is unnamed and
# won't even have a directory entry. Use NamedTemporaryFile() to relax this
# constraint.
with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)

# To make a temporary directory, use tempfile.TemporaryDirectory().
with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)
