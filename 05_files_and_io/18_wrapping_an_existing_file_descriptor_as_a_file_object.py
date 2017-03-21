import os
import sys
from socket import socket, AF_INET, SOCK_STREAM


# A file descriptor is different than a normal open file in that it is simply
# an integer handle assigned by the operating system to refer to some kind of
# system I/O channel. If you happen to have such a file descriptor, you can
# wrap a Python file object around it using the open() function. However, you
# simply supply the integer file descriptor as the first argument instead of
# the filename.
fd = os.open('somefile.bin', os.O_WRONLY | os.O_CREAT)
# Turn into a proper file.
f = open(fd, 'wt')
f.write('Hello from the other side!\n')
f.close()

# When the high-level file object is closed or destroyed, the underlying file
# descriptor will also be closed. If this is not desired, supply the optional
# closefd=False argument to open().
fd = os.open('somefile.bin', os.O_WRONLY | os.O_CREAT)
f = open(fd, 'wt', closefd=False)
f.close()


# On Unix systems, this technique of wrapping a file descriptor can be a
# convenient means for putting a file-like interface on an existing I/O
# channel that was opened in a different way (e.g., pipes, sockets, etc.).
def echo_client(client_sock, addr):
    print('Got connection from', addr)
    # Make text-mode file wrappers for socket reading/writing.
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1',
                     closefd=False)
    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1',
                      closefd=False)
    # Echo lines back to the client using file I/O.
    for line in client_in:
        client_out.write(line)
        client_out.flush()
    client_sock.close()


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)

# Create a file object that allows emitting binary data on stdout.
bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
bstdout.write(b'Hello World!\n')
bstdout.flush()
