from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement


# Iterating over all of the possible combinations or permutations of a
# collection of items.
items = ['a', 'b', 'c']

# The itertools.permutations() takes a collection of items and produces a
# sequence of tuples that rearranges all of the items into all possible
# permutations.
for p in permutations(items):
    print(p)

for p in permutations(items, 2):
    print(p)

# Use itertools.combinations() to produce a sequence of combinations of items
# taken from the input. For combinations(), the actual order of the elements
# is not considered.
for c in combinations(items, 3):
    print(c)

for c in combinations(items, 2):
    print(c)

for c in combinations(items, 1):
    print(c)

# When producing combinations, chosen items are removed from the collection
# of possible candidates. The itertools.combinations_with_replacement()
# function relaxes this, and allows the same item to be chosen more than
# once.
for c in combinations_with_replacement(items, 3):
    print(c)
