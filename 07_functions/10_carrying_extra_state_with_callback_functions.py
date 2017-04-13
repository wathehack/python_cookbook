from functools import partial


# Make the callback function carry extra state for use inside the callback
# function.
def apply_async(func, args, *, callback):
    # Compute the result.
    result = func(*args)
    # Invoke the callback with the result.
    callback(result)


def print_result(result):
    print('Got:', result)


def add(x, y):
    return x + y

apply_async(add, (2, 3), callback=print_result)
apply_async(add, ('hello', 'world'), callback=print_result)


class ResultHandler:
    '''
    One way to carry extra information in a callback is to use a bound-method
    instead of a simple function. This class keeps an internal sequence
    number that is incremented every time a result is received.
    '''

    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, ('hello', 'world'), callback=r.handler)


def make_handler():
    '''
    As an alternative to a class, this function uses a closure to capture
    state.
    '''
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

    return handler

handler = make_handler()
apply_async(add, (2, 3), callback=handler)
apply_async(add, ('hello', 'world'), callback=handler)


def make_handler():
    '''
    Use a coroutine to accomplish capture state.
    '''
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

handler = make_handler()
next(handler)
# For a coroutine, use its send() method as the callback.
apply_async(add, (2, 3), callback=handler.send)
apply_async(add, ('hello', 'world'), callback=handler.send)


# Carry state into a callback using an extra argument and partial function
# application.
class SequenceNo:

    def __init__(self):
        self.sequence = 0


def handler(result, seq):
    seq.sequence += 1
    print('[{}] Got: {}'.format(seq.sequence, result))

seq = SequenceNo()
apply_async(add, (2, 3), callback=partial(handler, seq=seq))
apply_async(add, ('hello', 'world'), callback=partial(handler, seq=seq))

# Instead of using partial(), use a lambda function to capture state.
apply_async(add, (2, 3), callback=lambda r: handler(r, seq))
