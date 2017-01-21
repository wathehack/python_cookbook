import os


# A very elegant way to combine a data reduction (e.g., sum(), min(), max())
# and a transformation is to use a generator-expression argument.
nums = [1, 2, 3, 4, 5]
# Creating a temporary data structure to only be used once and discarded.
print(sum([x * x for x in nums]))
# Pass generator-expr as argument.
print(sum((x * x for x in nums)))
# More elegant syntax.
print(sum(x * x for x in nums))

# Determine if any .py files exist in a directory.
files = os.listdir('.')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV.
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure.
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
print(min(s['shares'] for s in portfolio))
print(min(portfolio, key=lambda s: s['shares']))
