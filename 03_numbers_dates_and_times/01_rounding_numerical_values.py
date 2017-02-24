# For simple rounding, use the built-in round(value, ndigits) function.
print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(1.25361, 3))

# The number of digits given to round() can be negative.
a = 1627731
print(round(a, -1))
print(round(a, -2))
print(round(a, -3))

# Using format to output a numerical value with a certain number of decimal
# places.
x = 1.23456
print(format(x, '0.2f'))
print(format(x, '0.3f'))
print('x = {:0.4f}'.format(x))

# Fixing perceived accuracy problems.
a = 2.1
b = 4.2
c = a + b
print(c)
c = round(c, 2)
print(c)
