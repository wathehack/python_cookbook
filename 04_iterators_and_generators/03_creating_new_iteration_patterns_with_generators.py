# Using a generator function to implement a new kind of iteration pattern.
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(0, 4, 0.5):
    print(n)


# The mere presence of the yield statement in a function turns it into a
# generator. Unlike a normal function, a generator only runs in response to
# iteration.
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1

# Create the generator, no output appears.
c = countdown(3)
print(c)
# A generator function only runs in response to next operations carried out
# in iteration. Once a generator function returns, iteration stops. However,
# the for statement usually used to iterate takes care of these details.
try:
    while True:
        print(next(c))
except StopIteration:
    print('Done!')
