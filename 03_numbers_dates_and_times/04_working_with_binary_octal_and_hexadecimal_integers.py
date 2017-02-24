# Converting or output integers represented by binary, octal, or hexadecimal
# digits.
x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

x = -1234
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

# Add in the maximum value to set the bit length and produce an unsigned
# value.
print(format(2**32 + x, 'b'))
print(format(2**32 + x, 'o'))
print(format(2**32 + x, 'x'))

# Use the int() function with an appropriate base to convert integer strings
# in different bases.
print(int('4d2', 16))
print(int('10011010010', 2))

# Use 0755 to specify the octal value will cause a SyntaxError. Make sure
# you prefix the octal value with 0o.
print(0o755)
