from collections import deque


# Keeping a limited history using a collections.deque.
def search(lines, pattern, history=5):
    # A deque with limited length.
    previous_lines = deque(maxlen=history)
    for line in lines:
        # If the pattern is matched, the function yields the current line and
        # all previous lines, then it returns the control to whomever calls
        # this function, temporally.
        if pattern in line:
            yield line, previous_lines
        # Appending the current line to the deque of previous lines.
        previous_lines.append(line)


if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'No', 2):
            # Printing all previous lines.
            for prevline in prevlines:
                print(prevline, end='')
            # Printing the current line.
            print(line, end='')
            print('-' * 20)

    # Using a deque as a simple queue structure.
    q = deque([1, 2, 3, 4, 5])
    print(q)
    q.pop()
    q.popleft()
    q.append(100)
    q.appendleft(-100)
    print(q)
