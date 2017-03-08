# To manually consume an iterable, use the next() function and catch the
# StopIteration exception.
with open('somefile.txt') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass

# Return a terminating value, such as None, if using next() manually.
with open('somefile.txt') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')

items = [1, 2, 3]
# Get the iterator, invoke items.__iter__().
it = iter(items)
# Run the iterator, invoke it.__next__().
try:
    while True:
        print(next(it))
except StopIteration:
    print('This is the end')
