import os


# Using the x mode to open() to write data to a file that doesn't already
# exist on the filesystem.
if not os.path.exists('hello.txt'):
    with open('hello.txt', 'xt') as f:
        f.write('Hello, it is me!\n')
else:
    print('File already exists!')
