from collections import ChainMap


# Using the ChainMap class from the collections module to logically combine
# multiple dictionaries or mappings into a single mapping.
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print('c:', c)
print(c['x'], c['y'], c['z'])
print('length of c:', len(c))
print(list(c.keys()))
print(list(c.values()))

# If there are duplicate keys, the values from the first mapping get used.
# Operations that mutate the mapping always affect the first mapping listed.
c['z'] = 10
c['w'] = 40
del c['x']
print('a:', a)
print('c:', c)

try:
    del c['y']
except KeyError as e:
    print(e)

# A ChainMap is particularly useful when working with scoped values such
# as variables in a programming language (i.e., globals, locals, etc.).
values = ChainMap()

values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])

values = values.parents
print(values)
print(values['x'])
values = values.parents
print(values)
print(values['x'])

# As an alternative to ChainMap, you might consider merging dictionaries
# together using the update() method.
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged['x'], merged['y'], merged['z'])

# This requires to make a completely separate dictionary object. Also, if
# any of the original dictionaries mutate, the changes don't get reflected
# in the merged dictionary.
a['x'] = 13
print(merged['x'])

# A ChainMap uses the original dictionaries, so it doesn't have this behavior.
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
a['x'] = 42
print(merged['x'])
