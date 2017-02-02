# Naming a slice.
record = '....................100.......513.25....'

SHARES = slice(20, 23)
PRICE = slice(30, 36)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

items = [0, 1, 2, 3, 4, 5, 6]
print(items)

a = slice(2, 4)
print(items[a])

items[a] = [10, 11]
print(items)

del items[a]
print(items)

a = slice(5, 20, 2)
print(a.start)
print(a.stop)
print(a.step)

s = 'HelloWorld'
a.indices(len(s))
for i in range(*a.indices(len(s))):
    print(s[i])
