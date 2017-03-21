import urllib.request
import io
import sys


# If you want to add Unicode encoding/decoding to an already existing file
# object that's opened in binary mode, wrap it with an io.TextIOWrapper()
# object.
u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()

print(sys.stdout.encoding)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
print(sys.stdout.encoding)
