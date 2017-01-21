# Any sequence (or iterable) can be unpacked into variables using a simple
# assignment operation.
p = (2, 6)
x, y = p
print(x, y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, (year, mon, day) = data
print(name, shares, price, year, mon, day)

s = 'Hello'
a, b, c, d, e = s
print(a, b, c, d, e)
