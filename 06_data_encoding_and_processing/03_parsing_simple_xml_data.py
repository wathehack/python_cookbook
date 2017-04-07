from urllib.request import urlopen
from xml.etree.ElementTree import parse


# The xml.etree.ElementTree module can be used to extract data from simple XML
# documents.
# Download the RSS feed and parse it.
u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)
print(doc)

e = doc.find('channel/title')
print(e)
print(e.tag)
print(e.text)
print(e.get('language'))

# Extract and output tags of interest.
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    print(title)
    print(date)
    print(link)
