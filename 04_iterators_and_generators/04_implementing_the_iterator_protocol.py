class Node_1:
    '''
    Implement an iterator that traverses nodes in a depth-first pattern.
    The depth_first() method first yields itself and then iterates over each
    child yielding the items produced by the child's depth_first() method
    (using yield from).
    '''

    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node_1({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


class Node_2:
    '''
    Using an associated iterator class as an alternative implementation of
    the depth_first() method. The iterator has to maintain a lot of complex
    state about where it is in the iteration process, which is mind-bending.
    '''

    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node_2({!r})'.format(self._value)

    def add_child(self, other_node):
        self._children.append(other_node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    '''
    Depth-first traversal.
    '''

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # Return myself if just started; create an iterator for children.
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node
        # If processing a child, return its next item.
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        # Advance to the next child and start its iteration.
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)


if __name__ == '__main__':
    root = Node_1(0)
    child1 = Node_1(1)
    child2 = Node_1(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node_1(3))
    child1.add_child(Node_1(4))
    child2.add_child(Node_1(5))
    for ch in root.depth_first():
        print(ch)

    root = Node_2(0)
    child1 = Node_2(1)
    child2 = Node_2(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node_2(3))
    child1.add_child(Node_2(4))
    child2.add_child(Node_2(5))
    for ch in root.depth_first():
        print(ch)
