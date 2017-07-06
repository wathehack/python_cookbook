# In order to make an object compatible with the with statement, you need to
# implement __enter__() and __exit__() methods. Context managers are most
# commonly used in programs that need to manage resources such as files,
# network connections, and locks.
from socket import socket, AF_INET, SOCK_STREAM
from functools import partial


class LazyConnection:

    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


conn = LazyConnection(('www.python.org', 80))
# Connection closed

# The key feature of this class is that it represents a network connection,
# but it doesn't actually do anything initially (e.g., it doesn't establish a
# connection). Instead, the connection is established and closed using the
# with statement (essentially on demand).
with conn as s:
    '''
    When the with statement is first encountered, the __enter__() method is
    triggered. The return value of __enter__() (if any) is placed into the
    variable indicated with the as qualifier. Afterward, the statements in
    the body of the with statement execute. Finally, the __exit__() method is
    triggered to clean up.
    '''
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    print(resp)
    # conn.__exit__() executes: connection closed


# One subtle aspect of this recipe is whether or not the LazyConnection class
# allows nested use of the connection with multiple with statements. As shown,
# only a single socket connection at a time is allowed, and an exception is
# raised if a repeated with statement is attempted when a socket is already
# in use. You can work around this limitation with a slightly different
# implementation.
class LazyConnection:
    '''
    The LazyConnection class serves as a kind of factory for connections.
    Internally, a list is used to keep a stack. Whenever __enter__() executes,
    it makes a new connection and adds it to the stack. The __exit__() method
    simply pops the last connection off the stack and closes it.
    '''

    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()


# s1 and s2 are independent sockets
conn = LazyConnection(('www.python.org', 80))
with conn as s1:
    s1.send(b'GET /index.html HTTP/1.0\r\n')
    s1.send(b'Host: www.python.org\r\n')
    s1.send(b'\r\n')
    resp = b''.join(iter(partial(s1.recv, 8192), b''))

with conn as s2:
    s2.send(b'GET /index.html HTTP/1.0\r\n')
    s2.send(b'Host: www.python.org\r\n')
    s2.send(b'\r\n')
    resp = b''.join(iter(partial(s2.recv, 8192), b''))
