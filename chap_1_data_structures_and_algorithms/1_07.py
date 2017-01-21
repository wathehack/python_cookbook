from collections import OrderedDict


# Using an OrderedDict from the collections module to control the order of
# items in a dictionary.
if __name__ == '__main__':
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    print(d)

    d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
    print(OrderedDict(sorted(d.items(), key=lambda t: t[1])))
