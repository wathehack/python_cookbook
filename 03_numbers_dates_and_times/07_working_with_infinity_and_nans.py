import math


# Python has no special syntax to represent the floating-point values of
# infinity, negative infinity, and NaN, but they can be created using float().
a = float('inf')
b = float('-inf')
c = float('nan')
print(a, b, c)
print(math.isinf(a))
print(math.isnan(c))

print(a + 45)
print(a * 10)
print(10 / a)
print(a + a)
print(a + b)

print(c + 23)
print(c / 2)
print(c * 2)
print(math.sqrt(c))

# A subtle feature of NaN values is that they never compare as equal. Because
# of this, the only safe way to test for a NaN value is to use math.isnan().
d = float('nan')
print(c == d)
print(c is d)
