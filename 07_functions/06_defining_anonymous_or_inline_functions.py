# Simple functions that do nothing more than evaluate an expression can be
# replaced by a lambda expression.
add = lambda x, y: x + y
print(add(2, 3))
print(add('hello', 'world'))

names = ['David Beazley', 'Brian Jones',
         'Raymond Hettinger', 'Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))
