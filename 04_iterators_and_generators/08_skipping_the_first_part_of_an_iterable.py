from itertools import dropwhile
from itertools import islice


# Discarding the first few items when iterating over items in an iterable.
# To address this, Supply the itertools.dropwhile() function with a function
# and an iterable. The returned iterator discards the first items in the
# sequence as long as the supplied function returns True. Afterward, the
# entirety of the sequence is produced.
items = [10, 20, 30, 40, 50, 60, 70, 80]
for n in dropwhile(lambda n: n < 50, items):
    print(n)

# Using itertools.islice() instead if happens to know the exact number of
# items need to skip.
items = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for x in islice(items, 3, None):
    print(x)
