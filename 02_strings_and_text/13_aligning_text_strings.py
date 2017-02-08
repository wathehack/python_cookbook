# For basic alignment of strings, the ljust(), rjust(), and center() methods
# of strings can be used.
text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

print(text.rjust(20, '='))
print(text.center(20, '*'))

# The format() function is more general purpose than using the ljust(),
# rjust(), or center() method of strings in that it works with any kind of
# object.
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))

print(format(text, '=>20s'))
print(format(text, '*^20s'))

print('{:>10s} {:>10s}'.format('Hello', 'World'))

# One benefit of format() is that it is not specific to strings. It works with
# any value, making it more general purpose.
x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))
