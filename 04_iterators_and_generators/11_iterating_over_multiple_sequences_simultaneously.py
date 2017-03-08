from itertools import zip_longest


# To iterate over more than one sequence simultaneously, use the zip()
# function.
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, y)

# Iteration stops whenever one of the input sequences is exhausted. Thus, the
# length of the iteration is the same as the length of the shortest input.
a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a, b):
    print(i)

# The length of the iteration will be the same as the length of the longest
# input if using itertools.zip_longest().
for i in zip_longest(a, b):
    print(i)
for i in zip_longest(a, b, fillvalue=0):
    print(i)

# zip() is commonly used whenever you need to pair data together.
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s = dict(zip(headers, values))
for name, val in zip(headers, values):
    print(name, '=', val)

# zip() can be passed more than two sequences as input.
a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']
for i in zip(a, b, c):
    print(i)

# zip() creates an iterator as a result. If you need the paired values stored
# in a list, use the list() function.
print(zip(a, b))
print(list(zip(a, b)))
