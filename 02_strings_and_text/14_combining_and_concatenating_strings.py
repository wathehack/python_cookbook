# Combining many small strings together into a larger string.
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

a = 'Is Chicago'
b = 'Not Chicago?'
print('{} {}'.format(a, b))
print(a + ' ' + b)

a = 'Hello' 'World'
print(a)

# Using a generator expression for conversion of data to strings and
# concatenation at the same time.
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

a, b, c = 'a', 'b', 'c'
print(a + ':' + b + ':' + c)
print(':'.join([a, b, c]))
print(a, b, c, sep=':')


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

print(''.join(sample()))
for part in sample():
    print(part)


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(sample(), 32768):
    print(part)
