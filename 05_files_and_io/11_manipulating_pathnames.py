import os


# To manipulate pathnames, use the functions in the os.path module.
path = '/Users/BillGates/money.csv'

# Get the last component of the path.
print(os.path.basename(path))

# Get the directory name.
print(os.path.dirname(path))

# Join path components together.
print(os.path.join('Apple', 'SteveJobs', os.path.basename(path)))

# Expand the user's home directory.
path = '~/Google/stock.csv'
print(os.path.expanduser(path))

# Split the file extension.
print(os.path.splitext(path))
