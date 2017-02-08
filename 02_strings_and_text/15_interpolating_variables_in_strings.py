import sys


# Creating a string in which embedded variable names are substituted with a
# string representation of a variable's value.
s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))

name = 'Guido'
n = 37
print(s.format_map(vars()))


# One subtle feature of vars() is that it also works with instances.
class Info:

    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido', 37)
s.format_map(vars(a))

# One downside of format() and format_map() is that they do not deal
# gracefully with missing values.
try:
    s.format(name='Guido')
except KeyError as e:
    print(e)


# One way to avoid this is to define an alternative dictionary class with
# a __missing__() method.
class safesub(dict):

    def __missing__(self, key):
        return '{' + key + '}'

del n
print(s.format_map(safesub(vars())))


def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))
