from collections import deque


# To expose extra state to the user, implement a generator as a class, putting
# the generator function code in the __iter__() method.
class linehistory:

    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


if __name__ == '__main__':
    with open('somefile.txt') as f:
        lines = linehistory(f)
        for line in lines:
            if '4' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')

    # It might require an extra step of calling iter() if you are going to
    # drive iteration using a technique other than a for loop.
    f = open('somefile.txt')
    lines = linehistory(f)
    try:
        next(lines)
    except TypeError as e:
        print(e)
    # Call iter() first, then start iterating.
    it = iter(lines)
    print(next(it))
    print(next(it))
