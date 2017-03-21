import os
import os.path
import glob
from fnmatch import fnmatch


# Use the os.listdir() function to obtain a list of files in a directory.
names = os.listdir('/Workspace/python_cookbook')
print(names, '\n')

# Get all regular files.
names = [name for name in os.listdir('.')
         if os.path.isfile(os.path.join('.', name))]
print(names, '\n')

# Get all directories.
dirnames = [name for name in os.listdir('/Workspace/python_cookbook')
            if os.path.isdir(os.path.join('/Workspace/python_cookbook', name))]
print(dirnames, '\n')

# The startswith() and endswith() methods of strings can be useful for
# filtering the contents of a directory.
pyfiles = [name for name in os.listdir('.')
           if name.endswith('.py')]
print(pyfiles, '\n')

# Use the glob or fnmatch modules for filename matching.
txtfiles = glob.glob('./*.txt')
print(txtfiles, '\n')
binfiles = [name for name in os.listdir('.')
            if fnmatch(name, '*.bin')]
print(binfiles, '\n')

# Get file sizes and modification dates.
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]
for name, size, mtime in name_sz_date:
    print(name, size, mtime)
print('\n')

# Get file metadata with os.stat.
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
print('\n')
