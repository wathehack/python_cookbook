from collections import Iterable


# Flatten a nested sequence into a single list of values by a recursive
# generator function involving a yield from statement.
# The isinstance(x, Iterable) simply checks to see if an item is iterable. If
# so, yield from is used to emit all of its values as a kind of subroutine.
# The end result is a single sequence of output with no nesting.
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)

# The extra argument ignore_types and the check for not isinstance(x,
# ignore_types) is there to prevent strings and bytes from being interpreted
# as iterables and expanded as individual characters. This allows nested
# lists of strings to work in the way that most people would expect.
items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print(x)


# If you don't use the yield from statement, you need to use an extra for
# loop.
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield i
        else:
            yield x
