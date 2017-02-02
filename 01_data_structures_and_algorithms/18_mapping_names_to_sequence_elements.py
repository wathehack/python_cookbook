from collections import namedtuple


# collections.namedtuple() is actually a factory method that returns a
# subclass of the standard Python tuple type. You feed it a type name, and
# the fields it should have, and it returns a class that you can
# instantiate, passing in values for the fields you've defined, and so on.
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)


def compute_cost_1(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


def compute_cost_2(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
records = [
    ('IBM', 100, 91.1),
    ('AAPL', 50, 543.22),
    ('FB', 200, 21.09),
    ('HPQ', 35, 31.75),
    ('YHOO', 45, 16.35),
    ('ACME', 75, 115.65)
]
print(compute_cost_1(records), compute_cost_2(records))

# Unlike a dictionary, a namedtuple is immutable. If you need to change
# any of the attributes, it can be done using the _replace() method of a
# namedtuple instance.
s = Stock('ACME', 100, 123.45)
print(s)

try:
    s.shares = 75
except AttributeError:
    print('A namedtuple is immutable!')

s = s._replace(shares=75)
print(s)


# A subtle use of the _replace() method is that it can be a convenient way
# to populate named tuples that have optional or missing fields.
def dict_to_stock(s):
    Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
    stock_prototype = Stock('', 0, 0.0, None, None)
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))
