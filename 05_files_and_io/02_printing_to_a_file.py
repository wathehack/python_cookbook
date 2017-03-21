# Use the file keyword argument to print().
with open('hello.txt', 'wt') as f:
    print('Hello World!', file=f)
