import itertools


# The itertools.islice() function is perfectly suited for taking slices of
# iterators and generators.
def count(n):
    while True:
        yield n
        n += 1
c = count(0)
try:
    c[10:20]
except TypeError as e:
    print(e)

for x in itertools.islice(c, 10, 20):
    print(x)
