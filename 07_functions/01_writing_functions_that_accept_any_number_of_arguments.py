import html


# To write a function that accepts any number of positional arguments, use a
# * argument.
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

print(avg(1, 2))
print(avg(1, 2, 3, 4))


# To accept any number of keyword arguments, use an argument that starts with
# **.
def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))
    return element

print(make_element('item', 'Albatross', size='large', quantity=6))
print(make_element('p', '<spam>'))


def anyargs(*args, **kwargs):
    print(args)
    print(kwargs)

anyargs(1, 2, 3, num1=10, num2=20, num3=30)
