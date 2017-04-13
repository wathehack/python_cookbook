def spam(a, b=42):
    '''
    Assign values in the definition and make sure that default arguments
    appear last.
    '''
    print(a, b)

spam(1)
spam(1, 2)


def spam(a, b=None):
    '''
    If the default value is supposed to be a mutable container, such as a
    list, set, or dictionary, use None as the default.
    '''
    if b is None:
        b = []

_no_value = object()


def spam(a, b=_no_value):
    '''
    Test whether an optional argument was given an interesting value or not.
    '''
    if b is _no_value:
        print('No b value supplied')
    else:
        print(a, b)

spam(1)
spam(1, 2)
spam(1, None)


def spam(a, b=[]):
    '''
    The values assigned as defaults should always be immutable objects, such
    as None, True, False, numbers, or strings. Specifically, never use mutable
    objects.
    '''
    print(b)
    return b

x = spam(1)
x.append(99)
x.append('Yow!')
print(x)
# Modified list gets returned. To avoid this, it's better to assign None as a
# default and add a check inside the function for it.
spam(1)


def spam(a, b=None):
    '''
    The use of the is operator when testing for None is a critical part. Do
    not ust not operator. The problem here is that although None evaluates
    to False, many other objects (e.g., zero-length strings, lists, tuples,
    dicts, etc.) do as well. Thus, the test just shown would falsely treat
    certain inputs as missing.
    '''
    if not b:
        b = 'overwritten'
    print(a, b)

# OK
spam(1)
# Silent error. x value overwritten by default.
x = []
spam(1, x)
# Silent error. 0 ignored.
spam(1, 0)
# Silent error. '' ignored.
spam(1, '')
