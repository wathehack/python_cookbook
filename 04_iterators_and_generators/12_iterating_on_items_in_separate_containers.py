from itertools import chain


# The itertools.chain() method can be used to perform the same operation on
# many objects contained in different containers.
active_items = [77, 5, 54, 21, 98]
inactive_items = [417, 19, 74]
for item in chain(active_items, inactive_items):
    print(item / 2 + 13)

# itertools.chain() accepts one or more iterables as arguments. It then works
# by creating an iterator that successively consumes and returns the items
# produced by each of the supplied iterables you provided. It's a subtle
# distinction, but chain() is more efficient than first combining the
# sequences and iterating.
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
# Inefficent.
for x in a + b:
    print(x)
# Better.
for x in chain(a, b):
    print(x)
