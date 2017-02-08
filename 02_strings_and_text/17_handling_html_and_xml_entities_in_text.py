import html
from html.parser import HTMLParser
from xml.sax.saxutils import unescape


# Replacing special characters such as < or > is relatively easy if using the
# html.escape() function.
s = 'Elements are written as "<tag>text</tag>".'
print(s)
print(html.escape(s))
print(html.escape(s, quote=False))

# Using the errors='xmlcharrefreplace' argument to various I/O-related
# functions to emit text as ASCII for non-ASCII characters.
s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))

s = 'Spicy &quot;Jalape&#241;o&quot.'
p = HTMLParser()
print(p.unescape(s))

t = 'The prompt is &gt;&gt;&gt;'
print(unescape(t))
