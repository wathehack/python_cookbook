class Pair:
    '''
    To change the string representation of an instance, define the __str__()
    and __repr__() methods.
    '''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


# The __repr__() method returns the code representation of an instance, and is
# usually the text you would type to re-create the instance. The built-in
# repr() function returns this text, as does the interactive interpreter when
# inspecting values. The __str__() method converts the instance to a string,
# and is the output produced by the str() and print() functions.
p = Pair(3, 4)
print(p)
print('p is {0!r}'.format(p))
print('p is {0}'.format(p))
