import heapq


# Using the heapq module to implement a simple priority queue.
class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # The heapq compares the first value in the tuple, then the second,
        # the third, etc. In this example, it compares the priority value
        # first. If two items have the same priority values, it compares the
        # second value in the tuple, which is the index value.
        # The priority value is negated to get the queue to sort items from
        # highest priority to lowest priority.
        # The role of the index variable is to properly order items with the
        # same priority level. By keeping a constantly increasing index, the
        # items will be sorted according to the order in which they were
        # inserted.
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
