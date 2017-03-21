import os
import time


# Use the os.path module to test for the existence of a file or directory.
print(os.path.exists('./hello.txt'))
print(os.path.exists('./here.txt'))

# Is a regular file.
print(os.path.isfile('./hello.txt'))

# Is a directory.
print(os.path.isdir('/Workspace/python_cookbook'))

# Is a symbolic link.
print(os.path.islink('/usr/local/bin/python3'))

# Get the file linked to.
print(os.path.realpath('/usr/local/bin/python3'))

# Get metadata of a file or directory.
print(os.path.getsize('/Workspace/python_cookbook'))
print(os.path.getmtime('/Workspace/python_cookbook'))
print(time.ctime(os.path.getmtime('/Workspace/python_cookbook')))
