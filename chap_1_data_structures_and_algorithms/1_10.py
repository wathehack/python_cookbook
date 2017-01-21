# Eliminating the duplicate values in a sequence, but preserve the order of
# the remaining items.
a = [1, 5, 2, 1, 9, 1, 5, 10]
b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]


# If the values in the sequence are hashable, the problem can be easily
# solved using a set and a generator.
def dedupe_hashable(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a_dedupe = list(dedupe_hashable(a))
print(a_dedupe)


# If the values in the sequence are unhashable (such as dicts), the problem
# can be solved by making a slight change to the above recipe.
def dedupe_unhashable(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

b_dedupe = list(dedupe_unhashable(b, key=lambda d: (d['x'], d['y'])))
print(b_dedupe)

# If all you want to do is eliminate duplicates, it is often easy enough to
# make a set. However, this approach doesn't preserve any kind of ordering.
print(set(a))
