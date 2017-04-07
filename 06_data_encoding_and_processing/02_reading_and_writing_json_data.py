import json
from urllib.request import urlopen
from pprint import pprint
from collections import OrderedDict


# The json module provides an easy way to encode and decode data in JSON. The
# two main functions are json.dumps() and json.loads(), mirroring the
# interface used in other serialization libraries, such as pickle.
data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
json_str = json.dumps(data)
print(json_str)
data = json.loads(json_str)
print(data)

# Use json.dump() and json.load() to encode and decode JSON data if working
# with files instead of strings.
with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)

# JSON encoding supports the basic types of None, bool, int, float, and str,
# as well as lists, tuples, and dictionaries containing those types. For
# dictionaries, keys are assumed to be strings (any nonstring keys in a
# dictionary are converted to strings when encoding).
# The format of JSON encoding is almost identical to Python syntax except for
# a few minor changes. For instance, True is mapped to true, False is mapped
# to false, and None is mapped to null.
print(json.dumps(False))
print(json.dumps({'a': True, 'b': 'Hello', 'c': None}))

# Use the pprint() function in the pprint module to pretty print the results
# of a search
u = urlopen('https://query.yahooapis.com/v1/public/yql?q=select%20item.'
            'condition%20from%20weather.forecast%20where%20woeid%20%3D%'
            '202487889&format=json&env=store%3A%2F%2Fdatatables.org'
            '%2Falltableswithkeys')
resp = json.loads(u.read().decode('utf-8'))
pprint(resp)

# Normally, JSON decoding will create dicts or lists from the supplied data.
# If you want to create different kinds of objects, supply the
# object_pairs_hook or object_hook to json.loads().
s = '{"name": "ACME", "shares": 50, "price": 490.1}'
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)


class JSONObject:
    '''
    Turn a JSON dictionary into a Python object.
    '''

    def __init__(self, d):
        self.__dict__ = d

data = json.loads(s, object_hook=JSONObject)
print(data.name)
print(data.shares)
print(data.price)

# Use the indent argument to make the output nicely formatted.
data = json.loads(s)
print(json.dumps(data, indent=4))

# Use the sort_keys argument to make the keys sorted on output.
print(json.dumps(data, sort_keys=True))


class Point:
    '''
    Serialize Instances as JSON.
    '''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def serialize_instance(obj):
        d = {'__classname__': type(obj).__name__}
        d.update(vars(obj))
        return d

    def unserialize_object(d):
        classes = {'Point': Point}
        clsname = d.pop('__classname__', None)
        if clsname:
            cls = classes[clsname]
            obj = cls.__new__(cls)
            for key, value in d.items():
                setattr(obj, key, value)
                return obj
            else:
                return d

p = Point(2, 3)
s = json.dumps(p, default=Point.serialize_instance)
print(s)
a = json.loads(s, object_hook=Point.unserialize_object)
print(a)
