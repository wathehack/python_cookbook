import re


# Splitting strings on any of multiple delimiters.
line = 'asdf fjdk; afed,    fjek,asdf,             foo'

# The re.split() function is useful because you can specify multiple patterns
# for the separator.
print(re.split(r'[;,\s]\s*', line))

# If capture groups are used, then the matched text is also included in the
# result.
print(re.split(r'(;|,|\s)\s*', line))

# Maybe you need the split characters later on to reform an output string.
fields = re.split(r'(;|,|\s)\s*', line)
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)

# Reform the line using the same delimiters.
print(''.join(v + d for v, d in zip(values, delimiters)))

# If you don't want the separator characters in the result, but still need
# to use parentheses to group parts of the regular expression pattern, make
# sure you use a noncapture group, specified as (?:...).
print(re.split(r'(?:,|;|\s)\s*', line))
