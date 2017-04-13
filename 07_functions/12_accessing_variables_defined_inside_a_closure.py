import sys
from timeit import timeit


# Normally, the inner variables of a closure are completely hidden to the
# outside world. However, you can provide access by writing accessor functions
# and attaching them to the closure as function attributes.
def sample():
    n = 0

    def func():
        '''
        Closure function.
        '''
        print('n=', n)

    def get_n():
        '''
        Accessor methods for n.
        '''
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes.
    func.get_n = get_n
    func.set_n = set_n
    return func

f = sample()
f()
f.set_n(10)
f()
print(f.get_n())


class ClosureInstance:

    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
        # Update instance dictionary with callables.
        self.__dict__.update((key, value) for key, value in locals.items()
                             if callable(value))

    def __len__(self):
        '''
        Redirect special methods.
        '''
        return self.__dict__['__len__']()


def Stack_1():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()

s = Stack_1()
print(s)
s.push(10)
s.push(20)
s.push('Hello')
print(len(s))
print(s.pop())
print(s.pop())
print(s.pop())


class Stack_2:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

s = Stack_1()
print(timeit('s.push(1);s.pop()', 'from __main__ import s'))
s = Stack_2()
print(timeit('s.push(1);s.pop()', 'from __main__ import s'))
