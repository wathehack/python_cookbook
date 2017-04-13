def recv(maxsize, *, block):
    '''
    Place the keyword arguments after a * argument or a single unnamed * to
    make a function only accept certain arguments by keyword.
    '''
    pass

try:
    recv(1024, True)
except TypeError as e:
    print(e)
recv(1024, block=True)


# This technique can also be used to specify keyword arguments for functions
# that accept a varying number of positional arguments.
def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(minimum(1, 5, 2, -5, 10))
print(minimum(1, 5, 2, -5, 10, clip=0))
