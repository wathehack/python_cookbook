# Use the built-in reversed() function to iterate in reverse over a sequence.
a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)

# Reversed iteration only works if the object in question has a size that can
# be determined or if the object implements a __reversed__() special method.
# If neither of these can be satisfied, the object have to be converted into
# a list first.
f = open('somefile.txt')
for line in reversed(list(f)):
    print(line, end='')


# The reversed iteration can be customized on user defined classes if
# implementing the __reversed__() method.
class Countdown:

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


if __name__ == '__main__':
    for x in Countdown(3):
        print(x)
    for x in reversed(Countdown(3)):
        print(x)
