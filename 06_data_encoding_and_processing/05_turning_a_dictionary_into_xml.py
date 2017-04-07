from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring


# Using the xml.etree.ElementTree library to create XML documents.
def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML.
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
e = dict_to_xml('stock', s)
print(e)
# Using the tostring() function in xml.etree.ElementTree to convert the XML
# into a byte string.
print(tostring(e))

# Attach attributes to an element.
e.set('_id', '1234')
print(tostring(e))
