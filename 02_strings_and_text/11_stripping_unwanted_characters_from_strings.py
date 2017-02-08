import re


# The strip() method can be used to strip characters from the beginning or
# end of a string. lstrip() and rstrip() perform stripping from the left or
# right side, respectively. By default, these methods strip whitespace, but
# other characters can be given.
s = '      hello world   \n'
print(s.lstrip())
print(s.rstrip())
print(s.strip())

t = '-----hello====='
print(t.lstrip('-'))
print(t.rstrip('='))
print(t.strip('-='))

# Stripping does not apply to any text in the middle of a string.
s = '  hello         world    \n'
print(s.strip())

# Using another technique, such as using the replace() method or a regular
# expression substitution to do something to the inner space.
print(s.replace(' ', ''))
print(re.sub('\s+', ' ', s))
