# Formatting a number for output, controlling the number of digits,
# alignment, inclusion of a thousands separator, and other details.
x = 1234.56789

# Two decimal places of accuracy.
print(format(x, '0.2f'))
print(format(-x, '0.2f'))

# Right justified in 10 chars, one-digit accuracy.
print(format(x, '>10.1f'))

# Left justified in 10 chars, one-digit accuracy.
print(format(x, '<10.1f'))

# Centered in 10 chars, one-digit accuracy.
print(format(x, '^10.1f'))

# Inclusion of thousands separator.
print(format(x, ','))
print(format(x, '0,.1f'))

# Change the f to an e or E to use exponential notation.
print(format(x, 'e'))
print(format(x, '0.2E'))

# The general form of the width and precision in both cases is
# '[<>^]?width[,]?(.digits)?' where width and digits are integers and ?
# signifies optional parts. The same format codes are also used in the
# .format() method of strings.
print('The value is {:0,.2f}'.format(x))

# Swap separator characters using the translate() method of strings to format
# values with a thousands separator.
swap_separators = {ord('.'): ',', ord(','): '.'}
print(format(x, ',').translate(swap_separators))
