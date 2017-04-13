def myfun():
    '''
    To return multiple values from a function, simply return a tuple.
    '''
    return 1, 2, 3

a, b, c = myfun()
print(a, b, c)

# It's actually the comma that forms a tuple, not the parentheses.
a = (1, 2)
print(a)
b = 1, 2
print(b)

x = myfun()
print(x)
